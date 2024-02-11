from flask import session
from app import app
from app.config.db import *

class Penjualan:
	
    def selectPembelian(self):
        cursor = mysql.get_db().cursor()
        select_query = "SELECT * from Pembelian WHERE uang_masuk != 0 AND uang_keluar != 0 AND laba != 0"
        cursor.execute(select_query)
        dataPembelian = cursor.fetchall()

        return dataPembelian