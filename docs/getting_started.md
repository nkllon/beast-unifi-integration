# Getting Started

Quick start guide for using `beast-unifi-integration`.

## Installation

```bash
# Clone repository
git clone https://github.com/nkllon/beast-unifi-integration.git
cd beast-unifi-integration

# Install UV if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

## Basic Usage

### Using Site Manager API

```python
from beast_unifi import SiteManagerClient
from beast_unifi.credentials import load_credentials_from_env

# Load credentials
creds = load_credentials_from_env()
client = SiteManagerClient(api_key=creds['UNIFI_API_KEY'])

# Fetch data
hosts = client.get_hosts()
sites = client.get_sites()
devices = client.get_devices()
```

### Using Local Controller API

```python
from beast_unifi import LocalControllerClient

# Connect to local controller
client = LocalControllerClient(
    base_url="https://192.168.1.1:443",
    api_token="your-api-token",
    site="default"
)

# Fetch data
devices = client.get_devices()
clients = client.get_clients()
networks = client.get_networks()
```

### Using 1Password for Credentials

```python
from beast_unifi.credentials import load_credentials_from_1password

# Load from 1Password vault
creds = load_credentials_from_1password(vault_name="Beastmaster")

# Use credentials
from beast_unifi import SiteManagerClient
client = SiteManagerClient(api_key=creds['UNIFI_API_KEY'])
```

## Examples

See `examples/` directory for complete examples:
- `basic_sync.py` - Basic data fetching example

