# Project Path Setup Guide

## The Bug

**Problem:** Notebooks use relative paths that resolve to whatever directory you run them from. If you run from Downloads or another location, files get saved there instead of the project directory.

**Example:**
```python
output_dir = "unifi_data_export"  # Relative path
os.makedirs(output_dir, exist_ok=True)
# ❌ Creates in Downloads if run from Downloads
# ✅ Should always create in project root
```

## The Fix

### Option 1: Use `_setup_paths.py` (Recommended)

Add this to the **first code cell** of your notebook:

```python
from _setup_paths import PROJECT_ROOT, setup_project_paths

# This automatically:
# 1. Finds project root (by looking for pyproject.toml, .git, etc.)
# 2. Changes working directory to project root
# 3. Adds src/ to Python path for imports
setup_project_paths()

# Now all relative paths work correctly!
output_dir = PROJECT_ROOT / "unifi_data_export"
os.makedirs(output_dir, exist_ok=True)
```

### Option 2: Manual Project Root Detection

```python
from pathlib import Path

# Find project root
def find_project_root():
    current = Path.cwd()
    while current != current.parent:
        if (current / 'pyproject.toml').exists():
            return current
        current = current.parent
    return Path.cwd()  # Fallback

PROJECT_ROOT = find_project_root()
os.chdir(PROJECT_ROOT)

# Use project-relative paths
output_dir = PROJECT_ROOT / "unifi_data_export"
```

### Option 3: Environment Variable

```python
import os
from pathlib import Path

PROJECT_ROOT = Path(os.getenv('BEAST_UNIFI_ROOT', Path.cwd()))
os.chdir(PROJECT_ROOT)
```

## Best Practices

1. **Always use `PROJECT_ROOT` for file paths:**
   ```python
   # ❌ Bad: Relative to current directory
   output_dir = "unifi_data_export"
   
   # ✅ Good: Relative to project root
   output_dir = PROJECT_ROOT / "unifi_data_export"
   ```

2. **Use Path objects, not strings:**
   ```python
   # ✅ Good
   from pathlib import Path
   file_path = PROJECT_ROOT / "data" / "export.csv"
   file_path.parent.mkdir(parents=True, exist_ok=True)
   ```

3. **Add guard checks in critical notebooks:**
   ```python
   # Warn if not in project directory
   if 'beast-unifi-integration' not in str(PROJECT_ROOT):
       print("⚠️ WARNING: Not in project directory!")
       print(f"   Current: {PROJECT_ROOT}")
   ```

## Migration Checklist

- [ ] Add `_setup_paths.py` import to all notebooks
- [ ] Replace relative paths with `PROJECT_ROOT / ...`
- [ ] Update hardcoded `/Users/lou/Downloads/...` paths
- [ ] Test notebooks from different directories
- [ ] Update documentation/examples

