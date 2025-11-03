# beast-unifi-integration

UniFi network data integration with ServiceNow via Beastmaster framework.

> **Demonstration Project**: Showcasing Beastmaster framework integration capabilities with ServiceNow for network infrastructure management.

## Overview

This project provides:

1. **UniFi API Client** (`beast_unifi`) - Python library for interacting with UniFi Site Manager API and local controllers
2. **ServiceNow Integration** (`beast_unifi_servicenow`) - ServiceNow integration for syncing UniFi network data via MID server
3. **Example Notebooks** - Exploratory notebooks for API discovery, data analysis, and schema inference

## Quick Start

### Prerequisites

- Python 3.10+
- UV package manager (recommended) or pip
- UniFi API credentials (Site Manager API key or local controller access)
- ServiceNow instance with MID server (for integration)

### Installation

```bash
# Install UV if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone repository
git clone https://github.com/nkllon/beast-unifi-integration.git
cd beast-unifi-integration

# Install dependencies
uv sync
```

### Basic Usage

```python
from beast_unifi import SiteManagerClient

# Initialize client
client = SiteManagerClient(api_key="your-api-key")

# Fetch hosts/sites
hosts = client.get_hosts()
sites = client.get_sites()
devices = client.get_devices()
```

## Project Structure

```
beast-unifi-integration/
├── src/
│   ├── beast_unifi/              # UniFi API client library
│   │   ├── api/                  # API clients
│   │   ├── models/               # Data models
│   │   ├── utils/                # Utilities (schema, export)
│   │   └── credentials/          # Credential management
│   │
│   └── beast_unifi_servicenow/   # ServiceNow integration
│       ├── integration/          # Sync logic
│       └── mid_server/           # MID server Docker config
│
├── notebooks/                     # Exploratory notebooks
│   ├── discovery/                # API exploration
│   ├── analysis/                 # Data analysis
│   └── examples/                 # Example workflows
│
├── examples/                      # Production-ready examples
├── tests/                         # Test suite
└── docs/                          # Documentation
```

## Documentation

- [Getting Started](docs/getting_started.md)
- [API Reference](docs/api_reference.md)
- [ServiceNow Setup](docs/servicenow_setup.md)
- [Architecture](docs/architecture.md)

## Contributing

Contributions welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Related Projects

Part of the Beastmaster framework ecosystem:
- [beast-devkit](https://github.com/nkllon/beast-devkit)
- [beast-validators](https://github.com/nkllon/beast-validators)
- [beast-observability](https://github.com/nkllon/beast-observability)

