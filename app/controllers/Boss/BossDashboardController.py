from app import app
from flask import session, render_template, redirect, url_for

from app.models.dashboard import *

@app.route('/boss/dashboard')
def bossDashboard():
    if 'loggedin' in session:
        if session['role'] == 1 :

            getProfitDay = Dashboard().selectProfitDay()
            
            print("prifit : ", getProfitDay)
            
            return render_template('boss/boss_dashboard.html', dataProfitDay = getProfitDay)

        else :

            return redirect(url_for('adminDashboard'))

    return redirect(url_for('login'))
