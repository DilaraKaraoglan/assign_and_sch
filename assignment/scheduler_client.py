import requests

class SchedulerClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def solve(self, scheduler_input):

        response = requests.post(
            f"{self.base_url}/api/Scheduler/RandomSearchSchedule",
            json=scheduler_input,
            verify=False,
            timeout=1000
        )

        if response.status_code != 200:
            raise RuntimeError(response.text)

        return response.json()