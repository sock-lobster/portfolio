from flask import render_template, flash, url_for, redirect
from app import app
from app.forms import ContactForm

@app.route('/')
@app.route('/index')
def index():
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
    return render_template('index.html', title='Home', user=user, posts=posts, contactForm=ContactForm())

@app.route('/resume')
def resume():
    return render_template('resume.html', contactForm=ContactForm())

@app.route('/skills')
def skills():
    return render_template('skills.html', contactForm=ContactForm())

@app.route('/projects')
def projects():
    return render_template('projects.html', contactForm=ContactForm())
