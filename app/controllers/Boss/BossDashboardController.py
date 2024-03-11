from app import app
from flask import session, render_template, redirect, url_for

from app.models.dashboard import *

@app.route('/dashboard')
def bossDashboard():
    if 'loggedin' in session:
        if session['role'] == 1 :

            getProfitDay = Dashboard().selectProfitDay()
            getProfitWeek = Dashboard().selectProfitWeek()
            getOmsetDay = Dashboard().selectOmsetDay()
            getOmsetWeek = Dashboard().selectOmsetWeek()
            
            return render_template('menu/dashboard.html', dataOmsetWeek = getOmsetWeek, dataOmsetDay = getOmsetDay, dataProfitDay = getProfitDay, dataProfitWeek = getProfitWeek)

        else :

            return redirect(url_for('adminDashboard'))

    return redirect(url_for('login'))
