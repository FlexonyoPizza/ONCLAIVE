import inspect
import json
import logging
import llm_utils
import importlib
import os
import requests
import test_plan_06
import tiktoken
import urllib3
import warnings
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from glob import glob

llm_clients = llm_utils.LLMApiClient()

llm_clients.logger.setLevel(logging.INFO)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

working_directory = os.getcwd()

base_artifacts_path = "../demo-artifacts"

# Set logging level to reduce noise
logging.getLogger("urllib3.connectionpool").setLevel(logging.ERROR)
logging.getLogger("backoff").setLevel(logging.ERROR)

importlib.reload(test_plan_06)

#clearing any existing capability statements from vector database
test_plan_06.clear_capability_collection("capability_statements")

test_plan_06.generate_consolidated_test_plan(
    client_instance=llm_clients,
    api_type='claude',
    requirements_file=os.path.join(working_directory, base_artifacts_path, "requirements", "final", "consolidated_reqs.md"),
    capability_statement_file=os.path.join(working_directory, base_artifacts_path, "ig", "cleaned_markdown", "CapabilityStatement-us-core-server.md"),
    ig_name="US Core IG",
    output_dir=os.path.join(working_directory, base_artifacts_path, "test_plan"),
    verbose=True)
