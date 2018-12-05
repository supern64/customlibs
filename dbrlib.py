r"""DBRLib
An example library of DBR's API
Requires "requests" module
Put this file in the "Lib" folder if you want to be able to use this library anywhere in Python.
"""

import requests
from base64 import b64encode
base_url = "https://discordbotsreview.tk/api/"

class DBRBot(object):
    """Object for bots in Discord Bot Reviews"""
    def __init__(self, client_id, prefix, invite_url, support_url, short_description, long_description, owner, likes, dislikes, unique, very_unique):
        self.__client_id = client_id
        self.__prefix = prefix
        self.__invite_url = invite_url
        self.__support_url = support_url
        self.__short_description = short_description
        self.__long_description = long_description
        widget = requests.get(base_url + "widget/" + self.__client_id + ".png")
        self.__widget = DBRWidget(widget.content)
        if owner != None:
            self.__owner = DBRUser(owner['id'], owner['bio'], owner['certified'])
        else:
            self.__owner = None
        self.__likes = likes
        self.__dislikes = dislikes
        self.__unique = unique
        self.__very_unique = very_unique
    @property
    def client_id(self):
        """The bot's Client ID."""
        return self.__client_id
    @property
    def prefix(self): 
        """The bot's prefix."""
        return self.__prefix
    @property
    def invite_url(self):
        """The bot's invite URL."""
        return self.__invite_url
    @property
    def support_url(self):
        """The bot's support server invite. None if not found."""
        if self.__support_url == "":
            return None
        else:
            return "https://discord.gg/" + self.__support_url
    @property
    def short_description(self):
        """The bot's short description"""
        return self.__short_description
    @property
    def long_description(self):
        """The bot's long description. May contain Markdown."""
        return self.__long_description
    @property
    def owner(self):
        """The bot submitter's user object"""
        return self.__owner
    @property
    def likes(self): 
        """The amount of likes the bot has received."""
        return self.__likes
    @property
    def dislikes(self): 
        """The amount of dislikes the bot has received."""
        return self.__dislikes
    @property
    def is_unique(self): 
        """Returns true if bot is classified as "unique"."""
        return self.__unique
    @property
    def is_very_unique(self): 
        """Returns true if bot is classified as "very unique"."""
        return self.__very_unique
    @property
    def widget(self): 
        """Returns the bot's widget object"""
        return self.__widget
    def __str__(self):
        return self.__client_id
class DBRUser(object):
    """Object for users in Discord Bot Reviews"""
    def __init__(self, id, biography, certified, bots=None):
        self.__id = id
        self.__biography = biography
        self.__certified = certified
        self.__bots = bots
    @property
    def id(self): 
        """Returns the user's ID"""
        return self.__id
    @property
    def biography(self): 
        """Returns the user's biography."""
        return self.__biography
    @property
    def is_certified(self): 
        """Returns True if the user is certified."""
        return self.__certified
    @property
    def bots(self): 
        """Returns the user's bots."""
        return self.__bots
class DBRWidget:
    """Class for widgets"""
    def __init__(self, content):
        self.__widget_c = content
    def save(self, location):
        """Saves the widget file to a location."""
        open(location, "wb+").write(self.__widget_c)
    def get_base64(self):
        """Gets a base64 formatted text for the widget"""
        return b64encode(self.__widget_c)
    @property
    def content(self):
        """The widget's raw content."""
        return self.__widget_c
def getbot(id):
    """Gets a bot. Returns a bot object."""
    id = str(id)
    r = requests.get(base_url + "bot/" + id)
    json = r.json()
    return DBRBot(json['clientID'], json['prefix'], json['invite_url'], json['support_url'], json['short_description'], json['long_description'], json['owner'], json['likes'], json['dislikes'], json['unique'], json['veryUnique'])
def getuser(id):
    """Gets a user. Returns a user object."""
    id = str(id)
    r = requests.get(base_url + "user/" + id)
    json = r.json()
    e = []
    for i in json['bots']:
        e.append(DBRBot(i['clientID'], i['prefix'], i['invite_url'], i['support_url'], i['short_description'], i['long_description'], None, i['likes'], i['dislikes'], i['unique'], i['veryUnique']))
    return DBRUser(json['id'], json['bio'], json['certified'], e)
