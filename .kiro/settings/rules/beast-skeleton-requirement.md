# Rule: Beast Skeleton Requirement

**Type:** Mandatory Project Setup Rule  
**Applies To:** All new Beast project repositories  
**Enforcement:** Must be followed before first commit

## Rule Statement

**WHEN creating a new Beast project repository THEN it MUST include the complete Beast skeleton structure from the initial commit.**

**Rationale:** 
- Ensures consistent project structure across all Beast projects
- Prevents missing directories in git clones (empty directories aren't tracked)
- Ensures KiroBeast infrastructure is ready from day one
- Makes projects OSS-ready immediately

## Requirements

See `.kiro/steering/BEAST_SKELETON.md` for complete requirements.

**Minimum Requirements:**
1. All required directories exist (with `.gitkeep` or `__init__.py`)
2. Core files present (README, LICENSE, pyproject.toml, docs/agents.md)
3. KiroBeast infrastructure (`.kiro/` structure, steering docs, kirobeast.md)
4. Python package structure (`src/beast_*/__init__.py`)
5. Git remote configured (`nkllon/beast-*`)

## Enforcement

**Before First Commit:**
- Verify all directories exist
- Verify all required files exist
- Verify empty directories have `.gitkeep` (except Python packages)
- Verify Python packages have `__init__.py` (not `.gitkeep`)
- Verify git remote is configured

**This Rule Applies To:**
- LLMs creating new Beast projects
- Developers creating new Beast projects
- Any repository under `nkllon/beast-*`

## Exceptions

**None.** All Beast projects must follow this rule.

## Related Documents

- `.kiro/steering/BEAST_SKELETON.md` - Complete skeleton requirements
- `.kiro/steering/structure.md` - Project organization patterns
- `docs/agents.md` - Universal Beast project patterns

