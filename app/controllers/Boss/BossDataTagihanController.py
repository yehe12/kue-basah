from app import app
from app.models.tagihan import *
from app.models.pengiriman import *
from app.models.barang import *
from app.models.supplier import *
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
            if request.method == 'POST' and 'create_at' in request.form and 'nama_supplier' in request.form and 'jumlah_tagihan' in request.form :
                create_at = request.form['create_at']
                nama_supplier = request.form['nama_supplier']
                jumlah_tagihan = request.form['jumlah_tagihan']
            
                getIdBarang, date = Tagihan().selectIdBarang(create_at, nama_supplier)
                
                getFullTagihan = Tagihan().selectFullTagihan(nama_supplier, create_at)
                
                for data in getIdBarang :
                    Tagihan().updateStatus(data, date)
                    
                # email = "ma22052000@gmail.com"
                
                email = Supplier().selectEmail(nama_supplier)
                
                print(email)
                
                Tagihan().sendEmail(email, jumlah_tagihan, getFullTagihan)
                
            
            return redirect(url_for('bossDataTagihan'))

        else :
            return redirect(url_for('dashboard'))

    return redirect(url_for('login'))