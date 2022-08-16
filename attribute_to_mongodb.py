import pymongo
import pandas as pd

client = pymongo.MongoClient("mongodb+srv://Mishra_31:mishra8871@cluster0.hix22ie.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['ineuron']
collection = database['attribute dataset']

attribute = pd.read_excel('/Users/abhishekmishra/ineuron/live class/data fsds/Attribute DataSet.xlsx')


data=attribute.to_dict('records')
print(data)
collection.insert_many(data)