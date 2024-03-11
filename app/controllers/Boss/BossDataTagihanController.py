from app import app
from app.models.tagihan import *
from app.models.pengiriman import *
from app.models.barang import *
from flask import session, render_template, redirect, url_for, request

@app.route('/data-tagihan')
def bossDataTagihan():
    if 'loggedin' in session:
        if session['role'] == 1 or session['role'] == 2:
            
            getTagihan = Tagihan().selectTagihan()
            
            return render_template('menu/data_tagihan.html', dataTagihan=getTagihan)
        
        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/data-tagihan/detail', methods = ['POST'])
def bossDataTagihanOne():
    if 'loggedin' in session:
        if session['role'] == 1 or session['role'] == 2 :
            if request.method == 'POST' and 'create_at' in request.form and 'nama_supplier' in request.form :
                create_at = request.form['create_at']
                nama_supplier = request.form['nama_supplier']
            
                getPengirimanOne = Tagihan().selectPengirimanOne(create_at, nama_supplier)

            return render_template('menu/data_tagihan_detail.html', dataPengirimanOne=getPengirimanOne)

        else :
            return redirect(url_for('dashboard'))

    return redirect(url_for('login'))

@app.route('/data-tagihan/send', methods = ['POST'])
def bossDataIdBarang():
    if 'loggedin' in session:
        if session['role'] == 1 or session['role'] == 2 :
            if request.method == 'POST' and 'create_at' in request.form and 'nama_supplier' in request.form :
                create_at = request.form['create_at']
                nama_supplier = request.form['nama_supplier']
            
                getIdBarang, date = Tagihan().selectIdBarang(create_at, nama_supplier)
                
                for data in getIdBarang :
                    Tagihan().updateStatus(data, date)
                    
                email = "sakkarepkupokok123@gmail.com"
                Tagihan().sendEmail(email)
            
            return redirect(url_for('bossDataTagihan'))

        else :
            return redirect(url_for('dashboard'))

    return redirect(url_for('login'))