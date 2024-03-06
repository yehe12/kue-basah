from flask import session
from app import app
from app.config.db import *

class Dashboard:
	
    def selectProfitDay(self):
        
        cursor = mysql.get_db().cursor()
        select_query = "select sum(laba) from pembelian p WHERE DATE(`timestamp`) = CURDATE()"
        cursor.execute(select_query)
        profitDay = cursor.fetchone()[0]
        
        return profitDay
    
    # def selectProfitWeek(self):
        
    #     self.id = id
        
    #     cursor = mysql.get_db().cursor()
    #     select_query = "SELECT stok, sisa FROM pengiriman WHERE id = %s"
    #     cursor.execute(select_query, (self.id))
    #     count = cursor.fetchone()
        
    #     return count
    
    # def selectOmsetDay(self):
    #     cursor = mysql.get_db().cursor()
    #     select_query = "SELECT *, pengiriman.laku * barang.harga_beli AS total_harga_beli, date(pengiriman.create_at) from pengiriman INNER JOIN barang ON pengiriman.id_barang=barang.id INNER JOIN supplier ON barang.id_supplier = supplier.id ORDER BY pengiriman.create_at DESC"
    #     cursor.execute(select_query)
    #     dataPengiriman = cursor.fetchall()

    #     return dataPengiriman
        
    # def selectOmsetWeek(self, id):
    #     self.id = id
    #     cursor = mysql.get_db().cursor()
    #     select_one = "SELECT *, pengiriman.laku * barang.harga_beli AS total_harga_beli from pengiriman INNER JOIN barang ON pengiriman.id_barang=barang.id INNER JOIN supplier ON barang.id_supplier = supplier.id where pengiriman.id = %s"
    #     cursor.execute(select_one, (self.id))
    #     dataBarangOne = cursor.fetchone()

    #     return dataBarangOne