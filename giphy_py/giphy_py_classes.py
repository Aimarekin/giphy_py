# Here are all classes that chatkit_py handles.
# (Except the Client, which is in __main__)

import json as json_loader

from enum import Enum

from pprint import pprint

from collections import namedtuple

from . import giphy_py_exceptions

class rating(Enum):
    G = "g"
    PG = "pg"
    PG_13 = "pg-13"
    R = "r"
    NC17 = "nc17"

class language(Enum):
    en = "en"
    es = "es"
    pt = "pt"
    id = "id"
    fr = "fr"
    ar = "ar"
    tr = "tr"
    th = "th"
    vi = "vi"
    de = "de"
    it = "it"
    ja = "ja"
    zh_CN = "zh-cn"
    zh_TW = "zh-tw"
    ru = "ru"
    ko = "ko"
    pl = "pl"
    nl = "nl"
    ro = "ro"
    hu = "hu"
    sv = "sv"
    hi = "hi"
    bn = "bn"
    da = "da"
    fa = "fa"
    tl = "tl"
    fi = "fi"
    iw = "iw"
    ms = "ms"
    no = "no"
    uk = "uk"

class meta:
    def __init__(self, json:dict):
        self.msg = json["msg"]
        self.code = json["status"]
        self.id = json["response_id"]

    def __unicode__(self):
        return f"meta: {self.msg} - {self.code}, id {self.id}"

    def __str__(self):
        return self.__unicode__()

class pagination:
    def __init__(self, json:dict):
        self.offset = json["offset"]
        self.total_count = json["total_count"]
        self.result_count = json["count"]

    def __unicode__(self):
        return f"pagination: {self.total_count} results, {self.result_count} returned with an offset of {self.offset}"

    def __str__(self):
        return self.__unicode__()

class user:
    def __init__(self, json:dict):
        pass

class image:
    def __init__(self, type, json:dict):
        self.type = type
        for key, value in json.items():
            setattr(self, key, value)

    def __unicode__(self):
        return f"image {self.type}: {self.url}"

    def __str__(self):
        return self.__unicode__()

class images:
    def __init__(self, json:dict):
        for key, value in json.items():
            setattr(self, key, image(key, json[key]))

    def __unicode__(self):
        return f"images: {self.images.original.url}"

    def __str__(self):
        return self.__unicode__()

class gif:
    def __init__(self, json:dict):
        self.type = json["type"]
        self.id = json["id"]
        self.slug = json["slug"]
        self.url = json["url"]
        self.bitly_url = json["bitly_url"]
        self.embed_url = json["embed_url"]

        if "username" in json:
            self.username = json["username"]
        else:
            self.username = None

        if "source" in json:
            self.source = json["source"]
        else:
            self.source = None

        self.rating = rating(json["rating"])

        if "user" in json:
            self.user = user(json["user"])
        else:
            self.user = None

        if "source_tld" in json:
            self.source_tld = json["source_tld"]
        else:
            self.source_tld = None

        if "source_post_url" in json:
            self.source_post_url = json["source_post_url"]
        else:
            source_post_url = None

        if "update_datetime" in json:
            self.update_datetime = json["update_datetime"]
        else:
            self.update_datetime = None

        if "create_datetime" in json:
            self.create_datetime = json["create_datetime"]
        else:
            self.create_datetime = None

        self.import_datetime = json["import_datetime"]

        if "trending_datetime" in json:
            self.trending_datetime = json["trending_datetime"]
        else:
            self.trending_datetime = None
        if "480w_still" in json:
            json["images"]["w480_still"] = json["images"].pop("480w_still")
        self.images = images(json["images"])
        self.image_url = self.images.original.url
        self.title = json["title"]

    def __unicode__(self):
        return f"gif ({self.type}): {self.title} - {self.images.original.url}"

    def __str__(self):
        return self.__unicode__()

class search:
    def __init__(self, json:dict, query):
        self.meta = meta(json["meta"])
        self.pagination = pagination(json["pagination"])
        self.query = query
        self.results = []
        if len(json["data"]) == 0:
            raise giphy_py_exceptions.noResults(query, self.pagination.offset)
        for timeslooped, item in enumerate(json["data"]):
            self.results.append(gif(item))

    def __unicode__(self):
        return f"Search: {self.query} - {self.pagination.total_count} results, {self.pagination.result_count} returned with an offset of {self.pagination.offset}"

    def __str__(self):
        return self.__unicode__()
