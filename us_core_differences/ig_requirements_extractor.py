import path_helpers
from pathlib import Path
import requests

def load_and_extract_ig_requirements(
    old_requirements_location: str,
    artifacts_dir: str,
    verbose: bool = False
):
    """
    Docstring for load_and_extract_ig_requirements
    
    :param old_requirements_location: Description
    :type old_requirements_location: str
    :param artifacts_dir: Description
    :type artifacts_dir: str
    :param verbose: Description
    :type verbose: bool
    """
    artifacts_path = Path(artifacts_dir)
    old_ig_requirements_dir = artifacts_path / "ig" / "site" / "old"

    old_ig_requirements_dir.mkdir(parents=True, exist_ok=True)

    if verbose:
        # might need to change message if directory already existed
        print(f"Created directories: {old_ig_requirements_dir}")

    # Process IG requirements source (local CSV files)

    
    # Convert xlsx into Markdown? CVS? Will this make the LLM perform better?