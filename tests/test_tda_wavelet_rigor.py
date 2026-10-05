"""
Unit tests for TDA & Continuous Wavelet Transform Rigor (Bubenik L2, Persistence Entropy, Wavelet Spectral Entropy).
"""

import pytest
import numpy as np
import polars as pl

from bubble_detector.features.topology import (
    _takens_embedding,
    _compute_rips_persistence_diagrams,
    _compute_persistence_landscape_and_entropy,
    _compute_morlet_wavelet_energy_and_entropy,
    compute_tda_wavelet_complexity
)


def test_takens_delay_embedding_shape():
    """Verifies Takens delay coordinate embedding maps 1D series to (N, 3) point cloud."""
    r = np.random.randn(50)
    cloud = _takens_embedding(r, delay=2, dimension=3)
    assert cloud.shape == (50 - 4, 3)
    assert cloud.dtype == np.float32


def test_bubenik_l2_norm_and_persistence_entropy():
    """
    Verifies that Bubenik (2015) persistence landscape L2 norm and persistence entropy
    satisfy mathematical non-negativity and bounds.
    """
    # 1. Structured cycle: h0 components and non-trivial h1 cycle
    h0 = np.array([[0.0, 0.05], [0.0, 0.08], [0.0, 0.12]])
    h1 = np.array([[0.04, 0.14]])

    l2, entropy = _compute_persistence_landscape_and_entropy(h0, h1)
    assert l2 > 0.0
    assert l2 <= 0.25
    assert entropy > 0.0

    # 2. Empty diagrams
    empty_h0 = np.zeros((0, 2))
    empty_h1 = np.zeros((0, 2))
    l2_empty, ent_empty = _compute_persistence_landscape_and_entropy(empty_h0, empty_h1)
    assert l2_empty == 0.0
    assert ent_empty == 0.0


def test_persistence_entropy_herding_collapse():
    """
    Asserts persistence entropy E(D) drops sharply when market herding
    collapses multi-dimensional phase space dispersion into a synchronized flow.
    """
    # Herding regime: One dominant topological component dominates persistence lifetimes
    h0_herding = np.array([[0.0, 0.50], [0.0, 0.005], [0.0, 0.005]])
    h1_herding = np.zeros((0, 2))
    _, ent_herding = _compute_persistence_landscape_and_entropy(h0_herding, h1_herding)

    # Dispersed stochastic regime: Multiple components with comparable lifetimes
    h0_dispersed = np.array([[0.0, 0.20], [0.0, 0.20], [0.0, 0.20]])
    h1_dispersed = np.zeros((0, 2))
    _, ent_dispersed = _compute_persistence_landscape_and_entropy(h0_dispersed, h1_dispersed)

    assert ent_herding < ent_dispersed, (
        f"Expected entropy collapse during herding ({ent_herding:.4f}) vs dispersed ({ent_dispersed:.4f})"
    )
    assert ent_herding < 0.20, f"Herding entropy should be near 0, got {ent_herding:.4f}"


def test_morlet_wavelet_scaleogram_and_spectral_entropy():
    """
    Verifies pure-NumPy Morlet wavelet transform computes non-negative scaleogram energy
    and well-defined spectral Shannon entropy.
    """
    # Pure sinusoidal wave at specific frequency
    t = np.linspace(0, 10, 64)
    r = np.sin(2.0 * np.pi * t) * 0.02

    energy, entropy = _compute_morlet_wavelet_energy_and_entropy(r)
    assert energy > 0.0
    assert not np.isnan(energy)
    assert entropy >= 0.0
    assert not np.isnan(entropy)


def test_tda_wavelet_complexity_full_pipeline():
    """
    Asserts compute_tda_wavelet_complexity executes end-to-end and outputs
    all 4 indicators without nulls or NaNs.
    """
    np.random.seed(42)
    n = 100
    p = 100.0 * np.exp(np.cumsum(np.random.randn(n) * 0.01))
    df = pl.DataFrame({"SPY": p})

    df_out = compute_tda_wavelet_complexity(df, target_col="SPY", window_size=25)

    required_cols = [
        "TDA_Persistence_L2_Norm",
        "TDA_Persistence_Entropy",
        "Wavelet_Complexity_Score",
        "Wavelet_Spectral_Entropy"
    ]
    for col in required_cols:
        assert col in df_out.columns, f"Missing expected column: {col}"
        arr = df_out[col].to_numpy()
        assert not np.isnan(arr).any(), f"Column {col} contains NaN values"
        assert len(arr) == n

    l2_vals = df_out["TDA_Persistence_L2_Norm"].to_numpy()
    assert (l2_vals >= 0.0).all()
    assert (l2_vals <= 0.25).all()

    ent_vals = df_out["TDA_Persistence_Entropy"].to_numpy()
    assert (ent_vals >= 0.0).all()

    w_ent = df_out["Wavelet_Spectral_Entropy"].to_numpy()
    assert (w_ent >= 0.0).all()
