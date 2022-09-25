from django.shortcuts import render
from django.http import HttpResponse
import pymongo


client = pymongo.MongoClient('mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb')

dbname = client['testdb']
collection = dbname['test']

fruit = {"$set" : {"_id" : 0,"name" : "Apple", "color" : "green"}}
collection.update_one({'_id':0},fruit,upsert=True)

def index(request):
    result = collection.find({})
    for item in result:
        print("name: " + item['name'] + ", color: "+ item['color'])
    return HttpResponse("<h1>Rospatent app</h1>")