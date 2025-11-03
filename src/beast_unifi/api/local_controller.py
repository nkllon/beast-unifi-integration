"""UniFi Local Network Application API client."""

import requests
from typing import Dict, List, Optional, Any
from pathlib import Path
import os
from dotenv import load_dotenv


class LocalControllerClient:
    """Client for UniFi Network Application API (local controller)."""
    
    def __init__(
        self,
        base_url: str,
        api_token: Optional[str] = None,
        site: str = "default",
        verify_ssl: bool = False,
    ):
        """
        Initialize Local Network Application API client.
        
        Args:
            base_url: Base URL for local controller (e.g., "https://192.168.1.1:443")
            api_token: API token for authentication (required, 2FA needed for UniFi OS)
            site: Site name (default: "default")
            verify_ssl: Whether to verify SSL certificates (default: False for local)
        """
        if api_token is None:
            # Try to load from environment
            env_path = Path.home() / '.env'
            if env_path.exists():
                load_dotenv(env_path)
            api_token = os.getenv('UNIFI_LOCAL_TOKEN')
        
        if not api_token:
            raise ValueError(
                "API token required. UniFi OS requires 2FA, so username/password won't work. "
                "Create an API token in Settings → API Tokens and set UNIFI_LOCAL_TOKEN in ~/.env"
            )
        
        self.base_url = base_url.rstrip('/')
        self.api_token = api_token
        self.site = site
        self.session = requests.Session()
        self.session.verify = verify_ssl
        self.session.headers.update({
            'Authorization': f'Bearer {api_token}',
            'Content-Type': 'application/json',
        })
    
    def _get_endpoint(self, path: str) -> str:
        """Build full API endpoint URL."""
        # Try different endpoint patterns
        patterns = [
            f"{self.base_url}/proxy/network/api/s/{self.site}/{path}",
            f"{self.base_url}/api/s/{self.site}/{path}",
        ]
        return patterns[0]
    
    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """Make GET request to API endpoint."""
        url = self._get_endpoint(endpoint.lstrip('/'))
        return self.session.get(url, timeout=10, **kwargs)
    
    def post(self, endpoint: str, data: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Make POST request to API endpoint."""
        url = self._get_endpoint(endpoint.lstrip('/'))
        return self.session.post(url, json=data, timeout=10, **kwargs)
    
    def put(self, endpoint: str, data: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Make PUT request to API endpoint."""
        url = self._get_endpoint(endpoint.lstrip('/'))
        return self.session.put(url, json=data, timeout=10, **kwargs)
    
    def get_sites(self) -> List[Dict[str, Any]]:
        """Get all sites."""
        response = self.session.get(
            f"{self.base_url}/proxy/network/api/self/sites",
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])
    
    def get_devices(self) -> List[Dict[str, Any]]:
        """Get all devices for the site."""
        response = self.get('rest/device')
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])
    
    def get_clients(self) -> List[Dict[str, Any]]:
        """Get all clients for the site."""
        response = self.get('rest/sta')
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])
    
    def get_networks(self) -> List[Dict[str, Any]]:
        """Get network configurations."""
        response = self.get('rest/networkconf')
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])
    
    def get_vpn_tunnels(self) -> List[Dict[str, Any]]:
        """Get VPN tunnel configurations."""
        response = self.get('rest/vpntunnel')
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])
    
    def get_dynamic_dns(self) -> List[Dict[str, Any]]:
        """Get Dynamic DNS configurations."""
        response = self.get('rest/dynamicdns')
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])
    
    def get_routing(self) -> List[Dict[str, Any]]:
        """Get routing configurations."""
        response = self.get('rest/routing')
        response.raise_for_status()
        data = response.json()
        return data.get('data', [])

