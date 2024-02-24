from app import app
from app.models.tagihan import *
from app.models.pengiriman import *
from app.models.barang import *
from flask import session, render_template, redirect, url_for, request

@app.route('/boss/data-tagihan')
def bossDataTagihan():
    if 'loggedin' in session:
        if session['role'] == 1 :
            
            getTagihan = Tagihan().selectTagihan()
            
            return render_template('boss/boss_data_tagihan.html', dataTagihan=getTagihan)
        
        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/boss/data-tagihan/detail', methods = ['POST'])
def bossDataTagihanOne():
    if 'loggedin' in session:
        if session['role'] == 1 :
            if request.method == 'POST' and 'create_at' in request.form and 'nama_supplier' in request.form :
                create_at = request.form['create_at']
                nama_supplier = request.form['nama_supplier']
            
                getPengirimanOne = Tagihan().selectPengirimanOne(create_at, nama_supplier)

            return render_template('boss/boss_data_tagihan_detail.html', dataPengirimanOne=getPengirimanOne)

        else :
            return redirect(url_for('dashboard'))

    return redirect(url_for('login'))

# @app.route('/boss/data-tagihan/detail/update', methods =['POST'])
# def bossDataTagihanUpdate():
#     if 'loggedin' in session:
#         if session['role'] == 1 :
#             if request.method == 'POST' and 'status' in request.form:
#                 id = request.form['id']
#                 status = request.form.getlist('status')

#                 Pengiriman().updatePengirimanStatus(id, status)

#                 return redirect(url_for('bossDataTagihan'))

#         else :
#             return redirect(url_for('dashboard'))
        
#     return redirect(url_for('login'))