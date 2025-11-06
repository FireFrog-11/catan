from pathlib import Path

def get_project_root():
    current = Path(__file__).resolve()

    # Traverse parent dirs until we find requirements.txt
    for parent in [current] + list(current.parents):
        if (parent / "requirements.txt").exists():
            return parent

    raise FileNotFoundError("Could not find project root (no requirements.txt).")