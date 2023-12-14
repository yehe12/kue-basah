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
    
    def selectBarang(self):
        cursor = mysql.get_db().cursor()
        select_query = "SELECT * from barang INNER JOIN supplier ON barang.id_supplier=supplier.id;"
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
        
        # Pengecekan apakah ada referensi foreign key yang masih aktif
        cek_penjualan = "SELECT COUNT(*) FROM penjualan WHERE id_barang = %s"
        cek_pengiriman = "SELECT COUNT(*) FROM pengiriman WHERE id_barang = %s"
        
        cursor.execute(cek_penjualan, (self.id,))
        count_penjualan = cursor.fetchone()[0]

        cursor.execute(cek_pengiriman, (self.id,))
        count_pengiriman = cursor.fetchone()[0]
        
        print("penjualan :", count_penjualan)
        print("pengiriman :", count_pengiriman)
        
        if count_penjualan != 0 and count_pengiriman != 0:
            delete_query = "DELETE FROM barang WHERE id=%s"
            cursor.execute(delete_query, (self.id))
            mysql.get_db().commit()
            cursor.close()
            
            return count_penjualan+count_pengiriman
        
        else:
            return count_penjualan+count_pengiriman