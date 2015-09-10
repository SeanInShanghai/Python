from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Migual'}
    posts = [
        {
            'author':{'nickname':'John'},
            'body': 'Nice day!'
        },
        {
            'author':{'nickname':'Susan'},
            'body':'The movice is cool'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)