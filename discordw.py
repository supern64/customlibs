# DiscordWebhook

import json
import requests
  
class WebhookClient(object):
    """
    A class for interacting with webhooks [sending messages and deleting the webhook].
    """
    def __init__(self, username, webhook_url, avatar_url):
        if len(username) < 2 or len(username) > 32:
            raise ValueError('Username must be a string and has a length between 2 and 32.')
        if not requests.get(webhook_url).ok:
            raise WebhookInvalid("Not a valid Discord webhook.")
        self.username = username
        self.webhook_url = webhook_url
        self.avatar_url = avatar_url
    def send(self, message, tts=False):
        """
        Sends a message through a WebhookClient with the specified URL.
        """
        payload = {
            "avatar_url": str(self.avatar_url),
            "username": str(self.username),
            "content": message,
            "tts": tts
        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(self.webhook_url, data=json.dumps(payload), headers=headers)
        if not response.ok:
            raise requests.HTTPError("An error was returned from the server.")
    def delete(self):
        """
        Deletes the Webhook in WebhookClient.wurl.
        """
        response = requests.delete(self.webhook_url)
        if not response.ok:
            raise requests.HTTPError("An error was returned from the server.")
        return 'Webhook deleted.'
    def save(self, filename):
        """
        Saves the current WebhookClient to a .json file.
        """
        json.dump(self.__dict__, open(filename, 'x'))
class WebhookInvalid(Exception):
    """
    A Exception for Invalid Webhook passed into WebhookClient.
    """
    pass


def clifromjson(configjson):
    """
    A function for creating a WebhookClient object from a config json file. Useful if you're making a Webhook app that needs a config.
    """
    config = json.load(open(configjson))
    return WebhookClient(
        config['username'],
        config['webhook_url'],
        config['avatar_url'])

def jsonfromcli(cli, filename):
    """
    A fucntion for creating a json config file from a WebhookClient object.
    """
    if type(cli) != WebhookClient:
        raise TypeError('cli must be a WebhookClient object.')
    json.dump(cli.__dict__, open(filename, 'x'))
