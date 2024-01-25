from app import app
from app.models.barang import *
from app.models.pembelian import *
from flask import session, render_template, redirect, url_for, request

@app.route('/boss/data-pembelian/pembelian-baru')
def bossDataPembelianStore():
    if 'loggedin' in session:
        if session['role'] == 1 :
            
            hitung = 0
            uang_keluarInt = 0
            uang_masukInt = 0
            laba = 0
            
            getMaxId = Pembelian().getMaxIdPembelian()
            
            if getMaxId is not None:
                hitung = Pembelian().selectSumTotalHarga(getMaxId)
            
                if hitung[0] and hitung[1] and hitung is not None:
                    uang_masukInt = int(hitung[0])
                    uang_keluarInt = int(hitung[1])
                    
                    laba = uang_masukInt - uang_keluarInt
            
            Pembelian().updatePembelian(getMaxId, uang_masukInt, uang_keluarInt, laba)
            
            Pembelian().insertPembelian()
            
            return redirect(url_for('bossDataPembelian'))
        
        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/boss/data-pembelian')
def bossDataPembelian():
    if 'loggedin' in session:
        if session['role'] == 1 :
            
            pembayaranInt = 0
            getPembelianDetail = 0
            
            getBarang = Barang().selectBarangNow()
            
            getMaxId = Pembelian().getMaxIdPembelian()
            
            if getMaxId is not None:
                getPembelianDetail = Pembelian().selectPembelianDetail(getMaxId)
                pembayaran = Pembelian().selectSumTotalHarga(getMaxId)

                if pembayaran[0] and pembayaran is not None:
                    pembayaranInt = int(pembayaran[0])
            
            return render_template('boss/boss_data_pembelian.html', dataBarang=getBarang, dataPembelianDetail=getPembelianDetail, dataMaxId=getMaxId, totalPembayaran=pembayaranInt)
        
        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/boss/data-pembelian/store', methods=['POST'])
def bossDataPembelianDetailStore():
    if session['role'] == 1:
        if request.method == 'POST' and 'id_pembelian' in request.form and 'id_barang' in request.form and 'qty' in request.form and 'total_harga' in request.form and 'neto' in request.form:

            id_pembelian = request.form['id_pembelian']
            id_barang = request.form['id_barang']
            qty = int(request.form['qty'])
            total_harga = int(request.form['total_harga'])
            neto = int(request.form['neto'])
            
            total_harga = total_harga * qty
            neto = neto * qty

            Pembelian().insertPembelianDetail(id_pembelian, id_barang, qty, total_harga, neto)

            return redirect(url_for('bossDataPembelian'))
        
    else :
        return redirect(url_for('dashboard'))

    return redirect(url_for('login'))