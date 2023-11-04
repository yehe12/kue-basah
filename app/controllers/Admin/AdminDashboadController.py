from app import app
from flask import session, render_template, redirect, url_for

from app.models.user import *

@app.route('/admin/dashboard')
def adminDashboard():
    if 'loggedin' in session:
        if session['role'] == 2 :

            count_users = User().countUser()

            return render_template('admin/admin_dashboard.html', count_user=data_user)

        else :

            return redirect(url_for('bossDashboard'))

    return redirect(url_for('login'))
