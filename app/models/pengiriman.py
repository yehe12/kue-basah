from flask import session
from app import app
from app.config.db import *

class Pengiriman:
	
    def selectPengiriman(self):
        cursor = mysql.get_db().cursor()
        select_query = "SELECT * from pengiriman INNER JOIN barang ON pengiriman.id_barang=barang.id INNER JOIN supplier ON barang.id_supplier = supplier.id"
        cursor.execute(select_query)
        dataPengiriman = cursor.fetchall()

        return dataPengiriman
    
    def insertPengiriman(self, id_barang, stok, sisa):
        self.id_barang = id_barang
        self.stok = stok
        self.sisa = sisa

        cursor = mysql.get_db().cursor()
        insert_query = "INSERT INTO pengiriman (id_barang, stok, sisa, laku, create_at) VALUES (%s, %s, %s, 0, now())"
        cursor.execute(insert_query, (self.id_barang, self.stok, self.sisa))
        mysql.get_db().commit()
        cursor.close()
        
    def selectBarangOne(self, id):
        self.id = id
        cursor = mysql.get_db().cursor()
        select_one = "SELECT * from barang WHERE id=%s"
        cursor.execute(select_one, (self.id))
        dataBarangOne = cursor.fetchone()

        return dataBarangOne

    def updateBarang(self, id, nama_suplier, nomor_telepon, status, alamat):

        self.id = id
        self.nama_suplier = nama_suplier
        self.nomor_telepon = nomor_telepon
        self.status = status
        self.alamat = alamat

        cursor = mysql.get_db().cursor()
        update_query = "UPDATE barang SET nama_suplier = %s, nomor_telepon = %s, status = %s, alamat = %s WHERE id = %s"
        cursor.execute(update_query, (self.nama_suplier, self.nomor_telepon, self.status, self.alamat, self.id))
        mysql.get_db().commit()
        cursor.close()

    def deleteBarang(self, id):
        self.id = id
        cursor = mysql.get_db().cursor()
        
        # Pengecekan apakah ada referensi foreign key yang masih aktif
        check_query = "SELECT COUNT(*) FROM barang WHERE id_barang = %s"
        cursor.execute(check_query, (self.id,))
        count = cursor.fetchone()[0]
        
        if count > 0:
            return count
        
        else:
            delete_query = "DELETE FROM barang WHERE id=%s"
            cursor.execute(delete_query, (self.id))
            mysql.get_db().commit()
            cursor.close()
            
            return count
        
        

        
        