import requests
import os

PROMPTS_REPO = "kjgarza/prompts"
PROMPTS_FILE = "parrot_gpt.yml"

class PromptsService:
    def __init__(self):
        self.base_url = "https://api.github.com/repos"
        self.token = os.getenv("GITHUB_TOKEN")

    def get_yaml_file(self, repo_name = PROMPTS_REPO, file_name = PROMPTS_FILE):
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3.raw"
        }
        response = requests.get(f"{self.base_url}/{repo_name}/contents/{file_name}", headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            response.raise_for_status()