import os
import sys

def setup_environment():
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "uv", "-q"], check=True)

def download_resources():
    import subprocess
    urls = ["https://github.com/mitkeng/SEER/raw/refs/heads/main/models/seer_neg_model.zip"]
    for url in urls:
        subprocess.run(["wget", "-q", "-nc", url])

if __name__ == "__main__":
    print("Workflow script exists and is running.")