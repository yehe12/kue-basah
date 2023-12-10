from flask import session
from app import app
from app.config.db import *

class Supplier:
	
    def selectSupplier(self):
        cursor = mysql.get_db().cursor()
        select_query = "SELECT * FROM supplier ORDER BY create_at DESC;"
        # dataSupplier = "SELECT nama_suplier, umur FROM supplier;"
        cursor.execute(select_query)
        dataSupplier = cursor.fetchall()

        return dataSupplier
    
    def insertSupplier(self, nama_suplier, nomor_telepon, status, alamat):
        self.nama_suplier = nama_suplier
        self.nomor_telepon = nomor_telepon
        self.status = status
        self.alamat = alamat

        cursor = mysql.get_db().cursor()
        insert_query = "INSERT INTO supplier (nama_suplier, nomor_telepon, alamat, status, create_at) VALUES (%s, %s, %s, %s, now())"
        cursor.execute(insert_query, (self.nama_suplier, self.nomor_telepon, self.alamat, self.status))
        mysql.get_db().commit()
        cursor.close()
        
    def selectSupplierOne(self, id):
        self.id = id
        cursor = mysql.get_db().cursor()
        select_one = "SELECT * from supplier WHERE id=%s"
        cursor.execute(select_one, (self.id))
        dataSupplierOne = cursor.fetchone()

        return dataSupplierOne

    def updateSupplier(self, id, nama_suplier, nomor_telepon, status, alamat):

        self.id = id
        self.nama_suplier = nama_suplier
        self.nomor_telepon = nomor_telepon
        self.status = status
        self.alamat = alamat

        cursor = mysql.get_db().cursor()
        update_query = "UPDATE supplier SET nama_suplier = %s, nomor_telepon = %s, status = %s, alamat = %s WHERE id = %s"
        cursor.execute(update_query, (self.nama_suplier, self.nomor_telepon, self.status, self.alamat, self.id))
        mysql.get_db().commit()
        cursor.close()

    def deleteSupplier(self, id):
        self.id = id
        cursor = mysql.get_db().cursor()
        delete_query = "DELETE FROM supplier WHERE id=%s"
        cursor.execute(delete_query, (self.id))
        mysql.get_db().commit()
        cursor.close()