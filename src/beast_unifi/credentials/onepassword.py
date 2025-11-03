"""Load credentials from 1Password CLI."""

import subprocess
import json
import os
from typing import Dict, Optional


def load_credentials_from_1password(vault_name: str = "Beastmaster") -> Dict[str, str]:
    """
    Load UniFi credentials from 1Password vault.
    
    Args:
        vault_name: Name of the 1Password vault (default: "Beastmaster")
        
    Returns:
        Dictionary with credentials (UNIFI_API_KEY, UNIFI_LOCAL_TOKEN, etc.)
    """
    credentials = {}
    
    # Item names and field mappings
    items = {
        'UNIFI_API_KEY': ('UniFi Site Manager API Key', 'api_key'),
        'UNIFI_LOCAL_TOKEN': ('UniFi Local API Token', 'api_token'),
        'UNIFI_USERNAME': ('UniFi Username', 'username'),
        'UNIFI_PASSWORD': ('UniFi Password', 'password'),
    }
    
    for env_var, (item_name, field_name) in items.items():
        try:
            result = subprocess.run(
                ['op', 'item', 'get', item_name, '--vault', vault_name,
                 '--fields', field_name, '--format', 'json'],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode == 0:
                try:
                    field_data = json.loads(result.stdout)
                    if isinstance(field_data, list) and len(field_data) > 0:
                        value = field_data[0].get('value', '')
                    elif isinstance(field_data, dict):
                        value = field_data.get('value', '') or field_data.get(field_name, '')
                    else:
                        value = result.stdout.strip()
                    
                    if value:
                        credentials[env_var] = value
                        os.environ[env_var] = value
                except json.JSONDecodeError:
                    # Sometimes op returns plain text
                    value = result.stdout.strip()
                    if value:
                        credentials[env_var] = value
                        os.environ[env_var] = value
        except Exception:
            # Silently skip if item doesn't exist or CLI not available
            pass
    
    return credentials

