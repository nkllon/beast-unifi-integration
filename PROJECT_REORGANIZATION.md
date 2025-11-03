# Project Reorganization Proposal

## Current State Analysis

### What We Have
- ✅ Multiple Jupyter notebooks (exploratory work)
- ✅ Dockerfile for ServiceNow MID server
- ✅ Helper scripts (debugging tools, launch utilities)
- ✅ Data export files (CSV, pickle, parquet)
- ✅ ERD and schema definitions
- ✅ 1Password integration examples

### What's Missing
- ❌ Proper project structure
- ❌ Dependency management (UV)
- ❌ Reusable Python packages
- ❌ Documentation
- ❌ Clear separation of concerns
- ❌ Example/demo scripts
- ❌ Tests
- ❌ CI/CD setup
- ❌ License and contribution guidelines

## End Goal

**Primary:** Demonstrate Beastmaster framework integration with ServiceNow by syncing UniFi network data.

**Presentation:** Clean, professional OSS project that shows:
1. UniFi API integration (data collection)
2. Data transformation/normalization
3. ServiceNow integration via MID server
4. Beastmaster framework usage

## Proposed Structure: Monorepo Approach

**Repository:** `nkllon/beast-unifi-integration` (or split into multiple repos)

```
beast-unifi-integration/
├── README.md                    # Project overview, quick start
├── LICENSE                      # OSS license (MIT/Apache?)
├── pyproject.toml               # UV workspace configuration
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml               # Basic CI (tests, lint)
│
├── src/                         # Main source code
│   ├── beast_unifi/             # UniFi API client library
│   │   ├── __init__.py
│   │   ├── pyproject.toml       # Package config (UV)
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── site_manager.py  # Site Manager API client
│   │   │   ├── local_controller.py  # Local Network API
│   │   │   └── auth.py          # Authentication helpers
│   │   ├── models/              # Data models
│   │   │   ├── __init__.py
│   │   │   ├── device.py
│   │   │   ├── site.py
│   │   │   └── client.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   ├── schema.py        # Schema inference
│   │   │   └── export.py        # Data export helpers
│   │   └── credentials/         # Credential management
│   │       ├── __init__.py
│   │       ├── onepassword.py
│   │       └── env.py
│   │
│   └── beast_unifi_servicenow/  # ServiceNow integration
│       ├── __init__.py
│       ├── pyproject.toml       # Package config
│       ├── integration/
│       │   ├── __init__.py
│       │   ├── unifi_sync.py    # Main sync logic
│       │   └── transformers.py  # Data transformation
│       ├── mid_server/
│       │   ├── __init__.py
│       │   └── docker/          # MID server Docker config
│       │       └── Dockerfile
│       └── models/
│           └── __init__.py
│
├── notebooks/                   # Exploratory notebooks (organized)
│   ├── discovery/
│   │   ├── api_exploration.ipynb
│   │   └── schema_inference.ipynb
│   ├── analysis/
│   │   ├── data_analysis.ipynb
│   │   └── schema_database.ipynb
│   ├── examples/
│   │   ├── basic_sync.ipynb
│   │   └── credential_setup.ipynb
│   └── README.md               # Guide to notebooks
│
├── examples/                    # Production-ready examples
│   ├── basic_sync.py           # Simple sync script
│   ├── scheduled_sync.py       # Scheduled sync with cron
│   ├── docker_compose.yml      # Example deployment
│   └── README.md
│
├── tests/                       # Test suite
│   ├── unit/
│   │   ├── test_api.py
│   │   └── test_models.py
│   ├── integration/
│   │   └── test_sync.py
│   └── fixtures/
│
├── docs/                        # Documentation
│   ├── getting_started.md
│   ├── api_reference.md
│   ├── servicenow_setup.md
│   ├── architecture.md
│   └── examples.md
│
├── scripts/                     # Utility scripts
│   ├── setup_dev.sh
│   └── launch_notebook_debug.py
│
└── docker/                      # Docker configurations
    └── mid-server/
        └── Dockerfile           # ServiceNow MID server
```

## Key Decisions

### 1. Monorepo vs Separate Repos

**Recommendation: Monorepo**
- Easier to maintain related code together
- Shared utilities and models
- Single documentation site
- Better for demonstration purposes

**Alternative:** Separate if these grow independently:
- `nkllon/beast-unifi-client` (UniFi API)
- `nkllon/beast-unifi-servicenow` (ServiceNow integration)
- `nkllon/beast-unifi-examples` (Examples/demos)

### 2. UV Workspace Structure

```toml
# pyproject.toml (workspace root)
[tool.uv]
workspace = true

[workspace]
members = [
    "src/beast_unifi",
    "src/beast_unifi_servicenow",
]

# Each package has its own pyproject.toml
```

### 3. Package Naming

- Repository: `nkllon/beast-unifi-integration` (GitHub: `nkllon/beast-unifi-integration`)
- Python package: `beast_unifi_integration` (or split into)
  - `beast_unifi` (UniFi API client)
  - `beast_unifi_servicenow` (ServiceNow integration)

### 4. Notebook Organization

**Keep notebooks but organize:**
- Discovery notebooks → `notebooks/discovery/`
- Analysis notebooks → `notebooks/analysis/`
- Examples → `notebooks/examples/`
- Clean up exported data files (add to `.gitignore`)

### 5. Data Export Strategy

- **Don't commit** exported CSV/data files
- Add `*.csv`, `*.pkl`, `*.parquet` to `.gitignore` (except examples)
- Keep schema/ERD files (they're documentation)
- Maybe add `examples/data/` with sample data

## Implementation Steps

1. **Create UV workspace structure**
   - Initialize UV project
   - Create package structure
   - Move code into packages

2. **Extract reusable code from notebooks**
   - API client code → `beast_unifi/api/`
   - Models → `beast_unifi/models/`
   - Schema inference → `beast_unifi/utils/`
   - ServiceNow sync → `beast_unifi_servicenow/integration/`

3. **Organize notebooks**
   - Move to `notebooks/` subdirectories
   - Clean up and document

4. **Create examples**
   - Simple sync script
   - Scheduled sync example
   - Docker Compose example

5. **Documentation**
   - README with quick start
   - API documentation
   - ServiceNow setup guide
   - Architecture diagrams

6. **Clean up**
   - Remove data exports from repo
   - Add to `.gitignore`
   - Clean up temp files

## Questions to Consider

1. **License:** MIT? Apache 2.0? (For ServiceNow recruiter, Apache might be safer)

2. **Beastmaster Framework:** 
   - Is this a separate library/dependency?
   - How does it integrate with these packages?
   - Should we show it as a dependency or embedded?

3. **ServiceNow Integration:**
   - REST API? MID server? Both?
   - What tables in ServiceNow? (CMDB? Custom?)
   - Transformation rules?

4. **Target Audience:**
   - ServiceNow developers?
   - Network admins?
   - DevOps engineers?

5. **Repository Name:**
   - `nkllon/beast-unifi-integration` ✅ (recommended)
   - `nkllon/beast-unifi-servicenow` (if separate)

## Next Steps

1. Decide on structure (monorepo vs separate)
2. Set up UV workspace
3. Create package structure
4. Extract code from notebooks
5. Create example scripts
6. Write documentation
7. Clean up and prepare for GitHub

