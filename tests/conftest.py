"""Pytest configuration and shared fixtures."""

import pytest


@pytest.fixture
def sample_pubkey_string():
    """Sample pubkey string for testing."""
    return "AK2c89yrVsPpFUcb9AwqhYLU1xE7atjSvmfBNzyZ75Qh"


@pytest.fixture
def sample_vault_pda_string():
    """Sample vault PDA string for testing."""
    return "GrVK5Jjm1ipfQ9doigAXXS3KDoXYBFa3Jg6aKAqhRUuC"


@pytest.fixture
def mainnet_rpc_url():
    """Mainnet RPC URL for integration tests."""
    return "https://api.mainnet-beta.solana.com"
