from pathlib import Path

def get_project_path(relative_path: str) -> Path:
    """
    Resolve a project-relative path no matter where the script is run from.
    Example: get_project_path("config/car_frontal_detection.yaml")
    """
    script_path = Path(__file__).resolve()
    # Go up until we find the project root (contains src/, config/, etc.)
    for parent in script_path.parents:
        if (parent / "config").exists() and (parent / "src").exists():
            return (parent / relative_path).resolve()
    raise FileNotFoundError(f"Could not find project root for path: {relative_path}")
