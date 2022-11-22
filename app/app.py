from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.rospatent


# users collection
users = db.users
users.drop()
users.insert_one({"username" : "admin", "password" : "123"})
users.insert_one({"username" : "chel", "password" : "321"})


@app.route('/')
def main():
    user_list = []

    for user in users.find():
        user_list.append({"username": user["username"], "password": user["password"]})
    #return render_template("carslist.html", cars = cars)
    return render_template('index.html', items = user_list)

@app.route("/adduser", methods = ['GET','POST'])
def adduser():
    if request.method == 'GET':
        return render_template("adduser.html")
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        
        users.insert_one( { "username": username, "password": password } )
        return redirect('/')

if(__name__ == "__main__"):
    client.run()