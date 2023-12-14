from app import app
from app.models.barang import *
from app.models.supplier import *
from flask import session, render_template, redirect, url_for, request

@app.route('/boss/data-barang')
def bossDataBarang():
    if 'loggedin' in session:
        if session['role'] == 1 :
            
            getBarang = Barang().selectBarang()
            getSupplier = Supplier().selectSupplier()
            
            return render_template('boss/boss_data_barang.html', dataBarang=getBarang, dataSupplier=getSupplier)
        
        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/boss/data-barang/store', methods=['POST'])
def bossDataBarangStore():
    if session['role'] == 1:
        if request.method == 'POST' and 'id_supplier' in request.form and 'nama_barang' in request.form and 'harga_jual' in request.form and 'harga_beli' in request.form:
            id_supplier = request.form.getlist('id_supplier')
            nama_barang = request.form['nama_barang']
            harga_jual = request.form['harga_jual']
            harga_beli = request.form['harga_beli']

            Barang().insertBarang(id_supplier, nama_barang, harga_jual, harga_beli)

            return redirect(url_for('bossDataBarang'))
        
    else :
        return redirect(url_for('dashboard'))

    return redirect(url_for('login'))

@app.route('/boss/data-barang/detail/<int:id>', methods = ['GET'])
def bossDataBarangOne(id):
    if 'loggedin' in session:
        if session['role'] == 1 :
            getBarangOne = Barang().selectBarangOne(id)

            return render_template('boss/boss_data_barang_detail.html', dataBarangOne=getBarangOne)

        else :
            return redirect(url_for('dashboard'))

    return redirect(url_for('login'))

@app.route('/boss/data-barang/detail/update', methods =['POST'])
def bossDataBarangUpdate():
    if 'loggedin' in session:
        if session['role'] == 1 :
            if request.method == 'POST' and 'id_supplier' in request.form and 'nama_barang' in request.form and 'harga_jual' in request.form and 'harga_beli' in request.form:
                id = request.form['id']
                nama_barang = request.form['nama_barang']
                harga_jual = request.form['harga_jual']
                harga_beli = request.form['harga_beli']

                Barang().updateBarang(id, nama_barang, harga_jual, harga_beli)

                return redirect(url_for('bossDataBarang'))

        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/boss/data-barang/destroy/<int:id>', methods = ['GET'])
def bossDataBarangDelete(id):
    if 'loggedin' in session:
        if session['role'] == 1 :
            getBarang = Barang().selectBarang()
            data = Barang().deleteBarang(id)
            
            if data > 0:
                mesage = 'Tidak dapat menghapus barang karena masih terdapat data Pengiriman atau Penjualan!'
                return render_template('boss/boss_data_barang.html', dataBarang=getBarang, mesage = mesage)
            
            else:
                return redirect(url_for('bossDataBarang'))

        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))