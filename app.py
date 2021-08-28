from flask import Flask, redirect, url_for, render_template, request
# Initialize the Flask application
app = Flask(__name__)


@app.route('/',methods = ['POST', 'GET']) 
def login():  
   first_name = request.form.get('first_name')
   last_name = request.form.get('last_name')
   return render_template("login.html",Firstname=first_name,Lastname=last_name)
	
if __name__ == '__main__':
   app.run(debug = True)