from flask import Flask, render_template
from pprint import pprint
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.rospatent
# users collection
users = db.users
users.drop()
users.insert_one({"username" : "admin", "password" : "123"})
for document in users.find(): 
    pprint(document)



@app.route('/')
def hello():
    return render_template('index.html')