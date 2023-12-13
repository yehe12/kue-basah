from app import app
from app.models.barang import *
from app.models.supplier import *
from app.models.pengiriman import *
from flask import session, render_template, redirect, url_for, request

@app.route('/boss/data-pengiriman')
def bossDataPengiriman():
    if 'loggedin' in session:
        if session['role'] == 1 :
            
            getPengiriman = Pengiriman().selectPengiriman()
            getSupplier = Supplier().selectSupplier()
            getBarang = Barang().selectBarang()
            
            return render_template('boss/boss_data_pengiriman.html', dataPengiriman=getPengiriman, dataSupplier=getSupplier, dataBarang=getBarang)
        
        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/boss/data-pengiriman/store', methods=['POST'])
def bossDataPengirimanStore():
    if session['role'] == 1:
        if request.method == 'POST' and 'id_barang' in request.form and 'stok' in request.form and 'sisa' in request.form and 'laku' in request.form:
            id_barang = request.form.getlist('id_barang')
            stok = request.form['stok']
            sisa = request.form['sisa']
            laku = request.form['laku']
            
            print("ini jalan id_barang ", id_barang)
            print("ini jalan stok ", stok)
            print("ini jalan sisa ", sisa)
            print("ini jalan laku ", laku)

            Pengiriman().insertPengiriman(id_barang, stok, sisa, laku)

            return redirect(url_for('bossDataPengiriman'))
        
    else :
        return redirect(url_for('dashboard'))

    return redirect(url_for('login'))

@app.route('/boss/data-pengiriman/detail/<int:id>', methods = ['GET'])
def bossDataPengirimanOne(id):
    if 'loggedin' in session:
        if session['role'] == 1 :
            getPengirimanOne = Pengiriman().selectPengirimanOne(id)

            return render_template('boss/boss_data_barang_detail.html', dataPengirimanOne=getPengirimanOne)

        else :
            return redirect(url_for('dashboard'))

    return redirect(url_for('login'))

@app.route('/boss/data-pengiriman/detail/update', methods =['POST'])
def bossDataPengirimanUpdate():
    if 'loggedin' in session:
        if session['role'] == 1 :
            if request.method == 'POST' and 'nama_suplier' in request.form and 'nomor_telepon' in request.form and 'status' in request.form and 'alamat' in request.form:
                id = request.form['id']
                nama_suplier = request.form['nama_suplier']
                nomor_telepon = request.form['nomor_telepon']
                status = request.form.getlist('status')
                alamat = request.form['alamat']

                Pengiriman().updatePengiriman(id, nama_suplier, nomor_telepon, status, alamat)

                return redirect(url_for('bossDataPengiriman'))

        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/boss/data-pengiriman/destroy/<int:id>', methods = ['GET'])
def bossDataPengirimanDelete(id):
    if 'loggedin' in session:
        if session['role'] == 1 :
            getPengiriman = Pengiriman().selectPengiriman()
            data = Pengiriman().deletePengiriman(id)
            
            if data > 0:
                mesage = 'Tidak dapat menghapus barang karena masih terdapat data Barang!'
                return render_template('boss/boss_data_barang.html', dataPengiriman=getPengiriman, mesage = mesage)
            
            else:
                return redirect(url_for('bossDataPengiriman'))

        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))