"""Load credentials from environment variables."""

import os
from typing import Dict, Optional
from pathlib import Path
from dotenv import load_dotenv


def load_credentials_from_env(env_path: Optional[Path] = None) -> Dict[str, str]:
    """
    Load UniFi credentials from environment file.
    
    Args:
        env_path: Path to .env file (default: ~/.env)
        
    Returns:
        Dictionary with credentials (UNIFI_API_KEY, UNIFI_LOCAL_TOKEN, etc.)
    """
    if env_path is None:
        env_path = Path.home() / '.env'
    
    if env_path.exists():
        load_dotenv(env_path)
    
    credentials = {}
    
    # Site Manager API
    api_key = os.getenv('UNIFI_API_KEY')
    if api_key:
        credentials['UNIFI_API_KEY'] = api_key
    
    # Local Controller API
    local_token = os.getenv('UNIFI_LOCAL_TOKEN')
    if local_token:
        credentials['UNIFI_LOCAL_TOKEN'] = local_token
    
    # Local discovery credentials (optional)
    username = os.getenv('UNIFI_USERNAME')
    password = os.getenv('UNIFI_PASSWORD')
    
    if username:
        credentials['UNIFI_USERNAME'] = username
    if password:
        credentials['UNIFI_PASSWORD'] = password
    
    return credentials

