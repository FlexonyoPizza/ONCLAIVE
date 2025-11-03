import html_narrative_extractor_01
import markdown_cleaner_02
import os

working_directory = os.getcwd()

base_artifacts_path = "../artifacts-demo"

result = html_narrative_extractor_01.convert_local_html_to_markdown(
    artifacts_dir=os.path.join(working_directory, base_artifacts_path)
)

markdown_cleaner_02.process_directory(
    artifacts_dir=os.path.join(working_directory, base_artifacts_path)
)
