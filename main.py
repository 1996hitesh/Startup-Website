from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail

with open("config.json",'r') as c:
    params = json.load(c)['params']

local_server = True

app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-password']
    )
mail = Mail(app)
if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_url']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_url']

db = SQLAlchemy(app)


class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.String(15), nullable=True)
    msg = db.Column(db.String(300), nullable=False)
    date = db.Column(db.String(120), nullable=True)


class Courses(db.Model):
    sno = db.Column(db.Integer, primary_key=True)    
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    subtitle = db.Column(db.String(500), nullable=False)
    icon = db.Column(db.String(50), nullable=False)
    background = db.Column(db.String(50), nullable=False)
    about = db.Column(db.String(500), nullable=False)
    objectives = db.Column(db.String(500), nullable=False)
    audience = db.Column(db.String(500), nullable=False)    
    prerequisites = db.Column(db.String(500), nullable=False)
    slug = db.Column(db.String(30), nullable=False)

#Home Page
@app.route("/")
def index():
    return render_template("index.html", params=params)



#Admin Panel
@app.route("/dashboard", methods=['GET','POST'])
def dashboard():
    if 'user' in session and session['user'] == params['admin-user']:
        return render_template('admin dashboard.html')

    if request.method == 'POST':
        #Redirect to admin Dashboard
        username = request.form.get("uname")
        userpass = request.form.get("pass")
        if username == params['admin-user'] and userpass == params['admin-password']:
            session['user'] = username
            return render_template('admin dashboard.html')

    else:
        return render_template('dashboard.html')


@app.route("/post_course", methods=['GET','POST'])
def post_course():
    if 'user' in session and session['user'] == params['admin-user']:
        if request.method == 'POST':
            course_title = request.form.get('title')
            course_slug = request.form.get('slug')
            course_content = request.form.get('content')
            course_icon = request.form.get('icon')
            course_background = request.form.get('background')
            course_subtitle = request.form.get('subtitle')
            course_about = request.form.get('about')
            course_objectives = request.form.get('objectives')
            course_audience = request.form.get('audience')
            course_prereq = request.form.get('prereq')
            entry = Courses(title=course_title, slug=course_slug, content=course_content, 
                            icon=course_icon, subtitle=course_subtitle, background=course_background, 
                            about=course_about, objectives=course_objectives, audience=course_audience,
                            prerequisites=course_prereq )
            db.session.add(entry)
            db.session.commit()
    
    return render_template('admin dashboard.html')


@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')


#About section
@app.route("/about")
def about():
    return render_template('about.html')


# All Services
@app.route("/devops_service")
def devops_service():
    return render_template('DevOps_service.html')


@app.route("/infra_service")
def infra_service():
    return render_template('infra_service.html')


@app.route("/development_service")
def development_service():
    return render_template('development_service.html')


# Main Training page

@app.route("/training")
def training():
    return render_template('training.html')


# Sub Training pages
@app.route("/ai_training")
def ai_training():
    return render_template('AI training.html')


@app.route("/iot_training")
def iot_training():
    return render_template('IOT training.html')


@app.route("/azure_training")
def azure_training():
    return render_template('Azure training.html')


@app.route("/devops_training")
def devops_training():
    return render_template('DevOps training.html')


@app.route("/cloud_training")
def cloud_training():
    return render_template('Cloud training.html')


@app.route("/bigdata_training")
def bigdata_training():
    return render_template('BigData training.html')


# Training details page

@app.route("/courses/<string:courses_slug>", methods=['GET'])
def courses_route(courses_slug):
    course = Courses.query.filter_by(slug="first-course").first()
    #print(type(course.content))
    return render_template('details.html', course=course, content = course.content)


@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/blog_details")
def blog_details():
    return render_template('blog-details.html')



@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        '''Add entry to the database'''
        name = request.form.get('name')
        message = request.form.get('message')
        email = request.form.get('email')
        phn = request.form.get('phn')
        entry = Contact(name=name, phone_num=phn, email=email, msg=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message("New message from " + name,
                            sender = email,
                            recipients = [params['gmail-user']],
                            body = message + "\n" + phn 
                        )
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
