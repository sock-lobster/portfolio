from flask import render_template, flash, url_for, redirect
from flask_mail import Message
from app import app, mail
from app.forms import ContactForm

def send_contact_message(email, name, note):
    sender = app.config['ADMINS'][0]
    recipient = app.config['ADMINS'][1]
    msg = Message('Contact form message', sender=sender, recipients=[recipient], reply_to=email)
    msg.body = note
    mail.send(msg)

def contact_submit(form, page):
    if form.validate_on_submit():
        flash('{}, your message has been sent.'.format(form.name.data))
        send_contact_message(form.email.data, form.name.data, form.message.data)
        return redirect(page)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    print("here or ther ")
    user = {'username': 'Dan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    form = ContactForm()
    contact_submit(form, '/index')
    return render_template('index.html', title='Home', user=user, posts=posts, contactForm=form)

@app.route('/resume', methods=['GET', 'POST'])
def resume():
    print("in resume")
    form = ContactForm()
    contact_submit(form, '/resume')
    return render_template('resume.html', contactForm=ContactForm())

@app.route('/skills', methods=['GET', 'POST'])
def skills():
    return render_template('skills.html', contactForm=ContactForm())

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    return render_template('projects.html', contactForm=ContactForm())
