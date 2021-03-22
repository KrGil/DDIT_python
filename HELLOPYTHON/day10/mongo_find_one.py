import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.python

sample = db.sample

doc = {'col01': 1, 'col02': 1,'col03':1}

rows = db.sample.find({"col01" : 1})

for r in rows :
    print(r)