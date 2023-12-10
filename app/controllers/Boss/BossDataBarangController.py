from app import app
from app.models.barang import *
from flask import session, render_template, redirect, url_for, request

@app.route('/boss/data-barang')
def bossDataBarang():
    if 'loggedin' in session:
        if session['role'] == 1 :
            
            getBarang = Barang().selectBarang()
            
            return render_template('boss/boss_data_barang.html', dataBarang=getBarang)
        
        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/boss/data-barang/store', methods=['POST'])
def bossDataBarangStore():
    if session['role'] == 1:
        if request.method == 'POST' and 'nama_suplier' in request.form and 'nomor_telepon' in request.form and 'status' in request.form and 'alamat' in request.form:
            nama_suplier = request.form['nama_suplier']
            nomor_telepon = request.form['nomor_telepon']
            status = request.form.getlist('status')
            alamat = request.form['alamat']

            Barang().insertBarang(nama_suplier, nomor_telepon, status, alamat)

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
            if request.method == 'POST' and 'nama_suplier' in request.form and 'nomor_telepon' in request.form and 'status' in request.form and 'alamat' in request.form:
                id = request.form['id']
                nama_suplier = request.form['nama_suplier']
                nomor_telepon = request.form['nomor_telepon']
                status = request.form.getlist('status')
                alamat = request.form['alamat']

                Barang().updateBarang(id, nama_suplier, nomor_telepon, status, alamat)

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
                mesage = 'Tidak dapat menghapus barang karena masih terdapat data Barang!'
                return render_template('boss/boss_data_barang.html', dataBarang=getBarang, mesage = mesage)
            
            else:
                return redirect(url_for('bossDataBarang'))

        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))