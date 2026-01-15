import argparse
import html_narrative_extractor_01
import markdown_cleaner_02
import os

working_directory = os.getcwd()

demo_artifacts_path = "demo-artifacts"

parser = argparse.ArgumentParser(
    description="Convert html IG files into cleaned markdown files"
)

parser.add_argument(
    '--artifacts-dir',
    default=demo_artifacts_path,
    help="Relative path to the base artifacts directory"
)

parser.add_argument(
    '-v', '--verbose',
    default=False,
    action='store_true',
    help="Enable verbose logging"
)

parser.add_argument(
    '-e', '--exclude-pattern',
    action='append',
    help="Files matching regular expressions in this argument will be ignored"
)

args = parser.parse_args()

relative_artifacts_dir = args.artifacts_dir
verbose = args.verbose
exclude_patterns = args.exclude_pattern

final_artifacts_dir = os.path.abspath(os.path.join(working_directory, relative_artifacts_dir))

result = html_narrative_extractor_01.convert_local_html_to_markdown(
    artifacts_dir=final_artifacts_dir,
    verbose=verbose,
    exclude_patterns=exclude_patterns
)

markdown_cleaner_02.process_directory(
    artifacts_dir=final_artifacts_dir
)
