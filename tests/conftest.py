"""Pytest configuration and fixtures."""

import pytest
from pathlib import Path


@pytest.fixture
def test_data_dir():
    """Return path to test data directory."""
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def mock_env_file(tmp_path):
    """Create a temporary .env file for testing."""
    env_file = tmp_path / ".env"
    env_file.write_text(
        "UNIFI_API_KEY=test-api-key\n"
        "UNIFI_LOCAL_TOKEN=test-token\n"
        "UNIFI_USERNAME=test-user\n"
        "UNIFI_PASSWORD=test-pass\n"
    )
    return env_file

