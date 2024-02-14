
import time
import yaml
import requests
import json


class jobPosting():
    def __init__(self, jobname, user='ANONYMOUS'):
        self.jobname = jobname
        self.user = user

        # Load secrets from YAML file
        with open('secrets.yaml', 'r') as file:
            secrets = yaml.safe_load(file)

        # Access the 'url' value
        self.url = secrets['url']


    def start(self):
        json_data = {'text': f'{self.user} has started job: {self.jobname}'}

        self.start_time = time.time()

        requests.post(self.url, data=json.dumps(json_data))

    def stop(self):
        json_data = {'text': f'{self.user} has finished job: {self.jobname}, clock time taken: {round((time.time()-self.start_time)/3600, 3)} hrs'}

        requests.post(self.url, data=json.dumps(json_data))

    def crash_report(self, error_message):
        json_data = {'text': f'{self.user} has crashed job: {self.jobname}, error message: {error_message}. Clock time taken: {round((time.time()-self.start_time)/3600, 3)} hrs'}

        requests.post(self.url, data=json.dumps(json_data))