"""UniFi Site Manager API client."""

import requests
from typing import Dict, List, Optional, Any
from pathlib import Path
import os
from dotenv import load_dotenv


class SiteManagerClient:
    """Client for UniFi Site Manager API (cloud/remote API)."""
    
    BASE_URL = "https://api.ui.com/v1"
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Site Manager API client.
        
        Args:
            api_key: UniFi Site Manager API key. If not provided, loads from ~/.env
        """
        if api_key is None:
            # Try to load from environment
            env_path = Path.home() / '.env'
            if env_path.exists():
                load_dotenv(env_path)
            api_key = os.getenv('UNIFI_API_KEY')
        
        if not api_key:
            raise ValueError("API key required. Provide via parameter or set UNIFI_API_KEY in ~/.env")
        
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'X-API-Key': api_key,
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        })
    
    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """Make GET request to API endpoint."""
        url = f"{self.BASE_URL}/{endpoint.lstrip('/')}"
        return self.session.get(url, timeout=15, **kwargs)
    
    def get_hosts(self) -> List[Dict[str, Any]]:
        """Fetch all hosts (gateway devices)."""
        response = self.get('hosts')
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])
    
    def get_sites(self) -> List[Dict[str, Any]]:
        """Fetch all sites."""
        response = self.get('sites')
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])
    
    def get_devices(self) -> List[Dict[str, Any]]:
        """Fetch all devices."""
        response = self.get('devices')
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])
    
    def get_sd_wan_configs(self) -> List[Dict[str, Any]]:
        """Fetch SD-WAN configurations (for WAN/HA setup)."""
        response = self.get('sd-wan-configs')
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])
    
    def get_isp_metrics(self) -> Dict[str, Any]:
        """Fetch ISP metrics."""
        response = self.get('isp-metrics')
        response.raise_for_status()
        return response.json()

