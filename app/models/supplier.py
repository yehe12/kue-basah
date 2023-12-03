from flask import session
from app import app
from app.config.db import *

class Supplier:
	
    def selectSupplier(self):
        
        cursor = mysql.get_db().cursor()
        dataSupplier = "SELECT * FROM supplier;"
        # dataSupplier = "SELECT nama_suplier, umur FROM supplier;"
        cursor.execute(dataSupplier)
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
