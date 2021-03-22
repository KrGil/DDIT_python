import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.python

sample = db.sample

doc = {'col01': 1, 'col02': 1,'col03':1}

row = db.sample.update_many({"col01" : 2}, {"$set" : {"col02":3, "col03":3,}})
# db.people.updateMany({age:{$gt:25}},{$set:{status:"C"}})

rows = db.sample.find()

for r in rows :
    print(r)