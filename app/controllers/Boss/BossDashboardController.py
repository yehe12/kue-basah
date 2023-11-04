from app import app
from flask import session, render_template, redirect, url_for

from app.models.user import *

@app.route('/boss/dashboard')
def bossDashboard():
    if 'loggedin' in session:
        if session['role'] == 1 :

            return render_template('boss/boss_dashboard.html')

        else :

            return redirect(url_for('adminDashboard'))

    return redirect(url_for('login'))
