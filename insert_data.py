from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")

mydatabase = client['myproject']
mycollection = mydatabase['student']
rec =[ {
    "name": "siva",
    "add": "ndl",
    "age": "24"

},
    {
        "name": "gan",
        "add": "ndl",
        "age": "24"
    }
]
mycollection.insert_many(rec)
