from flask import Flask # import Flask class
app = Flask(__name__) # Create a Flask instance, the parameter is a must. 

@app.route('/') # use route decorator to tell Flask the url which invokes the following function
def index():
    return 'index1'
    
@app.route('/hello')
def hello():
	return 'hello world'

@app.route('/name/<username>')
def showUserName(username):
	return 'User : ' + username

@app.route('/userid/<int:userid>')
def showUserId(userid):
	return 'userid: ' + str(userid)
	
@app.route('/methods', methods=['GET', 'POST'])
def tellMethods():    
    if request.method == 'GET':
        return 'GET method'
if __name__== '__main__':
    app.run()
