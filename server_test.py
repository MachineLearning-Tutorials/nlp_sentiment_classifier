#!python

from starlette.responses import HTMLResponse
from starlette.testclient import TestClient
import unittest
# NOTE: Unknown pickling error. Unable to test any prediction functionalities
# import app.server

# TODO tests to write:
# - [ ] response time
# - [ ] assert negative and errors with confidence levels above X
# 

# NOTE: On hold due to machine learning server being down
# TODO Combinations of words that gave false positive predictions
# slickly great but also somewhat bad
# slickly good but also bad
# The movie displayed lot of nudity and had a theme that showed corruption within a city


class App:
    def __init__(self, scope):
        assert scope['type'] == 'http'
        self.scope = scope

    async def __call__(self, receive, send):
        response = HTMLResponse()
        await response(receive, send)

class ServerTest(unittest.TestCase):
    def test_website(self):
        client = TestClient(App)
        response = client.get('https://sentiment-classifier-restart2.onrender.com/')
        assert response.status_code == 200
    
    def test_download_model(self):
        client = TestClient(App)
        response = client.get('https://www.dropbox.com/s/xhnvw0axn6xjbk9/export.pkl?dl=1')
        assert response.status_code == 200



if __name__ == '__main__':
    unittest.main()