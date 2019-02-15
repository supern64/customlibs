from requests import Session, exceptions
from copy import copy
import json

base_url = "https://cleverbot.io/1.0"

class CleverbotHTTPException(Exception):
    pass

class Cleverbot:
    def __init__(self, api_user, api_key, nickname=None):
        self._session = Session()
        self._configuration = {
            'user': api_user,
            'key': api_key,
            'nick': nickname
        }
        try:
            data = self._session.post(base_url + "/create", json=self._configuration)
            data.raise_for_status()
        except exceptions.HTTPError as err:
            raise CleverbotHTTPException(data.json()['status'] if data else err)
    def ask(self, query):
        postdata = copy(self._configuration)
        postdata['text'] = query
        try:
            data = self._session.post(base_url + "/ask", json=postdata)
            data.raise_for_status()
        except exceptions.HTTPError as err:
            raise CleverbotHTTPException(data.json()['status'] if data else err)
        else:
            return data.json()['response']
