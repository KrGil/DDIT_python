import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.python

users = db.sample

doc = [
        {'col01': 1, 'col02': 1,'col03':1},
        {'col01': 2, 'col02': 2,'col03':2},
        {'col01': 3, 'col02': 3,'col03':3},
    ]

cnt = users.insert_many(doc)
print("cnt : ",     cnt)