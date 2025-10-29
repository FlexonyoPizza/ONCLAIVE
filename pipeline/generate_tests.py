import inspect
import json
import llm_utils
import importlib
import os
import test_kit_07
import tiktoken
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from glob import glob

llm_clients = llm_utils.LLMApiClient()

working_directory = os.getcwd()

base_artifacts_path = "../demo-artifacts"

# Faster generation- no LLM self evaluation
test_kit_07.generate_inferno_test_kit(
    client_instance=llm_clients, #initialize llm clients
    api_type='claude',  #set API
    test_plan_file=os.path.join(working_directory, base_artifacts_path, "test_plan", "test_plan.md"),
    ig_name='US Core',
    output_dir=os.path.join(working_directory, base_artifacts_path, "tests"),
    enable_validation=False  #disable LLM self evaluation
)
