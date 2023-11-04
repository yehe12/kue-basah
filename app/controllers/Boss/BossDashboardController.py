from app import app
from flask import session, render_template, redirect, url_for

from app.models.user import *

@app.route('/boss/dashboard')
def bossDashboard():
    if 'loggedin' in session:
        if session['role'] == 1 :

            count_users = User().countUser()

            return render_template('boss/boss_dashboard.html', count_user=data_user, count_cost_total=data_cost_total)

        else :

            return redirect(url_for('adminDashboard'))

    return redirect(url_for('login'))
