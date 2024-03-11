from app import app
from app.models.pembelian import *
from app.models.penjualan import *
from flask import session, render_template, redirect, url_for, request

@app.route('/data-penjualan')
def bossDataPenjualan():
    if 'loggedin' in session:
        if session['role'] == 1 or session['role'] == 2 :
            
            getPembelian = Penjualan().selectPembelian()
            
            return render_template('menu/data_penjualan.html', dataPembelian=getPembelian)
        
        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/data-penjualan/detail/<int:id>', methods = ['GET'])
def bossDataPenjualanOne(id):
    if 'loggedin' in session:
        if session['role'] == 1 or session['role'] == 2 :
            getPembelianOne = Pembelian().selectPembelianDetail(id)

            return render_template('menu/data_penjualan_detail.html', dataPembelianOne=getPembelianOne)

        else :
            return redirect(url_for('dashboard'))

    return redirect(url_for('login'))
