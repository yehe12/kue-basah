from app import app
from flask import session, render_template, redirect, url_for

from app.models.user import *

@app.route('/admin-dashboard')
def adminDashboard():
    if 'loggedin' in session:
        if session['role'] == 2 :

            getName = session['name']
            
            return render_template('admin/admin_dashboard.html', dataName = getName)

        else :

            return redirect(url_for('bossDashboard'))

    return redirect(url_for('login'))