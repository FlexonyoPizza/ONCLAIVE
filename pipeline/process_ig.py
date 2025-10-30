import inspect
import json
import llm_utils
import html_narrative_extractor_01
import importlib
import markdown_cleaner_02
import os
import tiktoken
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from glob import glob

# TODO: remove this
llm_clients = llm_utils.LLMApiClient()

working_directory = os.getcwd()

base_artifacts_path = "../artifacts-demo"

# Process directory with default settings
result = html_narrative_extractor_01.convert_local_html_to_markdown(
    input_dir=os.path.join(working_directory, base_artifacts_path, "ig", "site"),
    output_dir=os.path.join(working_directory, base_artifacts_path, "ig", "converted_markdown")
)

markdown_cleaner_02.process_directory(
    input_dir=os.path.join(working_directory, base_artifacts_path, "ig", "converted_markdown"),
    output_dir=os.path.join(working_directory, base_artifacts_path, "ig", "cleaned_markdown")
)
