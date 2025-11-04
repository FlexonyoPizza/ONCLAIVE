"""
Utility functions for loading and managing prompts from external markdown files.
"""
import os
import logging
from pathlib import Path
import path_helpers
from typing import Dict, Any, Optional

def load_prompt(artifacts_dir: str, filename: str, **kwargs) -> str:
    """
    Load a prompt from a markdown file and format it with the provided kwargs.
    
    Args:
        prompt_path: Path to the prompt markdown file
        **kwargs: Variables to substitute in the prompt template
        
    Returns:
        str: Formatted prompt
    """
    prompt_path = Path(artifacts_dir) / 'prompts' / filename
    if not prompt_path.is_file():
        prompt_path = Path(path_helpers.PROJECT_ROOT) / 'default_prompts' / filename

    logging.info(f"Using prompt at: {prompt_path}")
    try:
        with open(prompt_path, 'r') as f:
            prompt_template = f.read()
            
        # Format the prompt with provided variables
        formatted_prompt = prompt_template.format(**kwargs)
        return formatted_prompt
    except FileNotFoundError:
        logging.error(f"Prompt file not found: {prompt_path}")
        raise
    except KeyError as e:
        logging.error(f"Missing parameter in prompt template: {e}")
        raise
    except Exception as e:
        logging.error(f"Error loading prompt from {prompt_path}: {str(e)}")
        raise

# def setup_prompt_environment(artifacts_dir: str) -> Dict[str, Any]:
#     """
#     Setup the prompt environment by creating directories and returning paths.

#     Returns:
#         dict: Dictionary containing prompt-related paths
#     """
#     # Define prompt directory
#     prompt_dir = Path(artifacts_dir) / 'prompts'
#     default_prompt_dir = path_helpers.PROJECT_ROOT / 'prompts'

#     # Create prompt directory if it doesn't exist
#     os.makedirs(prompt_dir, exist_ok=True)

#     # Define paths for common prompts
#     paths = {
#         "prompt_dir": prompt_dir,
#         "requirements_extraction_path": os.path.join(prompt_dir, 'reqs_extraction.md'),
#         "requirements_refinement_path": os.path.join(prompt_dir, 'reqs_refinement.md'),
#         "requirement_grouping_path": os.path.join(prompt_dir, 'reqs_grouping.md'),
#         "test_plan_gen_path": os.path.join(prompt_dir, 'test_plan.md'),
#         "test_gen_path": os.path.join(prompt_dir, 'test_gen.md')
#     }

#     logging.info(f"Prompt environment set up at: {prompt_dir}")
#     return paths

# def list_available_prompts(prompt_dir: str) -> Dict[str, str]:
#     """
#     List all available prompts in the prompt directory

#     Args:
#         prompt_dir: Path to the prompts directory

#     Returns:
#         Dictionary with prompt names as keys and file paths as values
#     """
#     if not os.path.exists(prompt_dir):
#         logging.warning(f"Prompt directory does not exist: {prompt_dir}")
#         return {}

#     prompts = {}
#     for file in os.listdir(prompt_dir):
#         if file.endswith('.md'):
#             prompt_name = os.path.splitext(file)[0]
#             prompts[prompt_name] = os.path.join(prompt_dir, file)

#     return prompts
