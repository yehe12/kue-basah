from app import app
from app.models.user import *
from flask import session, render_template, redirect, url_for

# from app.models.user import *

@app.route('/boss/data-supplier')
def bossDataSupplier():
    if 'loggedin' in session:
        if session['role'] == 1 :
            
            getSupplier = User().selectSupplier()

            return render_template('boss/boss_data_supplier.html', dataSupplier=getSupplier)
        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))
