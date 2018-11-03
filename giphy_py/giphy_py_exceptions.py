# This contains possible Exceptions raised by giphy_py

class noResults(Exception):
    """Exception raised when a search has no results"""
    def __init__(self, query, offset):
        self.query = query
        self.offset = offset

    def __unicode__(self):
        return f"The Giphy search by {self.query} with an offset of {self.offset} returned no results."
