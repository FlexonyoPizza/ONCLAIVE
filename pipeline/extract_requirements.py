import inspect
import json
import llm_utils
import importlib
import os
import reqs_downselect_05
import reqs_extraction_03 #import LLM requirements extraction module
import reqs_reviewer_04
import requests
import tiktoken
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from glob import glob

llm_clients = llm_utils.LLMApiClient()

working_directory = os.getcwd()

base_artifacts_path = "../demo-artifacts"

reqs_extraction_03.run_requirements_extractor(
    markdown_dir=os.path.join(working_directory, base_artifacts_path, "ig", "cleaned_markdown"),
    output_dir=os.path.join(working_directory, base_artifacts_path, "requirements", "initial_extraction"),
    api_type= 'claude',
    client_instance=llm_clients)

reqs_reviewer_04.run_batch_requirements_refinement(
    input_file=os.path.join(working_directory, base_artifacts_path, "requirements", "initial_extraction", "reqs_list_v1.md"),
    output_dir=os.path.join(working_directory, base_artifacts_path, "requirements", "revised"),
    client_instance=llm_clients,  #initialize llm clients
    batch_size=25,  #set batch size
    api_type="claude"  #set API type
)

md_files_list=reqs_downselect_05.get_md_files_from_directory(os.path.join(working_directory, base_artifacts_path, "requirements", "revised"))

reqs_downselect_05.full_pass(
    md_files=md_files_list,
    output_dir=os.path.join(working_directory, base_artifacts_path, "requirements", "final")
)
