from flask import session
from app import app
from app.config.db import *

class Barang:
	
    def selectBarangSupplier(self, id):
        self.id = id
        cursor = mysql.get_db().cursor()
        select_one = "SELECT * from barang WHERE id_supplier=%s"
        cursor.execute(select_one, (self.id))
        dataBarangSupplier = cursor.fetchall()

        return dataBarangSupplier
    
    def selectBarangNow(self):
        cursor = mysql.get_db().cursor()
        select_query = "SELECT * FROM barang inner JOIN supplier ON barang.id_supplier = supplier.id inner join pengiriman on pengiriman.id_barang = barang.id WHERE DATE(pengiriman.create_at) = CURDATE() and pengiriman.sisa > 0;"
        cursor.execute(select_query)
        dataBarang = cursor.fetchall()

        return dataBarang
    
    def selectBarang(self):
        cursor = mysql.get_db().cursor()
        select_query = "SELECT * from barang INNER JOIN supplier ON barang.id_supplier=supplier.id order by supplier.nama_suplier asc;"
        cursor.execute(select_query)
        dataBarang = cursor.fetchall()

        return dataBarang
    
    def insertBarang(self, id_supplier, nama_barang, harga_jual, harga_beli):
        self.id_supplier = id_supplier
        self.nama_barang = nama_barang
        self.harga_jual = harga_jual
        self.harga_beli = harga_beli

        cursor = mysql.get_db().cursor()
        insert_query = "INSERT INTO barang (id_supplier, nama_barang, harga_jual, harga_beli, create_at) VALUES (%s, %s, %s, %s, now())"
        cursor.execute(insert_query, (self.id_supplier, self.nama_barang, self.harga_jual, self.harga_beli))
        mysql.get_db().commit()
        cursor.close()
        
    def selectBarangOne(self, id):
        self.id = id
        cursor = mysql.get_db().cursor()
        select_one = "SELECT * from barang WHERE id=%s"
        cursor.execute(select_one, (self.id))
        dataBarangOne = cursor.fetchone()

        return dataBarangOne

    def updateBarang(self, id, nama_barang, harga_jual, harga_beli):

        self.id = id
        self.nama_barang = nama_barang
        self.harga_jual = harga_jual
        self.harga_beli = harga_beli

        cursor = mysql.get_db().cursor()
        update_query = "UPDATE barang SET nama_barang = %s, harga_jual = %s, harga_beli = %s WHERE id = %s"
        cursor.execute(update_query, (self.nama_barang, self.harga_jual, self.harga_beli, self.id))
        mysql.get_db().commit()
        cursor.close()

    def deleteBarang(self, id):
        self.id = id
        cursor = mysql.get_db().cursor()
        
        delete_query = "DELETE FROM barang WHERE id=%s"
        cursor.execute(delete_query, (self.id))
        mysql.get_db().commit()
        cursor.close()