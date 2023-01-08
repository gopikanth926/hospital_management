from flask import Flask, request
from pymongo import MongoClient


app = Flask(__name__)


@app.route("/data_insertion", methods=['post'])
def add_a():
    input_json = request.get_json()
    client = MongoClient("mongodb://localhost:27017/")
    mydatabase = client['myproject']
    mycollection = mydatabase['stu']
    mycollection.find(input_json)
    print(input_json)
    return "True"


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=9999)


