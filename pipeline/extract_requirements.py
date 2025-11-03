import llm_utils
import os
import reqs_downselect_05
import reqs_extraction_03
import reqs_reviewer_04

llm_clients = llm_utils.LLMApiClient()

working_directory = os.getcwd()

base_artifacts_path = "../artifacts-demo"

reqs_extraction_03.run_requirements_extractor(
    artifacts_dir=os.path.join(working_directory, base_artifacts_path),
    api_type= 'claude',
    client_instance=llm_clients)

reqs_reviewer_04.run_batch_requirements_refinement(
    artifacts_dir=os.path.join(working_directory, base_artifacts_path),
    client_instance=llm_clients,
    batch_size=25,
    api_type="claude"
)

reqs_downselect_05.full_pass(
    artifacts_dir=os.path.join(working_directory, base_artifacts_path)
)
