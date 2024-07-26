
import requests


class Query:
    def __init__(self, url):
        self.url = url

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def send_query(self):  # makes GET query to specified url and returns servers respond
        try:
            response = requests.get(self.get_url())

            if response.status_code == 200:
                posts = response.json()
                return posts
            else:
                print('Error: ', response.status_code)
                return None
        except:
            raise ConnectionError

