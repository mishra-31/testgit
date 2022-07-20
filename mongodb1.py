import pymongo

client = pymongo.MongoClient("mongodb+srv://Mishra-31:Mishra8871@cluster0.a8wljwf.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d= {
    'name':'xyz',
    'email':'xyz@gmail.com',
    'last name':'efg'
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)