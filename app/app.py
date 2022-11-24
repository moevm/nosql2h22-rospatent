from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mongoengine import MongoEngine, Document
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import datetime
from decimal import Decimal
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    "db" : "rospatent"
}

db = MongoEngine(app)
app.config['SECRET_KEY'] = 'Trudy'


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


fields = ['registration number','registration date',
          'application number','application date','authors',
          'authors count' ,'right holders','contact to third parties',
          'program name','creation year','registration publish date',
          'registration publish number','actual','publication URL']

class Patent(UserMixin, db.Document):
    meta = {'collection' : 'patents'}
    registration_number = db.DecimalField()
    registration_date = db.ComplexDateTimeField()
    application_number = db.DecimalField()
    application_date = db.ComplexDateTimeField()
    authors = db.StringField()
    authors_count = db.DecimalField()
    right_holders = db.StringField()
    contact_to_third_parties = db.StringField()
    program_name = db.StringField()
    creation_year = db.DecimalField()
    registration_publish_date = db.ComplexDateTimeField()
    registration_publish_number = db.DecimalField()
    actual = db.BooleanField()
    publication_URL = db.StringField()

    def to_dict(self):
        d = {}
        for field in fields:
            field_name = field.replace(" ", "_")
            d[field_name] = str(self[field_name])
        return d

# users collection
Patent.drop_collection()
Patent(registration_number=123).save()
Patent(registration_number=321).save()

@app.route('/')
def main():
    return render_template('index.html', fields = fields)

@app.route('/api/data')
def data():
    query = Patent.objects()

    # response
    return {
        'data': [item.to_dict() for item in query],
        'recordsTotal': len(query),
        'recordsFiltered': len(query),
        'draw': request.args.get('draw', type=int),
    }

@app.route("/adduser", methods = ['GET','POST'])
def adduser():
    if request.method == 'GET':
        return render_template("adduser.html", fields = fields)
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        
        User(username=username, password=password).save()
        return redirect('/')

@app.route("/addpatent", methods = ['GET','POST'])
def addpatent():
    if request.method == 'GET':
        return render_template("addpatent.html", fields = fields)
    if request.method == 'POST':
        # args = {}
        # for field in fields:
        #     args[field.replace(' ', '_')] = request.form[field.replace(' ', '_')]
        
        # Patent(registration_number = Decimal(args['registration_number']),
        #     registration_date = datetime.datetime(args['registration_date']),
        #     application_number = Decimal(args['application_number']),
        #     application_date = args['application_date'],
        #     authors = args['application_date'],
        #     authors_count = Decimal(args['authors_count']),
        #     right_holders = args['right_holders'],
        #     contact_to_third_parties = args['contact_to_third_parties'],
        #     program_name = args['program_name'],
        #     creation_year = Decimal(args['creation_year']),
        #     registration_publish_date = args['registration_publish_date'],
        #     registration_publish_number = Decimal(args['registration_publish_number']),
        #     actual = args['actual'],
        #     publication_URL = args['publication_URL']).save()
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
    if not user:
        flash('Такого пользователя не существует!')
        return redirect('/login')
    if user['password'] != password:
        flash('Неправильный пароль!')
        return redirect('/login')
    login_user(user)

    return redirect('/')

@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect('/')


if(__name__ == "__main__"):
    app.run()