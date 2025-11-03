import llm_utils
import os
import test_kit_07

llm_clients = llm_utils.LLMApiClient()

working_directory = os.getcwd()

base_artifacts_path = "../artifacts-demo"

# TODO: add command line param for self evaluation
test_kit_07.generate_inferno_test_kit(
    client_instance=llm_clients,
    api_type='claude',
    artifacts_dir=os.path.join(working_directory, base_artifacts_path),
    ig_name='US Core',
    enable_validation=False
)
