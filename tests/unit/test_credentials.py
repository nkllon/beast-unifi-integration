"""Unit tests for credential management."""

import pytest
from unittest.mock import patch, Mock
from pathlib import Path
import os
from beast_unifi.credentials.env import load_credentials_from_env
from beast_unifi.credentials.onepassword import load_credentials_from_1password


class TestEnvCredentials:
    """Tests for environment credential loading."""
    
    @patch('beast_unifi.credentials.env.load_dotenv')
    @patch('beast_unifi.credentials.env.os.getenv')
    def test_load_credentials_from_env(self, mock_getenv, mock_load_dotenv):
        """Test loading credentials from environment."""
        mock_getenv.side_effect = lambda key: {
            'UNIFI_API_KEY': 'test-api-key',
            'UNIFI_LOCAL_TOKEN': 'test-token',
            'UNIFI_USERNAME': 'test-user',
            'UNIFI_PASSWORD': 'test-pass',
        }.get(key)
        
        creds = load_credentials_from_env()
        assert creds['UNIFI_API_KEY'] == 'test-api-key'
        assert creds['UNIFI_LOCAL_TOKEN'] == 'test-token'
        assert creds['UNIFI_USERNAME'] == 'test-user'
        assert creds['UNIFI_PASSWORD'] == 'test-pass'
    
    @patch('beast_unifi.credentials.env.load_dotenv')
    @patch('beast_unifi.credentials.env.os.getenv', return_value=None)
    def test_load_empty_credentials(self, mock_getenv, mock_load_dotenv):
        """Test loading when no credentials are set."""
        creds = load_credentials_from_env()
        assert len(creds) == 0
    
    @patch('beast_unifi.credentials.env.Path.exists', return_value=True)
    @patch('beast_unifi.credentials.env.load_dotenv')
    def test_load_from_custom_path(self, mock_load_dotenv, mock_exists):
        """Test loading from custom env path."""
        custom_path = Path("/custom/.env")
        load_credentials_from_env(custom_path)
        mock_load_dotenv.assert_called_once()


class Test1PasswordCredentials:
    """Tests for 1Password credential loading."""
    
    @patch('beast_unifi.credentials.onepassword.subprocess.run')
    def test_load_credentials_from_1password_success(self, mock_run):
        """Test loading credentials from 1Password."""
        mock_result = Mock()
        mock_result.returncode = 0
        mock_result.stdout = '[{"value": "test-api-key"}]'
        mock_run.return_value = mock_result
        
        creds = load_credentials_from_1password("Beastmaster")
        # Should attempt to load credentials
        assert mock_run.called
    
    @patch('beast_unifi.credentials.onepassword.subprocess.run')
    def test_load_credentials_from_1password_failure(self, mock_run):
        """Test handling 1Password CLI failures gracefully."""
        mock_result = Mock()
        mock_result.returncode = 1
        mock_run.return_value = mock_result
        
        # Should not raise, just return empty dict
        creds = load_credentials_from_1password("Beastmaster")
        assert isinstance(creds, dict)

