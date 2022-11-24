from wtforms import DecimalField, StringField, BooleanField, DateField, SubmitField
from flask import Flask, render_template, request, redirect, flash
from flask_mongoengine import MongoEngine, Document
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    "db": "rospatent"
}

db = MongoEngine(app)
app.config['SECRET_KEY'] = 'Trudy'


# Authorization

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Document):
    meta = {'collection': 'users'}
    username = db.StringField()
    password = db.StringField()


@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()


# users collection
User.drop_collection()
User(username="admin", password="123").save()
User(username="chel", password="321").save()


# Patents db

fields = ['registration number', 'registration date',
          'application number', 'application date', 'authors',
          'authors count', 'right holders', 'contact to third parties',
          'program name', 'creation year', 'registration publish date',
          'registration publish number', 'actual', 'publication URL']
fields_name = [field.replace(" ", "_") for field in fields]


class Patent(UserMixin, db.Document):
    meta = {'collection': 'patents'}
    registration_number = db.StringField()
    registration_date = db.DateField()
    application_number = db.StringField()
    application_date = db.DateField()
    authors = db.StringField()
    authors_count = db.DecimalField(precision=0)
    right_holders = db.StringField()
    contact_to_third_parties = db.StringField()
    program_name = db.StringField()
    creation_year = db.DecimalField(precision=0)
    registration_publish_date = db.DateField()
    registration_publish_number = db.DecimalField(precision=0)
    actual = db.BooleanField()
    publication_URL = db.StringField()

    def to_dict(self):
        d = {}
        for field in fields:
            field_name = field.replace(" ", "_")
            d[field_name] = str(self[field_name])
        return d


# patents collection
Patent.drop_collection()
Patent(registration_number="950396", registration_date="1995-11-09",application_number="0000950377",application_date="1995-10-19",
       authors="Тюхов Борис Петрович (RU) Ильиченкова Зоя Викторовна  (RU) Федосеева Татьяна Леонидовна (RU)",
       authors_count=3, right_holders="Тюхов Борис Петрович (RU)", contact_to_third_parties="",program_name="",creation_year=None,
       registration_publish_date="1996-03-20", registration_publish_number=1,actual=True,publication_URL="http://www1.fips.ru/fips_servl/fips_servlet?DB=EVM&DocNumber=950396").save()

Patent(registration_number="970019", registration_date="1997-01-17",application_number="0000960509",application_date="1996-12-20",
       authors="Колдина А.И. (RU) Макаров С.В. (RU) Александрова Г.М. (RU) Иванов В.Г. (RU) Высоцкая Н.В. (RU) Лебедев С.Н. (RU)",
       authors_count=6, right_holders="Чарский Виталий Владимирович (RU) Иванов Владимир Георгиевич (RU)", contact_to_third_parties="",program_name="Комплексная система информационного обеспечения учета и движения кадров",creation_year=None,
       registration_publish_date="1997-06-20", registration_publish_number=2,actual=True,publication_URL="http://www1.fips.ru/fips_servl/fips_servlet?DB=EVM&DocNumber=970019").save()

Patent(registration_number="950396", registration_date="1995-11-09",application_number="19951019",
       authors="Тюхов Борис Петрович (RU) Ильиченкова Зоя Викторовна  (RU) Федосеева Татьяна Леонидовна (RU)",
       authors_count=3, right_holders="Тюхов Борис Петрович (RU)", contact_to_third_parties="",program_name="",creation_year=None,
       registration_publish_date="1996-03-20", registration_publish_number=1,actual=True,publication_URL="http://www1.fips.ru/fips_servl/fips_servlet?DB=EVM&DocNumber=950396").save()

Patent(registration_number="970019", registration_date="1997-01-17",application_number="0000960509",application_date="1996-12-20",
       authors="Колдина А.И. (RU) Макаров С.В. (RU) Александрова Г.М. (RU) Иванов В.Г. (RU) Высоцкая Н.В. (RU) Лебедев С.Н. (RU)",
       authors_count=6, right_holders="Чарский Виталий Владимирович (RU) Иванов Владимир Георгиевич (RU)", contact_to_third_parties="",program_name="Комплексная система информационного обеспечения учета и движения кадров",creation_year=None,
       registration_publish_date="1997-06-20", registration_publish_number=2,actual=True,publication_URL="http://www1.fips.ru/fips_servl/fips_servlet?DB=EVM&DocNumber=970019").save()


class AddPatentForm(FlaskForm):
    registration_number = StringField()
    registration_date = DateField()
    application_number = StringField()
    application_date = DateField()
    authors = StringField()
    authors_count = DecimalField()
    right_holders = StringField()
    contact_to_third_parties = StringField()
    program_name = StringField()
    creation_year = DecimalField()
    registration_publish_date = DateField()
    registration_publish_number = DecimalField()
    actual = BooleanField()
    publication_URL = StringField()
    submit = SubmitField("Add")

# Routes


@app.route('/')
def main():
    return render_template('index.html', fields=fields)


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


@app.route("/adduser", methods=['GET', 'POST'])
def adduser():
    if request.method == 'GET':
        return render_template("adduser.html", fields=fields)
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        User(username=username, password=password).save()
        return redirect('/')


@app.route("/addpatent", methods=['GET', 'POST'])
@login_required
def addpatent():
    if request.method == 'GET':
        form = AddPatentForm()
        return render_template("addpatent.html", form=form)
    if request.method == 'POST':
        # args = {}
        # for field in fields:
        #     args[field.replace(' ', '_')] = request.form[field.replace(' ', '_')]
        form = AddPatentForm()
        Patent(registration_number=form.registration_number.data,
               registration_date=form.registration_date.data,
               application_number=form.application_number.data,
               application_date=form.application_date.data,
               authors=form.authors.data,
               authors_count=form.authors_count.data,
               right_holders=form.right_holders.data,
               contact_to_third_parties=form.contact_to_third_parties.data,
               program_name=form.program_name.data,
               creation_year=form.creation_year.data,
               registration_publish_date=form.registration_publish_date.data,
               registration_publish_number=form.registration_publish_number.data,
               actual=form.actual.data,
               publication_URL=form.publication_URL.data).save()
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


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


if(__name__ == "__main__"):
    app.run(host='0.0.0.0', port=5001)
