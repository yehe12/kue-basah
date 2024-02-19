from flask import session
from app import app
from app.config.db import *

class Visualisasi:
	
    def selectVisualisasiHarian(self):
        cursor = mysql.get_db().cursor()
        select_query =  """ SELECT id_barang, barang.nama_barang, SUM(qty) AS total_qty
                            FROM pembelian_detail inner join barang on pembelian_detail.id_barang = barang.id
                            GROUP BY id_barang;
                        """
        cursor.execute(select_query)
        dataVisualisasi = cursor.fetchall()

        return dataVisualisasi
