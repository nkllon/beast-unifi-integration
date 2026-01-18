# Project Organization

## Directory Structure

```
beast-unifi-integration/
├── src/                           # Source packages
│   ├── beast_unifi/              # Core UniFi API library
│   │   ├── api/                  # API clients
│   │   ├── credentials/          # Credential management
│   │   ├── models/               # Data models
│   │   └── utils/                # Utilities
│   └── beast_unifi_servicenow/   # ServiceNow integration
│       ├── integration/          # Sync logic
│       └── mid_server/           # MID server Docker
│
├── notebooks/                     # Jupyter notebooks
│   ├── discovery/                # API exploration
│   ├── analysis/                 # Data analysis
│   ├── examples/                 # Example workflows
│   └── _setup_paths.py          # Project root detection
│
├── examples/                      # Production-ready examples
├── tests/                         # Test suite
│   ├── unit/                     # Unit tests
│   └── integration/              # Integration tests
│
├── docs/                          # Documentation
├── scripts/                       # Utility scripts
└── .kiro/                         # BeastSpec/Kiro specs
```

## Package Organization

### beast_unifi
Core library for UniFi API access:
- `api/` - Site Manager and Local Controller clients
- `credentials/` - 1Password and environment variable management
- `models/` - Data models for UniFi entities
- `utils/` - Schema inference, export utilities

### beast_unifi_servicenow
ServiceNow integration:
- `integration/` - Sync logic and transformers
- `mid_server/` - MID server Docker configuration

## Notebook Organization

- **discovery/** - API exploration, endpoint discovery
- **analysis/** - Data analysis, schema inference
- **examples/** - Example workflows, tutorials

## Naming Conventions

- **Packages:** `beast_*` prefix (snake_case)
- **Modules:** Descriptive, lowercase (e.g., `site_manager.py`)
- **Classes:** PascalCase (e.g., `SiteManagerClient`)
- **Functions:** snake_case (e.g., `get_hosts()`)
- **Constants:** UPPER_SNAKE_CASE

## File Patterns

- **API Clients:** `api/{service_name}.py`
- **Models:** `models/{entity_name}.py`
- **Tests:** `tests/{type}/test_{module}.py`
- **Notebooks:** Descriptive names with underscores (e.g., `unifi_local_token_setup.ipynb`)

## Import Patterns

- Absolute imports from package root
- Group imports: stdlib, third-party, local
- Use `__init__.py` for package exports

