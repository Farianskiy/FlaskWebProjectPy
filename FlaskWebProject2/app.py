"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import request
from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"


@app.route('/api', methods = ['POST', 'PUT', 'GET'])
def Post_User():
    if request.method == 'POST':
        f = open('file.txt','a')
        username= request.form['username']
        login = request.form['login']
        password = request.form['password']
        group = request.group['group']
        phone= request.form['phone']
        f.write(username + " " + login + " " + password + " " + group + " "+ phone + "\n")
        f.close()
    if request.method == 'GET':
        f = open('file.txt','r')
        users = f.read();
        f.close();
        return users;
    if request.method == 'PUT':
        f = open('file.txt','r')
        username= request.form['username']
        login = request.form['login']
        password = request.form['password']
        group = request.group['group']
        phone= request.form['phone']


        newusername= request.form['newusername']
        newlogin = request.form['newlogin']
        newpassword = request.form['newpassword']
        newgroup = request.form['newgroup']
        newphone= request.form['newphone']
        s = (username + " " + login + " " + password + " " + group + " "+ phone)
        data = f.read()
        data = data.replace(s, newusername + " " + newlogin + " " + newpassword + " " + newgroup + " "+newphone)
        f.close()
        f = open('file.txt','wt')
        f.write(data)
        f.close
    
        

@app.route('/api/<int:idd>', methods = ['DELETE'])
def Del_User(idd):
    if request.method == 'DELETE':
        f = open('file.txt', 'w')
        f.close()




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3005')
