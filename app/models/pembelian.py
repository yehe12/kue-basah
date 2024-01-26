from flask import session
from app import app
from app.config.db import *

class Pembelian:
	
    def insertPembelianDetail(self, id_pembelian, id_barang, qty, total_harga, neto):
        self.id_pembelian = id_pembelian
        self.id_barang = id_barang
        self.qty = qty
        self.total_harga = total_harga
        self.neto = neto

        cursor = mysql.get_db().cursor()
        insert_query = "INSERT INTO pembelian_detail (id_pembelian, id_barang, qty, total_harga, neto, create_at) VALUES (%s, %s, %s, %s, %s, now())"
        cursor.execute(insert_query, (self.id_pembelian, self.id_barang, self.qty, self.total_harga, self.neto))
        mysql.get_db().commit()
        cursor.close()
        
        return

    def getMaxIdPembelian(self):
        cursor = mysql.get_db().cursor()
        select_query = "SELECT MAX(id) FROM pembelian;"
        cursor.execute(select_query)
        count = cursor.fetchone()[0]

        return count
    
    def insertPembelian(self):
        cursor = mysql.get_db().cursor()
        insert_query = "INSERT INTO pembelian (uang_keluar, uang_masuk, laba, timestamp) VALUES (0, 0, 0, now())"
        cursor.execute(insert_query)
        mysql.get_db().commit()
        cursor.close()

    def selectPembelianDetail(self, id):
        self.id = id
        cursor = mysql.get_db().cursor()
        select_query = "SELECT * from pembelian_detail INNER JOIN barang ON pembelian_detail.id_barang=barang.id WHERE id_pembelian=%s"
        cursor.execute(select_query, (self.id))
        dataPembelianDetail = cursor.fetchall()

        return dataPembelianDetail
    
    def selectSumTotalHarga(self, id):
        self.id = id
        cursor = mysql.get_db().cursor()
        select_query = "SELECT SUM(total_harga) AS total_harga_jumlah, SUM(neto) AS total_neto FROM pembelian_detail WHERE id_pembelian = %s"
        cursor.execute(select_query, (self.id))
        count = cursor.fetchone()
        
        return count
    
    def updatePembelian(self, id, uang_masuk, uang_keluar, laba):

        self.id = id
        self.uang_masuk = uang_masuk
        self.uang_keluar = uang_keluar
        self.laba = laba

        cursor = mysql.get_db().cursor()
        update_query = "UPDATE pembelian SET uang_masuk = %s, uang_keluar = %s, laba = %s WHERE id = %s"
        cursor.execute(update_query, (self.uang_masuk, self.uang_keluar, self.laba, self.id))
        mysql.get_db().commit()
        cursor.close()
        
    def deletePembelianDetail(self, id):
        self.id = id
        cursor = mysql.get_db().cursor()

        delete_query = "DELETE FROM pembelian_detail WHERE id=%s"
        cursor.execute(delete_query, (self.id))
        mysql.get_db().commit()
        cursor.close()