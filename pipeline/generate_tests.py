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
    test_plan_file=os.path.join(working_directory, base_artifacts_path, "test_plan", "test_plan.md"),
    ig_name='US Core',
    output_dir=os.path.join(working_directory, base_artifacts_path, "tests"),
    enable_validation=False
)
