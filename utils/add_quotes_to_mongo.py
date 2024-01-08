import json
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.hw8

with open("quotes.json", "r", encoding="utf-8") as fd:
    quotes = json.load(fd)


for quote in quotes:
    quote["author"] = db.authors.find_one({"fullname": quote["author"]})
    if quote["author"]:
        db.quotes.insert_one({
            "quote": quote["quote"],
            "tags": quote["tags"],
            "author": ObjectId(quote["author"]["_id"])
        })
