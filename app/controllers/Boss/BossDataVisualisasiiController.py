from app import app
from app.models.visualisasi import *
from app.models.barang import *
from flask import session, render_template, redirect, url_for, request

@app.route('/boss/data-visualisasi')
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
            
            return render_template('boss/boss_data_visualisasi.html', dataReturnMingguan = getReturnMingguan, dataPerbandingan = "", dataBarang = getBarang, dataProfitBulanan = getProfitBulanan, dataProfitMingguan = getProfitMingguan, dataOmsetBulanan = getOmsetBulanan, dataOmsetMingguan = getOmsetMingguan, dataFavoritHarian=getFavoritHarian, dataFavoritMingguan=getFavoritMingguan)
        
        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))

@app.route('/boss/data-visualisasi-perbandingan', methods =['POST'])
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

                print("data ne : ", getPerbandingan)
                
                return render_template('boss/boss_data_visualisasi.html', dataReturnMingguan = getReturnMingguan, dataPerbandingan = getPerbandingan, dataBarang = getBarang, dataProfitBulanan = getProfitBulanan, dataProfitMingguan = getProfitMingguan, dataOmsetBulanan = getOmsetBulanan, dataOmsetMingguan = getOmsetMingguan, dataFavoritHarian=getFavoritHarian, dataFavoritMingguan=getFavoritMingguan)

        else :
            return redirect(url_for('dashboard'))
        
    return redirect(url_for('login'))