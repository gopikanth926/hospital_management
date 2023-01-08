
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")

mydatabase = client['myproject']
mycollection = mydatabase['student']

for data in mycollection.find({"name":"chandra"}):
    print(data)