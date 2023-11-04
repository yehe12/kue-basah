from app import app
from app.config.db import *
from app.models.user import *

from flask import Flask, render_template, url_for, redirect, session, request
from flaskext.mysql import MySQL

#fungsi melihat user
@app.route('/boss/user')
def bossUser():

    if 'loggedin' in session:
        if session['role'] == 3 :
            
            user = User().selectUser()
            role = User().selectRole()

            return render_template('bos/user.html', users=user, roles=role)

        else :
            return redirect(url_for('dashboard'))

    return redirect(url_for('login'))

@app.route('/boss/user/detail/<int:id>', methods = ['GET'])
def bossUserDetail(id):

    if 'loggedin' in session:
        if session['role'] == 3 :
            
            user_detail = User().selectUserDetail(id)
            role = User().selectRole()

            return render_template('bos/user_detail.html', user_details=user_detail, roles=role)

        else :
            return redirect(url_for('dashboard'))

    return redirect(url_for('login'))
