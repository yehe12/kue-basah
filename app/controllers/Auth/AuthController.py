from app import app
from app.models.user import * ## import kelas User dari model

from flask import Flask, render_template, url_for, redirect, session, request
from flaskext.mysql import MySQL

#fungsi redirect
@app.route('/')
def dashboard():
    if 'loggedin' not in session:

        return redirect(url_for('login'))

    if session['role'] == 1 :
        return redirect(url_for('bossDashboard'))
    
    if session['role'] == 2 :
        return redirect(url_for('adminDashboard'))



#fungsi login
@app.route('/login', methods =['GET', 'POST'])
def login():
    if 'loggedin' in session:

        return redirect(url_for('dashboard'))
    
    old_value = ''
    mesage = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        old_value = username
            
        userAuth = User().selectLogin(username, password) #panggil fungsi login

        if userAuth:
            session['loggedin'] = True
            session['id'] = userAuth[0]
            session['role'] = userAuth[1]
            session['name'] = userAuth[2]
            session['username'] = userAuth[3]
            mesage = 'Logged in successfully!'

            return redirect(url_for('dashboard'))

        else:
            mesage = 'Please enter correct username / password !'
    
    return render_template('auth/login.html', mesage = mesage, old_value=old_value)

#fungsi logout
@app.route('/logout')
def logout():

    User().getLogout() #panggil fungsi logout

    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)