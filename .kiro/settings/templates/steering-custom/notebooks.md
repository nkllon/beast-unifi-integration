# Notebook Creation Steering

## Core Principle

**Never use relative paths that depend on working directory. Always use `PROJECT_ROOT` for all file paths.**

## The Problem

Notebooks run from various directories (project root, notebooks/, Downloads, etc.). Relative paths like `"unifi_data_export"` resolve to wherever you run the notebook from, causing:
- Files created in wrong location
- Hard to find outputs
- Data loss risk if working directory cleaned up
- Silent failures

## The Solution

Use `_setup_paths.py` in every notebook to ensure paths always resolve to project root:

```python
# First cell of every notebook:
from _setup_paths import PROJECT_ROOT, setup_project_paths

setup_project_paths()  # Changes working dir to project root

# All file paths use PROJECT_ROOT:
from pathlib import Path

output_dir = PROJECT_ROOT / "unifi_data_export"
os.makedirs(output_dir, exist_ok=True)

csv_file = PROJECT_ROOT / "data" / "export.csv"
```

## Patterns

### ✅ Correct Pattern
```python
from _setup_paths import PROJECT_ROOT
from pathlib import Path

# Always use PROJECT_ROOT
output_dir = PROJECT_ROOT / "data" / "exports"
cache_file = PROJECT_ROOT / "cache" / "data.pkl"
config_file = PROJECT_ROOT / "config" / "settings.json"
```

### ❌ Wrong Patterns
```python
# DON'T: Relative paths
output_dir = "data/exports"  # Resolves to cwd

# DON'T: Hardcoded absolute paths
output_dir = "/Users/lou/Downloads/..."  # Not portable

# DON'T: os.path without PROJECT_ROOT
output_dir = os.path.join("data", "exports")  # Still depends on cwd
```

## Required Setup Cell

Every notebook should start with:

```python
# Setup project paths
from _setup_paths import PROJECT_ROOT, setup_project_paths

setup_project_paths()

# Verify we're in the right place
print(f"Project root: {PROJECT_ROOT}")
print(f"Working directory: {os.getcwd()}")
assert str(PROJECT_ROOT) == os.getcwd(), "Working directory should be project root"
```

## File Path Patterns

### Data Exports
```python
output_dir = PROJECT_ROOT / "unifi_data_export"
os.makedirs(output_dir, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_file = output_dir / f"devices_{timestamp}.csv"
```

### Caching
```python
cache_dir = PROJECT_ROOT / "unifi_data_cache"
cache_file = cache_dir / "dataframes.pkl"
```

### Configuration
```python
config_dir = PROJECT_ROOT / "config"
config_file = config_dir / "settings.json"
```

## Docker Execution

When notebooks run in Docker, working directory is set to project root by container definition. `PROJECT_ROOT` still works correctly.

## Validation

Before committing a notebook, verify:
1. First cell imports and calls `setup_project_paths()`
2. All file paths use `PROJECT_ROOT / ...`
3. No hardcoded `/Users/...` or `~/Downloads/...` paths
4. No relative paths like `"data/exports"` without `PROJECT_ROOT`

