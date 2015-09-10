__author__ = 'FSG'
from flask import Flask
from flask import request
from flask import make_response
from flask import redirect

app = Flask(__name__)

@app.route('/')
def helloworld():
    return '<h1>Hello World!</h1>'

@app.route('/usr/<name>')
def user(name):
    return '<h1>Hello, %s</h1>' %name

@app.route('/requestinfo/')
def requestinfo():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/response/')
def responseinfo():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', 12)
    return response

@app.route('/redirect/')
def myredirect():
    return redirect('http://www.baidu.com')

if __name__ == '__main__':
    app.run(debug=True)