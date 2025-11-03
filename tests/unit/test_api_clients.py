"""Unit tests for API clients."""

import pytest
from unittest.mock import Mock, patch
from beast_unifi.api.site_manager import SiteManagerClient
from beast_unifi.api.local_controller import LocalControllerClient


class TestSiteManagerClient:
    """Tests for SiteManagerClient."""
    
    def test_init_with_api_key(self):
        """Test initialization with API key."""
        client = SiteManagerClient(api_key="test-key")
        assert client.api_key == "test-key"
        assert client.BASE_URL == "https://api.ui.com/v1"
    
    def test_init_without_api_key_raises(self):
        """Test initialization without API key raises ValueError."""
        with patch('beast_unifi.api.site_manager.load_dotenv'), \
             patch('beast_unifi.api.site_manager.os.getenv', return_value=None):
            with pytest.raises(ValueError, match="API key required"):
                SiteManagerClient()
    
    @patch('beast_unifi.api.site_manager.requests.Session')
    def test_get_hosts(self, mock_session):
        """Test get_hosts method."""
        mock_response = Mock()
        mock_response.json.return_value = {'data': [{'id': '1', 'type': 'UDM'}]}
        mock_response.raise_for_status = Mock()
        
        mock_session_instance = Mock()
        mock_session_instance.get.return_value = mock_response
        mock_session.return_value = mock_session_instance
        
        client = SiteManagerClient(api_key="test-key")
        with patch.object(client, 'session', mock_session_instance):
            hosts = client.get_hosts()
            assert len(hosts) == 1
            assert hosts[0]['id'] == '1'
    
    @patch('beast_unifi.api.site_manager.requests.Session')
    def test_get_sites(self, mock_session):
        """Test get_sites method."""
        mock_response = Mock()
        mock_response.json.return_value = {'data': [{'id': 'site1', 'name': 'Test Site'}]}
        mock_response.raise_for_status = Mock()
        
        mock_session_instance = Mock()
        mock_session_instance.get.return_value = mock_response
        mock_session.return_value = mock_session_instance
        
        client = SiteManagerClient(api_key="test-key")
        with patch.object(client, 'session', mock_session_instance):
            sites = client.get_sites()
            assert len(sites) == 1
            assert sites[0]['id'] == 'site1'


class TestLocalControllerClient:
    """Tests for LocalControllerClient."""
    
    def test_init_with_api_token(self):
        """Test initialization with API token."""
        client = LocalControllerClient(
            base_url="https://192.168.1.1:443",
            api_token="test-token"
        )
        assert client.api_token == "test-token"
        assert client.base_url == "https://192.168.1.1:443"
        assert client.site == "default"
    
    def test_init_without_api_token_raises(self):
        """Test initialization without API token raises ValueError."""
        with patch('beast_unifi.api.local_controller.load_dotenv'), \
             patch('beast_unifi.api.local_controller.os.getenv', return_value=None):
            with pytest.raises(ValueError, match="API token required"):
                LocalControllerClient(base_url="https://192.168.1.1:443")
    
    def test_get_endpoint(self):
        """Test endpoint URL construction."""
        client = LocalControllerClient(
            base_url="https://192.168.1.1:443",
            api_token="test-token",
            site="default"
        )
        endpoint = client._get_endpoint("rest/device")
        assert "proxy/network/api/s/default/rest/device" in endpoint

