import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.python

users = db.sample

doc = {'col01': 1, 'col02': 1,'col03':1}

users.insert_one(doc)