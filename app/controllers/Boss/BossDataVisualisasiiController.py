from app import app
from app.models.visualisasi import *
from app.models.barang import *
from flask import session, render_template, redirect, url_for, request

@app.route('/data-visualisasi')
def bossDataVisualisasi():
    if 'loggedin' in session:
        if session['role'] == 1 :
            
            getBarang = Barang().selectBarang()
            
            getFavoritHarian = Visualisasi().selectFavoritHarian()
            getFavoritMingguan = Visualisasi().selectFavoritMingguan()
            
            getOmsetMingguan = Visualisasi().selectOmsetMingguan()
            getOmsetBulanan = Visualisasi().selectOmsetBulanan()
            
            getProfitMingguan = Visualisasi().selectProfitMingguan()
            getProfitBulanan = Visualisasi().selectProfitBulanan()
            
            getReturnMingguan = Visualisasi().selectReturnMingguan()
            
            return render_template('menu/data_visualisasi.html', dataReturnMingguan = getReturnMingguan, dataPerbandingan = "", 
            dataBarang = getBarang, dataProfitBulanan = getProfitBulanan, dataProfitMingguan = getProfitMingguan, 
            dataOmsetBulanan = getOmsetBulanan, dataOmsetMingguan = getOmsetMingguan, dataFavoritHarian=getFavoritHarian, 
            dataFavoritMingguan=getFavoritMingguan, dataCustomFavorit = "", dataTanggalFavorit = "" , dataCustomOmset = "", dataTanggalOmset = "", dataCustomProfit = "", dataTanggalProfit = "",
            dataTanggalReturn="", dataCustomReturn="")
        
        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/data-visualisasi-perbandingan', methods =['POST'])
def bossDataVisualisasiPerbandingan():
    if 'loggedin' in session:
        if session['role'] == 1 :
            if request.method == 'POST':
                
                nama_barang_a = request.form.getlist('nama_barang_a')
                nama_barang_b = request.form.getlist('nama_barang_b')
                tanggal_awal = request.form['tanggal_awal']
                tanggal_akhir = request.form['tanggal_akhir']
                
                getBarang = Barang().selectBarang()
            
                getFavoritHarian = Visualisasi().selectFavoritHarian()
                getFavoritMingguan = Visualisasi().selectFavoritMingguan()
                
                getOmsetMingguan = Visualisasi().selectOmsetMingguan()
                getOmsetBulanan = Visualisasi().selectOmsetBulanan()
                
                getProfitMingguan = Visualisasi().selectProfitMingguan()
                getProfitBulanan = Visualisasi().selectProfitBulanan()
                
                getReturnMingguan = Visualisasi().selectReturnMingguan()

                getPerbandingan = Visualisasi().selectPerbandingan(nama_barang_a, nama_barang_b, tanggal_awal, tanggal_akhir)

                return render_template('menu/data_visualisasi.html', dataReturnMingguan = getReturnMingguan,
                dataPerbandingan = getPerbandingan, dataBarang = getBarang, dataProfitBulanan = getProfitBulanan, 
                dataProfitMingguan = getProfitMingguan, dataOmsetBulanan = getOmsetBulanan, dataOmsetMingguan = getOmsetMingguan, 
                dataFavoritHarian=getFavoritHarian, dataFavoritMingguan=getFavoritMingguan, dataCustomFavorit= "", dataTanggalFavorit = "",
                dataCustomOmset = "", dataTanggalOmset = "", dataCustomProfit = "", dataTanggalProfit = "", dataTanggalReturn="", dataCustomReturn="")

        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/data-visualisasi-favorit', methods =['POST'])
def bossDataVisualisasiCustomFavorit():
    if 'loggedin' in session:
        if session['role'] == 1 :
            if request.method == 'POST':
                
                tanggal_awal = request.form['tanggal_awal']
                tanggal_akhir = request.form['tanggal_akhir']
                
                getBarang = Barang().selectBarang()
            
                getFavoritHarian = Visualisasi().selectFavoritHarian()
                getFavoritMingguan = Visualisasi().selectFavoritMingguan()
                
                getOmsetMingguan = Visualisasi().selectOmsetMingguan()
                getOmsetBulanan = Visualisasi().selectOmsetBulanan()
                
                getProfitMingguan = Visualisasi().selectProfitMingguan()
                getProfitBulanan = Visualisasi().selectProfitBulanan()
                
                getReturnMingguan = Visualisasi().selectReturnMingguan()

                getCustomFavorit= Visualisasi().selectCustomFavorit(tanggal_awal, tanggal_akhir)
                
                getTanggalFavorit = "(" + tanggal_awal + " sampai " + tanggal_akhir + ")"
                
                return render_template('menu/data_visualisasi.html', dataReturnMingguan = getReturnMingguan, dataPerbandingan = "", 
                dataBarang = getBarang, dataProfitBulanan = getProfitBulanan, dataProfitMingguan = getProfitMingguan, dataOmsetBulanan = getOmsetBulanan, 
                dataOmsetMingguan = getOmsetMingguan, dataFavoritHarian=getFavoritHarian, dataFavoritMingguan=getFavoritMingguan, 
                dataCustomFavorit = getCustomFavorit, dataTanggalFavorit = getTanggalFavorit, dataCustomOmset = "", dataTanggalOmset = "", dataCustomProfit = "", dataTanggalProfit = "",
                dataTanggalReturn="", dataCustomReturn="")
        
        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/data-visualisasi-omset', methods =['POST'])
def bossDataVisualisasiCustomOmset():
    if 'loggedin' in session:
        if session['role'] == 1 :
            if request.method == 'POST':
                
                tanggal_awal = request.form['tanggal_awal']
                tanggal_akhir = request.form['tanggal_akhir']
                
                getBarang = Barang().selectBarang()
                
                getFavoritHarian = Visualisasi().selectFavoritHarian()
                getFavoritMingguan = Visualisasi().selectFavoritMingguan()
                
                getOmsetMingguan = Visualisasi().selectOmsetMingguan()
                getOmsetBulanan = Visualisasi().selectOmsetBulanan()
                
                getProfitMingguan = Visualisasi().selectProfitMingguan()
                getProfitBulanan = Visualisasi().selectProfitBulanan()
                
                getReturnMingguan = Visualisasi().selectReturnMingguan()

                getCustomOmset= Visualisasi().selectCustomOmset(tanggal_awal, tanggal_akhir)
                
                print(getCustomOmset)
                
                getTanggalOmset = "(" + tanggal_awal + " sampai " + tanggal_akhir + ")"
                
                return render_template('menu/data_visualisasi.html', dataReturnMingguan = getReturnMingguan, dataPerbandingan = "", 
                dataBarang = getBarang, dataProfitBulanan = getProfitBulanan, dataProfitMingguan = getProfitMingguan, dataOmsetBulanan = getOmsetBulanan, 
                dataOmsetMingguan = getOmsetMingguan, dataFavoritHarian=getFavoritHarian, dataFavoritMingguan=getFavoritMingguan, 
                dataCustomFavorit = "", dataTanggalFavorit = "", dataCustomProfit = "", dataTanggalProfit = "",
                dataCustomOmset = getCustomOmset, dataTanggalOmset = getTanggalOmset, dataTanggalReturn="", dataCustomReturn="")

        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/data-visualisasi-profit', methods =['POST'])
def bossDataVisualisasiCustomProfit():
    if 'loggedin' in session:
        if session['role'] == 1 :
            if request.method == 'POST':
                
                tanggal_awal = request.form['tanggal_awal']
                tanggal_akhir = request.form['tanggal_akhir']
                
                getBarang = Barang().selectBarang()
                
                getFavoritHarian = Visualisasi().selectFavoritHarian()
                getFavoritMingguan = Visualisasi().selectFavoritMingguan()
                
                getOmsetMingguan = Visualisasi().selectOmsetMingguan()
                getOmsetBulanan = Visualisasi().selectOmsetBulanan()
                
                getProfitMingguan = Visualisasi().selectProfitMingguan()
                getProfitBulanan = Visualisasi().selectProfitBulanan()
                
                getReturnMingguan = Visualisasi().selectReturnMingguan()

                getCustomProvit= Visualisasi().selectCustomProfit(tanggal_awal, tanggal_akhir)
                
                print(getCustomProvit)
                
                getTanggalProfit = "(" + tanggal_awal + " sampai " + tanggal_akhir + ")"
                
                return render_template('menu/data_visualisasi.html', dataReturnMingguan = getReturnMingguan, dataPerbandingan = "", 
                dataBarang = getBarang, dataProfitBulanan = getProfitBulanan, dataProfitMingguan = getProfitMingguan, dataOmsetBulanan = getOmsetBulanan, 
                dataOmsetMingguan = getOmsetMingguan, dataFavoritHarian=getFavoritHarian, dataFavoritMingguan=getFavoritMingguan, 
                dataCustomFavorit = "", dataTanggalFavorit = "", dataCustomOmset = "", dataTanggalOmset = "", dataCustomProfit = getCustomProvit, dataTanggalProfit = getTanggalProfit,
                dataTanggalReturn="", dataCustomReturn="")

        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/data-visualisasi-return', methods =['POST'])
def bossDataVisualisasiCustomReturn():
    if 'loggedin' in session:
        if session['role'] == 1 :
            if request.method == 'POST':
                
                tanggal_awal = request.form['tanggal_awal']
                tanggal_akhir = request.form['tanggal_akhir']
                
                getBarang = Barang().selectBarang()
                
                getFavoritHarian = Visualisasi().selectFavoritHarian()
                getFavoritMingguan = Visualisasi().selectFavoritMingguan()
                
                getOmsetMingguan = Visualisasi().selectOmsetMingguan()
                getOmsetBulanan = Visualisasi().selectOmsetBulanan()
                
                getProfitMingguan = Visualisasi().selectProfitMingguan()
                getProfitBulanan = Visualisasi().selectProfitBulanan()
                
                getReturnMingguan = Visualisasi().selectReturnMingguan()

                getCustomReturn= Visualisasi().selectCustomReturn(tanggal_awal, tanggal_akhir)
                
                print(getCustomReturn)
                
                getTanggalReturn = "(" + tanggal_awal + " sampai " + tanggal_akhir + ")"
                
                return render_template('menu/data_visualisasi.html', dataReturnMingguan = getReturnMingguan, dataPerbandingan = "", 
                dataBarang = getBarang, dataProfitBulanan = getProfitBulanan, dataProfitMingguan = getProfitMingguan, dataOmsetBulanan = getOmsetBulanan, 
                dataOmsetMingguan = getOmsetMingguan, dataFavoritHarian=getFavoritHarian, dataFavoritMingguan=getFavoritMingguan, 
                dataCustomFavorit = "", dataTanggalFavorit = "", dataCustomOmset = "", dataTanggalOmset = "", dataCustomProfit = "", dataTanggalProfit = "",
                dataTanggalReturn=getTanggalReturn, dataCustomReturn=getCustomReturn)

        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))