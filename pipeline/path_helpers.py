def project_root() -> Path:
    Path(__file__).parent.parent

def demo_artifacts_path() -> Path:
    Path(__file__).parent / "demo-artifacts" / "ig" / "site" / "CapabilityStatement-us-core-server.html"
