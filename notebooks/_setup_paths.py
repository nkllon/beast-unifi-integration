"""
Project Path Setup Utility

Ensures notebooks always use project-relative paths regardless of where they're run from.
Add this to the first cell of any notebook:

    from _setup_paths import PROJECT_ROOT, setup_project_paths
    
    setup_project_paths()  # Sets working directory to project root
"""

from pathlib import Path
import os
import sys


def find_project_root(start_path: Path = None) -> Path:
    """
    Find project root by looking for pyproject.toml or .git directory.
    
    Args:
        start_path: Path to start searching from (defaults to current file location)
        
    Returns:
        Path to project root
        
    Raises:
        FileNotFoundError: If project root cannot be found
    """
    if start_path is None:
        # Get directory of this file (notebooks/)
        # Then go up one level to start search from parent
        try:
            file_dir = Path(__file__).parent.resolve()
            start_path = file_dir.parent  # Go up from notebooks/ to project root
        except NameError:
            # __file__ not available (e.g., in notebook)
            start_path = Path.cwd()
    
    current = Path(start_path).resolve()
    
    # Look for project root markers (check parent too if we're in notebooks/)
    markers = ['pyproject.toml', '.git', 'README.md']
    structure_markers = ['src/beast_unifi', 'src/beast_unifi_servicenow']
    
    # Check current and parent if in notebooks/
    paths_to_check = [current]
    if current.name == 'notebooks':
        paths_to_check.append(current.parent)
    
    for check_path in paths_to_check:
        # Check for marker files
        if any((check_path / marker).exists() for marker in markers):
            return check_path
        # Check for structure
        if any((check_path / marker).exists() for marker in structure_markers):
            return check_path
    
    # Walk up directory tree
    while current != current.parent:
        if any((current / marker).exists() for marker in markers):
            return current
        if any((current / marker).exists() for marker in structure_markers):
            return current
        current = current.parent
    
    raise FileNotFoundError(
        f"Could not find project root. Started from: {start_path}\n"
        f"Looking for one of: {markers + structure_markers}"
    )


def setup_project_paths(verbose: bool = True) -> Path:
    """
    Set working directory to project root and add src to Python path.
    
    Args:
        verbose: Print status messages
        
    Returns:
        Path to project root
    """
    project_root = find_project_root()
    
    # Change to project root
    if os.getcwd() != str(project_root):
        os.chdir(project_root)
        if verbose:
            print(f"✓ Changed working directory to project root:")
            print(f"  {project_root}")
    
    # Add src to Python path for imports
    src_path = project_root / 'src'
    if src_path.exists() and str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
        if verbose:
            print(f"✓ Added {src_path} to Python path")
    
    if verbose:
        print(f"✓ Ready to use project-relative paths\n")
    
    return project_root


# Global variable for easy access
PROJECT_ROOT = find_project_root()

# Auto-setup if imported (optional - can be disabled)
# setup_project_paths(verbose=False)

