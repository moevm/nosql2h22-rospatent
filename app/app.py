from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mongoengine import MongoEngine, Document
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    "db" : "rospatent"
}

#client = MongoClient('localhost', 27017)
db = MongoEngine(app)
app.config['SECRET_KEY'] = 'dogshit'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Document):
    meta = {'collection' : 'users'}
    username = db.StringField()
    password = db.StringField()

@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

# users collection
User.drop_collection()
User(username="admin", password="123").save()
User(username="chel", password="321").save()

@app.route('/')
def main():
    user_list = []
    for user in User.objects():
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
        
        User(username=username, password=password).save()
        #users.insert_one( { "username": username, "password": password } )
        return redirect('/')

@app.route("/login")
def login():
    if current_user.is_authenticated == True:
        return redirect('/')
    return render_template('login.html')

@app.route("/login", methods=["POST"])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.objects(username=username).first()
    #users.find_one({"username" : username})
    print(user)
    if not user or user['password'] != password:
        flash('Please check your login details and try again.')
        return redirect('/login')
    login_user(user)

    return redirect('/')


@app.route("/logout", methods=["POST", "GET"])
def logout():
    return 'Logout'


if(__name__ == "__main__"):
    app.run()