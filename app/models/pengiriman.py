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
        
    def selectPengirimanOne(self, id):
        self.id = id
        cursor = mysql.get_db().cursor()
        select_one = "SELECT * from pengiriman INNER JOIN barang ON pengiriman.id_barang=barang.id INNER JOIN supplier ON barang.id_supplier = supplier.id where pengiriman.id = %s"
        cursor.execute(select_one, (self.id))
        dataBarangOne = cursor.fetchone()

        return dataBarangOne

    def updatePengiriman(self, id, stok):

        self.id = id
        self.stok = stok

        cursor = mysql.get_db().cursor()
        update_query = "UPDATE pengiriman SET stok = %s WHERE id = %s"
        cursor.execute(update_query, (self.stok, self.stok, self.id))
        mysql.get_db().commit()
        cursor.close()

    def deletePengiriman(self, id):
        self.id = id
        cursor = mysql.get_db().cursor()
        
        delete_query = "DELETE FROM pengiriman WHERE id=%s"
        cursor.execute(delete_query, (self.id))
        mysql.get_db().commit()
        cursor.close()
        
        

        
        