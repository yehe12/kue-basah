from flask import session
from app import app
from app.config.db import *

class Tagihan:
	
    def selectTagihan(self):
        cursor = mysql.get_db().cursor()
        select_query =  """ 
                            SELECT
                                DATE_FORMAT(tagihan.create_at, '%d %M %Y') AS create_at,
                                supplier.nama_suplier AS nama_supplier,
                                tagihan.status,
                                SUM(tagihan.neto) AS neto
                            FROM  
                                tagihan
                            INNER JOIN  
                                barang ON tagihan.id_barang = barang.id
                            INNER JOIN  
                                supplier ON barang.id_supplier = supplier.id
                            GROUP BY  
                                DATE_FORMAT(tagihan.create_at, '%d %M %Y'),tagihan.status, supplier.nama_suplier
                            ORDER BY   
                                create_at, nama_supplier;
                        """
        cursor.execute(select_query)
        dataTagihan = cursor.fetchall()

        return dataTagihan
        
    def selectPengirimanOne(self, id):
        self.id = id
        cursor = mysql.get_db().cursor()
        print("cik : ", self.id)
        select_one = """
                        SELECT 
                            barang.nama_barang, pengiriman.id, pengiriman.status, pengiriman.stok, pengiriman.sisa, pengiriman.laku, 
                            barang.harga_beli, supplier.id, pengiriman.laku * barang.harga_beli AS total_harga_beli 
                        FROM pengiriman INNER JOIN barang ON pengiriman.id_barang=barang.id 
                        INNER JOIN supplier ON barang.id_supplier = supplier.id 
                        WHERE tagihan.id = %s
                    """
        cursor.execute(select_one, (self.id))
        dataBarangOne = cursor.fetchall()

        return dataBarangOne
    
    def insertTagihan(self, id_barang, qty, neto):
        self.id_barang = id_barang
        self.qty = qty
        self.neto = neto

        cursor = mysql.get_db().cursor()
        insert_query = "INSERT INTO tagihan (id_barang, qty, neto, status, create_at) VALUES (%s, %s, %s, 'Belum Lunas', now())"
        cursor.execute(insert_query, (self.id_barang, self.qty, self.neto))
        mysql.get_db().commit()
        cursor.close()
        
        return