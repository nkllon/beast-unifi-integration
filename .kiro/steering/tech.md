# Technology Stack

## Core Technologies

### Language & Runtime
- **Python 3.10+** - Primary language
- **UV** - Package management (recommended) or pip

### Libraries & Frameworks
- **requests** - HTTP client for API calls
- **python-dotenv** - Environment variable management
- **playwright** / **selenium** - Browser automation (token setup)
- **pandas** / **numpy** - Data analysis (notebooks)
- **jupyter** - Notebook environment

### Infrastructure
- **Docker** - Containerization (MID server)
- **ServiceNow MID Server** - Integration hub
- **1Password CLI** - Credential management

### Development Tools
- **Black** - Code formatting (88 char line length)
- **Ruff** - Linting (E, W, F, I, B, C4, UP rules)
- **MyPy** - Type checking (strict mode)
- **pytest** - Testing framework

## Architecture Patterns

### Package Structure
```
beast-unifi-integration/
├── src/
│   ├── beast_unifi/           # Core API clients
│   │   ├── api/               # API client implementations
│   │   ├── credentials/        # Credential management
│   │   ├── models/            # Data models
│   │   └── utils/             # Utilities
│   └── beast_unifi_servicenow/ # ServiceNow integration
│       ├── integration/       # Sync logic
│       └── mid_server/        # MID server config
```

### Credential Management Pattern
1. Try 1Password CLI first (Beastmaster vault)
2. Fallback to environment variables (~/.env)
3. Raise error if neither available

### API Client Pattern
- Session-based HTTP clients
- Consistent error handling
- Type hints throughout
- Environment-based configuration

### Notebook Pattern
- Use `_setup_paths.py` for project root detection
- Always use `PROJECT_ROOT / "relative/path"` for file paths
- Never hardcode absolute paths
- Support Docker execution environments

## Quality Standards

- **Type Safety:** All functions typed, MyPy strict mode
- **Code Style:** Black formatting, Ruff linting
- **Testing:** pytest with unit and integration tests
- **Documentation:** Docstrings for all public APIs

## Integration Patterns

- **ServiceNow:** MID server for secure, authenticated sync
- **1Password:** CLI-based credential retrieval
- **UniFi:** Both Site Manager (cloud) and Local Controller (on-prem) APIs

