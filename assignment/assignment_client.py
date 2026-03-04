import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class AssignmentClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def solve(self, model_input):

        response = requests.post(
            f"{self.base_url}/api/Assignment",
            json=model_input,
            verify=False,
            timeout=1000
        )

        if response.status_code != 200:
            raise RuntimeError(response.text)

        return response.json()