from app import app
from app.models.barang import *
from app.models.pembelian import *
from app.models.tagihan import *
from app.models.pengiriman import *
from flask import session, render_template, redirect, url_for, request

@app.route('/data-pembelian/pembelian-baru')
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

@app.route('/data-pembelian')
def bossDataPembelian():
    if 'loggedin' in session:
        if session['role'] == 1 or session['role'] == 2 :
            
            pembayaranInt = 0
            getPembelianDetail = 0
            
            getBarang = Barang().selectBarangNow()
            
            getMaxId = Pembelian().getMaxIdPembelian()
            
            if getMaxId is not None:
                getPembelianDetail = Pembelian().selectPembelianDetail(getMaxId)
                pembayaran = Pembelian().selectSumTotalHarga(getMaxId)

                if pembayaran[0] and pembayaran is not None:
                    pembayaranInt = int(pembayaran[0])
            
            return render_template('menu/data_pembelian.html', dataBarang=getBarang, dataPembelianDetail=getPembelianDetail, dataMaxId=getMaxId, totalPembayaran=pembayaranInt)
        
        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/data-pembelian/store', methods=['POST'])
def bossDataPembelianDetailStore():
    if session['role'] == 1 or session['role'] == 2:
        if request.method == 'POST' and 'id_pengiriman' in request.form and 'id_pembelian' in request.form and 'id_barang' in request.form and 'qty' in request.form and 'total_harga' in request.form and 'neto' in request.form:

            id_pembelian = request.form['id_pembelian']
            id_barang = request.form['id_barang']
            qty = int(request.form['qty'])
            total_harga = int(request.form['total_harga'])
            neto = int(request.form['neto'])
            
            id_pengiriman = int(request.form['id_pengiriman'])
            sisa = int(request.form['sisa'])
            laku = int(request.form['laku'])
            
            total_harga = total_harga * qty
            neto = neto * qty
            
            if sisa >= qty :
                sisa = sisa - qty
                laku = laku + qty
            
                Tagihan().insertTagihan(id_pembelian, id_barang, qty, neto)
                Pembelian().updateStockPengiriman(id_pengiriman, sisa, laku)
                Pembelian().insertPembelianDetail(id_pembelian, id_barang, qty, total_harga, neto, id_pengiriman)

            return redirect(url_for('bossDataPembelian'))
        
    else :
        return redirect(url_for('dashboard'))

    return redirect(url_for('login'))

@app.route('/data-pembelian-detail/destroy/<int:id>/<int:qty>/<int:id_pengiriman>/<int:id_pembelian>/<int:id_barang>', methods = ['GET'])
def bossDataPembelianDetailDelete(id, qty, id_pengiriman, id_pembelian, id_barang):
    if 'loggedin' in session:
        if session['role'] == 1 or session['role'] == 2:
            
            Tagihan().deleteTagihan(id_pembelian, id_barang)
            Pembelian().deletePembelianDetail(id)
            pengiriman = Pengiriman().selectPengirimanOne(id_pengiriman)
            
            sisa = pengiriman[3]
            laku = pengiriman[4]
            
            sisa = sisa + qty
            laku = laku - qty
            
            Pembelian().updateStockPengiriman(id_pengiriman, sisa, laku)

            return redirect(url_for('bossDataPembelian'))

        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))