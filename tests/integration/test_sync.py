"""Integration tests for ServiceNow sync."""

import pytest
from beast_unifi_servicenow.integration.unifi_sync import UniFiServiceNowSync


class TestUniFiServiceNowSync:
    """Tests for UniFi to ServiceNow sync."""
    
    def test_init(self):
        """Test UniFiServiceNowSync initialization."""
        sync = UniFiServiceNowSync(
            servicenow_url="https://test.instance.service-now.com",
            servicenow_credentials={"username": "test", "password": "test"}
        )
        assert sync.servicenow_url == "https://test.instance.service-now.com"
        assert sync.unifi_client is None
        assert sync.local_client is None
    
    def test_sync_devices_not_implemented(self):
        """Test that sync_devices raises NotImplementedError."""
        sync = UniFiServiceNowSync(
            servicenow_url="https://test.instance.service-now.com",
            servicenow_credentials={"username": "test", "password": "test"}
        )
        with pytest.raises(NotImplementedError):
            sync.sync_devices()
    
    def test_sync_sites_not_implemented(self):
        """Test that sync_sites raises NotImplementedError."""
        sync = UniFiServiceNowSync(
            servicenow_url="https://test.instance.service-now.com",
            servicenow_credentials={"username": "test", "password": "test"}
        )
        with pytest.raises(NotImplementedError):
            sync.sync_sites()

