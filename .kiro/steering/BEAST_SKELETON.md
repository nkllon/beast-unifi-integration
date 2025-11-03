# Beast Skeleton Requirements

**Definition:** What makes a project a "Nkllon Beast" project

## Mandatory Requirements

When creating a new Beast project repository, **ALL** of the following must be present from the initial commit:

### 1. Directory Structure (All Directories Must Exist)

**Required Directories:**
```
project-name/
├── .cursor/
│   └── commands/
│       └── kiro/              # Kiro command definitions (empty ok, but must exist)
├── .kiro/
│   ├── steering/              # Product, tech, structure steering docs
│   ├── settings/
│   │   ├── rules/             # Project-specific rules (empty ok)
│   │   └── templates/
│   │       ├── specs/         # Spec templates (empty ok)
│   │       └── steering-custom/  # Custom steering templates
│   └── specs/                 # Feature specs directory
├── src/
│   └── beast_*/              # Python package (snake_case)
│       └── __init__.py       # Must exist (not .gitkeep!)
├── tests/                     # Test suite (empty ok, but must exist)
├── notebooks/                 # Jupyter notebooks (empty ok, but must exist)
├── examples/                  # Example code (empty ok, but must exist)
└── docs/                      # Documentation
```

**Important:** Empty directories must have `.gitkeep` files (except Python packages which use `__init__.py`).

### 2. Core Files

**Required Files:**
- `README.md` - Project overview
- `LICENSE` - MIT License (required for OSS)
- `pyproject.toml` - Python package configuration
- `docs/agents.md` - Agent communication patterns (copied from template)
- `.kiro/settings/templates/steering-custom/kirobeast.md` - KiroBeast configuration
- `.kiro/steering/product.md` - Product vision
- `.kiro/steering/tech.md` - Technology stack
- `.kiro/steering/structure.md` - Project organization

### 3. KiroBeast Infrastructure

**Required:**
- `.kiro/` directory structure (complete)
- `docs/agents.md` (copied from latest Beast project)
- `kirobeast.md` steering template
- At least one initial spec in `.kiro/specs/` (even if minimal)

### 4. Python Package Structure

**Required:**
- `src/beast_*/__init__.py` (not `.gitkeep`!)
- `pyproject.toml` with:
  - Project name: `beast-*` (hyphenated)
  - Package name: `beast_*` (snake_case)
  - MIT License
  - Python 3.10+ requirement
  - Black, Ruff, MyPy configuration

### 5. Git Configuration

**Required:**
- Remote configured: `nkllon/beast-*`
- Initial commit with skeleton structure
- All directories tracked (via `.gitkeep` or files)

### 6. Naming Conventions

**Required Patterns:**
- Repository: `nkllon/beast-*` (hyphenated)
- Package: `beast_*` (snake_case, underscore)
- 1Password Vault: "Beastmaster"
- GitHub Org: `nkllon`

## Empty Directory Tracking

**Rule:** Git doesn't track empty directories. Use:
- **Python packages:** `__init__.py` (not `.gitkeep`)
- **Other directories:** `.gitkeep` files

**Directories requiring `.gitkeep`:**
- `.cursor/commands/kiro/`
- `.kiro/settings/rules/`
- `.kiro/settings/templates/specs/`
- `tests/`
- `examples/`
- `notebooks/`
- Any other empty non-Python directories

## Skeleton Creation Checklist

Before first commit, verify:

- [ ] All required directories exist
- [ ] All required files exist
- [ ] Python package has `__init__.py` (not `.gitkeep`)
- [ ] Empty directories have `.gitkeep` files
- [ ] `docs/agents.md` copied from latest Beast project
- [ ] `kirobeast.md` steering template present
- [ ] Steering docs (product, tech, structure) created
- [ ] `pyproject.toml` configured correctly
- [ ] `README.md` describes project
- [ ] `LICENSE` (MIT) included
- [ ] Git remote configured: `nkllon/beast-*`
- [ ] Initial commit with complete skeleton

## Why This Matters

**Problem:** Empty directories don't exist in git clones, breaking project structure.

**Solution:** Beast skeleton ensures:
1. Consistent structure across all Beast projects
2. No missing directories on clone
3. KiroBeast infrastructure ready from day one
4. OSS-ready (LICENSE, README, proper structure)

**Rule:** Never create a new Beast project without first creating the complete skeleton.

