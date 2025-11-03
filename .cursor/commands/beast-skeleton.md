# Beast Skeleton Generator

**Command:** Create a new Beast project with complete skeleton structure

## Usage

When creating a new Beast project:

1. **Create project directory:**
   ```bash
   mkdir beast-new-project
   cd beast-new-project
   ```

2. **Generate Beast skeleton:**
   - Use this template/checklist
   - Or use a script (if available)

3. **Verify skeleton:**
   - Check `.kiro/steering/BEAST_SKELETON.md` requirements
   - Ensure all directories exist
   - Ensure all files exist

## Skeleton Template

### Directory Structure
```bash
mkdir -p .cursor/commands/kiro
mkdir -p .kiro/{steering,settings/{rules,templates/{specs,steering-custom}},specs}
mkdir -p src/beast_new_project
mkdir -p {tests,notebooks,examples,docs}
```

### Required Files

1. **Core Files:**
   - `README.md` - Project description
   - `LICENSE` - MIT License
   - `pyproject.toml` - Package configuration

2. **KiroBeast Files:**
   - `docs/agents.md` - Copy from latest Beast project
   - `.kiro/steering/product.md` - Product vision
   - `.kiro/steering/tech.md` - Technology stack
   - `.kiro/steering/structure.md` - Project organization
   - `.kiro/settings/templates/steering-custom/kirobeast.md` - KiroBeast config

3. **Python Package:**
   - `src/beast_new_project/__init__.py` (not .gitkeep!)

4. **Empty Directory Tracking:**
   - `.cursor/commands/kiro/.gitkeep`
   - `.kiro/settings/rules/.gitkeep`
   - `.kiro/settings/templates/specs/.gitkeep`
   - `tests/.gitkeep`
   - `examples/.gitkeep`
   - `notebooks/.gitkeep`

### Git Setup

```bash
git init
git remote add origin https://github.com/nkllon/beast-new-project.git
git add -A
git commit -m "Initial commit: Beast skeleton structure"
git branch -M main
git push -u origin main
```

## Checklist

Before first commit, verify:
- [ ] All directories exist
- [ ] Python package has `__init__.py`
- [ ] Empty directories have `.gitkeep`
- [ ] All required files present
- [ ] Git remote configured
- [ ] README describes project
- [ ] LICENSE included (MIT)

## Notes

- **Python packages:** Use `__init__.py` (not `.gitkeep`)
- **Other directories:** Use `.gitkeep` files
- **Repository name:** `nkllon/beast-*` (hyphenated)
- **Package name:** `beast_*` (snake_case, underscore)

