from flask import session
from app import app
from app.config.db import *

class Tagihan:
	
    def selectTagihan(self):
        cursor = mysql.get_db().cursor()
        select_query =  """ SELECT
                            supplier.id,
                                MAX(date_format(pengiriman.create_at, '%d %M %Y')) AS tanggal_pengiriman,
                                supplier.nama_suplier,
                                MAX(pengiriman.status) AS status,
                                SUM(pengiriman.laku * barang.harga_beli) AS total_harga_beli 
                            FROM
                                pengiriman
                            INNER JOIN
                                barang ON pengiriman.id_barang = barang.id 
                            INNER JOIN
                                supplier ON barang.id_supplier = supplier.id 
                            GROUP BY
                                supplier.id, supplier.nama_suplier;
                        """
        cursor.execute(select_query)
        dataTagihan = cursor.fetchall()

        return dataTagihan
        
    def selectPengirimanOne(self, id):
        self.id = id
        cursor = mysql.get_db().cursor()
        select_one = """
                        SELECT 
                            barang.nama_barang, pengiriman.id, pengiriman.status, pengiriman.stok, pengiriman.sisa, pengiriman.laku, 
                            barang.harga_beli, supplier.id, pengiriman.laku * barang.harga_beli AS total_harga_beli 
                        FROM pengiriman INNER JOIN barang ON pengiriman.id_barang=barang.id 
                        INNER JOIN supplier ON barang.id_supplier = supplier.id 
                        WHERE supplier.id = %s
        """
        cursor.execute(select_one, (self.id))
        dataBarangOne = cursor.fetchall()

        return dataBarangOne