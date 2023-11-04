from app import app
from flask import session, render_template, redirect, url_for

from app.models.user import *
from app.models.repair import *

@app.route('/admin/dashboard')
def adminDashboard():
    if 'loggedin' in session:
        if session['role'] == 2 :

            count_users = User().countUser()
            repairTaken = Repair().countRepairTaken()
            count_cost_totals = Repair().countCostTotal()
            count_repairs = Repair().countRepair()
            count_in_repairs = Repair().countInRepair()

            taken =  int(repairTaken[0])
            
            data_cost_total = 0
            if taken != 0:    
                data_cost_total =  int(count_cost_totals[0])

            data_repair = str(count_repairs[0]).strip("()'")

            data_in_repair = str(count_in_repairs[0]).strip("()'")

            data_user = str(count_users[0]).strip("()'")

            return render_template('admin/admin_dashboard.html', count_user=data_user, count_cost_total=data_cost_total, count_repair=data_repair, count_in_repair=data_in_repair)

        else :

            return redirect(url_for('bossDashboard'))

    return redirect(url_for('login'))
