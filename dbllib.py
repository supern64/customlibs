r"""DBLLib: The library for connecting with discordbots.org (100% for fun, not recommended for actual use)
Requires:
requests_html
google/python-fire
Features:
Uses HTML scraping for looking up things without the help of the API
Object-based
Note: This library is still in beta and this library cannot get all things.
"""
import fire
from requests.exceptions import HTTPError 
try:
    from requests_html import HTMLSession
except ImportError:
    from requests_html import Session as HTMLSession # Fallback
    
session = HTMLSession()

__version__ = "1.0b"
__author__ = "SuperNiintendo#3700 2018"

class DBLBot(object):
    """A class for all DBL Bots
    All attributes are read-only.
    """
    def __init__(self, botid):
        botid = str(botid)
        self.__url = 'https://discordbots.org/bot/' + botid
        self.__id = botid
        r = session.get(self.__url)
        r.raise_for_status()
        d = r.html.find('#details', first=True)
        self.__description = d.find(".bot-description", first=True).text # Description
        self.__name = d.find(".bot-name", first=True).text # Name
        self.__prefix = r.html.find("#prefix", first=True).text # Prefix
        self.__library = d.find("#libclick", first=True).text # Library
        self.__owners = r.html.find(".owners", first=True).text.split()[2:] # Owners
        self.__long_description = r.html.find(".longdescription", first=True).text # Long description (WILL NOT WORK CORRECTLY WITH STYLED PAGES!!!)
        self.__tags = r.html.find("#tags", first=True).text.split() # Tags (might not work perfectly)
        self.__upvotes = int(d.find("#points", first=True).text.replace(",", "")) # Upvotes
        self.__vote_url = self.__url + '/vote'
        self.__invite_url = d.find('[target="_blank"]', first=True).attrs['href']
        self.__report_url = self.__url + "/report"
        u = d.find(".bot-img", first=True)
        self.__avatar_url = u.find("img", first=True).attrs['src']
        try:
            self.__support_url = r.html.find('#support', first=True).attrs['href']
        except (KeyError, AttributeError):
            self.__support_url = None
        try:
            self.__github_repo = r.html.find('#github', first=True).attrs['href']
        except (KeyError, AttributeError):
            self.__github_repo = None
        g = r.html.find(".serversshards", first=True)
        try:
            self.__servers = int(g.text.split()[0].replace(",", ""))
        except (IndexError, AttributeError):
            self.__servers = None
        try:
            self.__shards = int(g.text.split()[2].replace(",", "")) # Bug probably only with 3.4
        except (IndexError, AttributeError):
            self.__shards = None
    @property
    def description(self):
        """The bot's description [str]"""
        return self.__description
    @property
    def name(self):
        """The bot's name [str]"""
        return self.__name
    @property
    def prefix(self):
        """The bot's prefix [str]"""
        return self.__prefix
    @property
    def library(self):
        """The bot's library [str]"""
        return self.__library
    @property
    def owners(self):
        """The bot's owners [list]"""
        return self.__owners
    @property
    def url(self):
        """The bot's URL [str]"""
        return self.__url
    @property
    def id(self):
        """The bot's ID [str]"""
        return self.__id
    @property
    def long_description(self):
        """The bot's long description [str]"""
        return self.__long_description
    @property
    def tags(self):
        """The bot's tags [list]"""
        return self.__tags
    @property
    def upvotes(self):
        """The bot's upvotes [int]"""
        return self.__upvotes
    @property
    def vote_url(self):
        """The bot's vote URL [str]"""
        return self.__vote_url
    @property
    def invite_url(self):
        """The bot's invite URL [str]"""
        return self.__invite_url
    @property
    def report_url(self):
        """The bot's report URL [str]"""
        return self.__report_url
    @property
    def support_url(self):
        """The bot's support server URL [str|None]"""
        return self.__support_url
    @property
    def servers(self):
        """The bot's amount of servers [int]"""
        return self.__servers
    @property
    def shards(self):
        """The bot's amount of shards [int]"""
        return self.__shards
    @property
    def avatar_url(self):
        """The bot's avatar URL. [str]"""
        return self.__avatar_url
    @property
    def github_repo(self):
        """The bot's github repository [str|None]"""
        return self.__github_repo
    def __str__(self):
        """String method."""
        return self.__name
    def refetch(self):
        """Refetches the information from DBL."""
        r = session.get(self.__url)
        r.raise_for_status()
        d = r.html.find('#details', first=True)
        self.__description = d.find(".bot-description", first=True).text # Description
        self.__name = d.find(".bot-name", first=True).text # Name
        self.__prefix = r.html.find("#prefix", first=True).text # Prefix
        self.__library = d.find("#libclick", first=True).text # Library
        self.__owners = r.html.find(".owners", first=True).text.split()[2:] # Owners
        self.__long_description = r.html.find(".longdescription", first=True).text # Long description (WILL NOT WORK CORRECTLY WITH STYLED PAGES!!!)
        self.__tags = r.html.find("#tags", first=True).text.split() # Tags (might not work perfectly)
        self.__upvotes = int(d.find("#points", first=True).text.replace(",", "")) # Upvotes
        self.__vote_url = self.__url + '/vote'
        self.__invite_url = d.find('[target="_blank"]', first=True).attrs['href']
        self.__report_url = self.__url + "/report"
        u = d.find(".bot-img", first=True)
        self.__avatar_url = u.find("img", first=True).attrs['src']
        try:
            self.__support_url = r.html.find('#support', first=True).attrs['href']
        except (KeyError, AttributeError):
            self.__support_url = None
        try:
            self.__github_repo = r.html.find('#github', first=True).attrs['href']
        except (KeyError, AttributeError):
            self.__github_repo = None
        g = r.html.find(".serversshards", first=True)
        try:
            self.__servers = int(g.text.split()[0].replace(",", ""))
        except (IndexError, AttributeError):
            self.__servers = None
        try:
            self.__shards = int(g.text.split()[2].replace(",", "")) # Bug probably only with 3.4
        except (IndexError, AttributeError):
            self.__shards = None
def fetchbot(id):
    return DBLBot(id)

# Command line tools
class CmdTools:
    def getbot(self, id):
        m = fetchbot(id)
        fmt = "Name: {0.name}\nLibrary: {0.library}\nOwners: {1}\nPrefix: {0.prefix}\nServers: {0.servers}\nShards: {0.shards}\nUpvotes: {0.upvotes}\nDescription: {0.description}\nTags: {2}\nGithub repository: {0.github_repo}\nSupport server URL: {0.support_url}".format(m, ", ".join(m.owners), ", ".join(m.tags))
        return fmt

if __name__ == "__main__":
    fire.Fire(CmdTools)
