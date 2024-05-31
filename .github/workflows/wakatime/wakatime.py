from os import environ
import requests
import base64

class wakatime:
    def __init__(self):
        self.WAKATIME_API_KEY = environ['WAKATIME_API_KEY']
        self.BASE_URL = 'https://wakatime.com/api/v1/'

    def make_requests(self, method, api):
        url = self.BASE_URL + api
        key = base64.b64encode(bytes(self.WAKATIME_API_KEY, 'utf-8')).decode('utf-8')
        headers = {
            'Authorization': f'Basic {key}'
        }

        if method == 'GET':
            resp = requests.get(url, headers=headers, timeout=10)
        else:
            resp = requests.post(url, headers=headers, timeout=10)

        return resp.json()['data']

    def get_user(self):
        api = '/users/current'
        method = 'GET'
        users = self.make_requests(method, api)
        return users['id']

    def get_stats(self):
        user = self.get_user()
        api = f'/users/{user}/stats/all_time'
        method = 'GET'
        stats = self.make_requests(method, api)
        return stats

