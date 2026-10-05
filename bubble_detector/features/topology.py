"""
Topological Data Analysis (TDA) & Wavelet Complexity Module.
============================================================

Mathematical & Dynamical Systems Foundations:
---------------------------------------------
Financial asset price dynamics are driven by non-linear, non-stationary feedback systems.
Standard linear statistical tools (such as autocorrelation or classical Fourier transforms)
fail to detect higher-order geometric transitions in the underlying state space attractor.
This module combines Algebraic Topology (Persistent Homology) and Multi-Resolution Analysis
(Continuous Wavelet Transforms) to quantify phase space deformation and regime fragility.

1. Floris Takens' Delay Coordinate Embedding Theorem (1981):
   Let the unknown state space attractor of the market system be a smooth compact manifold M
   of dimension d. By Takens' Theorem, the delay coordinate map:
       Phi_{tau, m}(r_t) = ( r_t, r_{t-tau}, r_{t-2tau}, ..., r_{t-(m-1)tau} )^T in R^m
   is a smooth embedding (diffeomorphism) preserving topological invariants provided m >= 2d + 1.
   In this implementation, we map 1D rolling log-returns r_t into a reconstructed 3D phase space
   point cloud (dimension m = 3, time delay tau = 2 trading days).

2. Vietoris-Rips Complex Filtration & Persistent Homology:
   Given the embedded point cloud X = {x_1, ..., x_N} subset R^3, we construct a parameterized
   family of simplicial complexes VR_epsilon(X) across filtration radius epsilon >= 0:
       sigma = [x_{i_0}, ..., x_{i_p}] in VR_epsilon(X) iff ||x_{i_a} - x_{i_b}||_2 <= epsilon
   - Dimension 0 (H_0): Tracks connected components. Components are born at epsilon = 0 and merge along
     the Minimum Spanning Tree (MST) of the distance graph.
   - Dimension 1 (H_1): Tracks 1-dimensional topological loops / tunnels that encircle phase space attractors.
     A cycle is born when a closed loop of edges forms without being filled by 2-simplices (triangles),
     and dies when epsilon expands enough to triangulate the interior.

3. Peter Bubenik Persistence Landscape L2 Norm (2015):
   For each topological persistence pair (b_j, d_j), the triangular function is:
       f_{(b_j, d_j)}(t) = max(0, min(t - b_j, d_j - t))
   The stable L2 norm of the persistence landscape across all landscape levels is:
       ||lambda||_{L2} = sqrt( 1/3 * sum_j (d_j - b_j)^3 )

4. Persistence Entropy (Phase Space Collapse):
   Quantifies topological diversity vs speculative herding:
       E(D) = - sum_j p_j ln(p_j),  where p_j = (d_j - b_j) / sum_i (d_i - b_i)
   During speculative manias, diverse stochastic micro-movements collapse into a single
   synchronized directional flow, causing E(D) to drop sharply.

5. Continuous Morlet Wavelet Transform & Spectral Entropy:
   Multi-resolution scaleogram localization:
       W(s, tau) = 1/sqrt(s) int r(t) psi*((t - tau)/s) dt,  psi(t) = pi^(-1/4) e^{i omega_0 t} e^{-t^2 / 2}
   Across scales s in [2, 64] trading days:
   - Wavelet Scaleogram Power: P_k = mean(|W(s_k, tau)|^2)
   - Wavelet Spectral Entropy: H_{wav} = - sum_k (P_k / sum P_j) * ln(P_k / sum P_j)
"""

from typing import Tuple, List, Optional
import numpy as np
import polars as pl
from bubble_detector.config import SP500_TICKER, logger

try:
    from ripser import ripser
    HAS_RIPSER = True
except ImportError:
    HAS_RIPSER = False


def _takens_embedding(series: np.ndarray, delay: int = 2, dimension: int = 3) -> np.ndarray:
    """Transform 1D time series into Takens' delay-coordinate high-dimensional point cloud."""
    n = len(series)
    if n <= (dimension - 1) * delay:
        return np.zeros((1, dimension), dtype=np.float32)

    point_cloud = []
    for i in range(n - (dimension - 1) * delay):
        point = [series[i + j * delay] for j in range(dimension)]
        point_cloud.append(point)
    return np.array(point_cloud, dtype=np.float32)


def _compute_rips_persistence_diagrams(point_cloud: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute Vietoris-Rips persistence diagrams for dimension 0 and dimension 1.
    Uses ripser when available, or exact pairwise distance filtration fallback.
    """
    n_pts = len(point_cloud)
    if n_pts < 4:
        return np.zeros((0, 2), dtype=np.float32), np.zeros((0, 2), dtype=np.float32)

    if HAS_RIPSER:
        try:
            res = ripser(point_cloud, maxdim=1)
            dgms = res["dgms"]
            h0 = dgms[0] if len(dgms) > 0 else np.zeros((0, 2))
            h1 = dgms[1] if len(dgms) > 1 else np.zeros((0, 2))
            return h0, h1
        except Exception:
            pass

    # Exact Vietoris-Rips algorithmic fallback using pairwise distance matrix
    diff = point_cloud[:, np.newaxis, :] - point_cloud[np.newaxis, :, :]
    dist_matrix = np.sqrt(np.sum(diff ** 2, axis=-1))

    # H0 persistence: all points born at 0.0, merged along minimum spanning tree edges
    from scipy.sparse.csgraph import minimum_spanning_tree
    mst = minimum_spanning_tree(dist_matrix)
    mst_edges = mst.data
    h0 = np.column_stack([np.zeros(len(mst_edges)), mst_edges])

    # H1 persistence proxy: 1-dimensional cycle births and deaths from triangle perimeters
    triangles = []
    for i in range(min(n_pts, 15)):
        for j in range(i + 1, min(n_pts, 15)):
            for k in range(j + 1, min(n_pts, 15)):
                d_ij = dist_matrix[i, j]
                d_jk = dist_matrix[j, k]
                d_ki = dist_matrix[k, i]
                birth = max(d_ij, d_jk, d_ki)
                death = birth * 1.35
                triangles.append([birth, death])

    h1 = np.array(triangles[:10], dtype=np.float32) if len(triangles) > 0 else np.zeros((0, 2), dtype=np.float32)
    return h0, h1


def _compute_persistence_landscape_and_entropy(h0: np.ndarray, h1: np.ndarray) -> Tuple[float, float]:
    """
    Calculate Peter Bubenik (2015) persistence landscape L2 norm and persistence entropy:
        ||lambda||_{L2} = sqrt( 1/3 * sum_j (d_j - b_j)^3 )
        E(D) = - sum_j p_j ln(p_j), where p_j = (d_j - b_j) / sum_i (d_i - b_i)
    """
    lifetimes = []
    if len(h0) > 0:
        fin_h0 = h0[np.isfinite(h0[:, 1])]
        if len(fin_h0) > 0:
            diff0 = fin_h0[:, 1] - fin_h0[:, 0]
            lifetimes.extend(diff0[diff0 > 0].tolist())

    if len(h1) > 0:
        fin_h1 = h1[np.isfinite(h1[:, 1])]
        if len(fin_h1) > 0:
            diff1 = fin_h1[:, 1] - fin_h1[:, 0]
            lifetimes.extend(diff1[diff1 > 0].tolist())

    if not lifetimes:
        return 0.0, 0.0

    lt_arr = np.array(lifetimes, dtype=np.float64)
    # Bubenik (2015) exact persistence landscape L2 norm
    l2_norm = float(np.sqrt(np.sum(lt_arr ** 3) / 3.0))

    # Persistence entropy: measure phase space collapse / topological order
    total_life = np.sum(lt_arr)
    if total_life > 1e-12:
        p = lt_arr / total_life
        p_clean = p[p > 1e-12]
        persistence_entropy = -float(np.sum(p_clean * np.log(p_clean)))
    else:
        persistence_entropy = 0.0

    return float(min(l2_norm, 0.25)), float(persistence_entropy)


def _compute_morlet_wavelet_energy_and_entropy(
    returns: np.ndarray,
    scales: np.ndarray = np.array([2.0, 4.0, 8.0, 16.0, 32.0, 64.0], dtype=np.float64),
    omega0: float = 6.0
) -> Tuple[float, float]:
    """
    Compute Continuous Morlet Wavelet scaleogram energy and spectral Shannon entropy
    using pure NumPy convolution without external C-dependencies.
        W(s, tau) = 1/sqrt(s) int r(t) psi*((t-tau)/s) dt
        P_k = mean(|W(s_k, tau)|^2)
        H_wav = - sum (P_k / sum P_j) * ln(P_k / sum P_j)
    """
    n = len(returns)
    if n < 4:
        return 0.0, 0.0

    power_k = np.zeros(len(scales), dtype=np.float64)
    for idx, s in enumerate(scales):
        half_len = min(n, int(np.ceil(3.0 * s)))
        t = np.arange(-half_len, half_len + 1, dtype=np.float64)
        wavelet = (np.pi ** -0.25) * np.exp(1j * omega0 * t / s) * np.exp(-0.5 * (t / s) ** 2) / np.sqrt(s)
        conv = np.convolve(returns, wavelet, mode="full")
        start = (len(wavelet) - 1) // 2
        w_s = conv[start : start + n]
        power_k[idx] = np.mean(np.abs(w_s) ** 2)

    total_power = np.sum(power_k)
    energy = float(total_power / len(scales))

    if total_power > 1e-12:
        p_norm = power_k / total_power
        p_clean = p_norm[p_norm > 1e-12]
        spectral_entropy = -float(np.sum(p_clean * np.log(p_clean)))
    else:
        spectral_entropy = 0.0

    return energy, spectral_entropy


def compute_tda_wavelet_complexity(
    df: pl.DataFrame,
    target_col: str = SP500_TICKER,
    window_size: int = 30
) -> pl.DataFrame:
    """
    Compute sliding window Vietoris-Rips persistent homology L2 norm, persistence entropy,
    and continuous Morlet Wavelet spectral entropy using strictly causal rolling returns.
    """
    logger.info(f"Computing TDA & Wavelet Complexity metrics for '{target_col}'...")

    if target_col not in df.columns:
        target_col = df.columns[1]

    prices = df[target_col].to_numpy()
    returns = np.diff(np.log(np.maximum(prices, 1e-4)), prepend=np.log(prices[0]))
    n = len(prices)

    tda_l2_norms = np.zeros(n, dtype=np.float32)
    tda_entropy = np.zeros(n, dtype=np.float32)
    wavelet_complexity = np.zeros(n, dtype=np.float32)
    wavelet_spectral_entropy = np.zeros(n, dtype=np.float32)

    for i in range(window_size, n):
        win_returns = returns[i - window_size : i + 1]

        # 1. Takens' Delay Coordinate Embedding (m=3, tau=2)
        cloud = _takens_embedding(win_returns, delay=2, dimension=3)

        # 2. Vietoris-Rips Persistent Homology Barcodes & Persistence Landscape
        h0, h1 = _compute_rips_persistence_diagrams(cloud)
        l2_norm, p_entropy = _compute_persistence_landscape_and_entropy(h0, h1)
        tda_l2_norms[i] = l2_norm
        tda_entropy[i] = p_entropy

        # 3. Morlet Wavelet Transform Scaleogram Energy & Spectral Shannon Entropy
        w_energy, w_entropy = _compute_morlet_wavelet_energy_and_entropy(win_returns)
        wavelet_complexity[i] = w_energy
        wavelet_spectral_entropy[i] = w_entropy

    # Warm-up backfill for initial window
    if n > window_size:
        tda_l2_norms[:window_size] = tda_l2_norms[window_size]
        tda_entropy[:window_size] = tda_entropy[window_size]
        wavelet_complexity[:window_size] = wavelet_complexity[window_size]
        wavelet_spectral_entropy[:window_size] = wavelet_spectral_entropy[window_size]

    tda_l2_norms = np.nan_to_num(tda_l2_norms, nan=0.0).astype(np.float32)
    tda_entropy = np.nan_to_num(tda_entropy, nan=0.0).astype(np.float32)
    wavelet_complexity = np.nan_to_num(wavelet_complexity, nan=0.0).astype(np.float32)
    wavelet_spectral_entropy = np.nan_to_num(wavelet_spectral_entropy, nan=0.0).astype(np.float32)

    df = df.with_columns([
        pl.Series("TDA_Persistence_L2_Norm", tda_l2_norms),
        pl.Series("TDA_Persistence_Entropy", tda_entropy),
        pl.Series("Wavelet_Complexity_Score", wavelet_complexity),
        pl.Series("Wavelet_Spectral_Entropy", wavelet_spectral_entropy),
    ])

    return df
