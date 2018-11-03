# This is the main script for chatkit_py.

#This is the starting point of mainly everything, all those scripts are handled from here.

#Let's begin by importing our own stuff.
from . import giphy_py_exceptions as Exceptions
from .giphy_py_classes import *

# Now for other packages
import requests

# Let's set variables
end_point = "https://api.giphy.com/v1/"

# And let's go with the Client class

class Client:
    """The main class for giphy_py. It handles all connections to Giphy."""
    def __init__(self, key):
        self.key = key
        self.end_point = end_point
        self.lang = language.en

    def logout(self):
        del self

    def authenticate(self, key):
        self.key = key
        self.end_point = end_point

    def set_language(self, lang):
        """Changes language on requests. By default, this is en (English). You can anyway set exceptions when doing requests with the lang argument, which is the value set by this function by default."""
        self.lang = lang

    async def search_gifs(self, query:str, limit:int = 25, offset:int = 0, rating: rating = rating.G, lang:language = None):
        lang_to_use = lang or self.lang
        result = requests.get(self.end_point + "gifs/search", params = {
        "api_key" : self.key,
        "q" : query,
        "limit":limit,
        "offset":offset,
        "rating":rating.value,
        "lang":lang_to_use.value})
        return search(result.json(), query)

def get_client(key):
    return Client(key)
