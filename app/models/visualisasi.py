from flask import session
from app import app
from app.config.db import *

class Visualisasi:
	
    def selectFavoritHarian(self):
        cursor = mysql.get_db().cursor()
        select_query =  """ SELECT id_barang, barang.nama_barang, SUM(qty) AS total_qty
                            FROM pembelian_detail inner join barang on pembelian_detail.id_barang = barang.id
                            WHERE DATE(pembelian_detail.create_at) = CURRENT_DATE()
                            GROUP BY id_barang
                            ORDER BY total_qty DESC
                            limit 5;
                        """
        cursor.execute(select_query)
        dataFavorit = cursor.fetchall()

        return dataFavorit

    def selectFavoritMingguan(self):
        cursor = mysql.get_db().cursor()
        select_query =  """ SELECT id_barang, barang.nama_barang, SUM(qty) AS total_qty
                            FROM pembelian_detail inner join barang on pembelian_detail.id_barang = barang.id
                            WHERE DATE(pembelian_detail.create_at) BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 6 DAY) AND CURRENT_DATE()
                            GROUP BY id_barang
                            ORDER BY total_qty DESC
                            limit 5;
                        """
        cursor.execute(select_query)
        dataFavorit = cursor.fetchall()

        return dataFavorit
    
    def selectCustomFavorit(self, tanggal_awal, tanggal_akhir):
        self.tanggal_awal = tanggal_awal
        self.tanggal_akhir = tanggal_akhir

        cursor = mysql.get_db().cursor()
        select_query = """ SELECT id_barang, barang.nama_barang, SUM(qty) AS total_qty
                            FROM pembelian_detail inner join barang on pembelian_detail.id_barang = barang.id

                            WHERE DATE(pembelian_detail.create_at) BETWEEN %s AND %s
                            GROUP BY id_barang
                            ORDER BY total_qty DESC
                            limit 5;
                        """
        cursor.execute(select_query, (self.tanggal_awal, self.tanggal_akhir))
        dataCustomFavorit= cursor.fetchall()
        
        return dataCustomFavorit
    
    def selectOmsetMingguan(self):
        cursor = mysql.get_db().cursor()
        select_query =  """ select date(`timestamp`), sum(uang_masuk) from pembelian
                            WHERE DATE(timestamp) BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 6 DAY) AND CURRENT_DATE()
                            GROUP by DATE(`timestamp`)
                            order by DATE(`timestamp`)
                        """
        cursor.execute(select_query)
        dataOmset = cursor.fetchall()

        return dataOmset
    
    def selectOmsetBulanan(self):
        cursor = mysql.get_db().cursor()
        select_query =  """ select date(`timestamp`), sum(uang_masuk) from pembelian
                            WHERE DATE(timestamp) BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 29 day) AND CURRENT_DATE()
                            GROUP by DATE(`timestamp`)
                            order by DATE(`timestamp`)
                        """
        cursor.execute(select_query)
        dataOmset = cursor.fetchall()

        return dataOmset
    
    def selectCustomOmset(self, tanggal_awal, tanggal_akhir):
        self.tanggal_awal = tanggal_awal
        self.tanggal_akhir = tanggal_akhir

        cursor = mysql.get_db().cursor()
        select_query = """ SELECT date(`timestamp`), sum(uang_masuk) from pembelian
                            WHERE DATE(timestamp) BETWEEN %s AND %s
                            GROUP by DATE(`timestamp`)
                            order by DATE(`timestamp`)
                        """
        cursor.execute(select_query, (self.tanggal_awal, self.tanggal_akhir))
        dataCustomOmset= cursor.fetchall()
        
        return dataCustomOmset
    
    def selectProfitMingguan(self):
        cursor = mysql.get_db().cursor()
        select_query =  """ select date(`timestamp`), sum(laba) from pembelian
                            WHERE DATE(timestamp) BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 6 DAY) AND CURRENT_DATE()
                            GROUP by DATE(`timestamp`)
                            order by DATE(`timestamp`)
                        """
        cursor.execute(select_query)
        dataProfit = cursor.fetchall()

        return dataProfit
    
    def selectProfitBulanan(self):
        cursor = mysql.get_db().cursor()
        select_query =  """ select date(`timestamp`), sum(laba) from pembelian
                            WHERE DATE(timestamp) BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 29 day) AND CURRENT_DATE()
                            GROUP by DATE(`timestamp`)
                            order by DATE(`timestamp`)
                        """
        cursor.execute(select_query)
        dataProfit= cursor.fetchall()

        return dataProfit
    
    def selectReturnMingguan(self):
        cursor = mysql.get_db().cursor()
        select_query =  """ select barang.id, barang.nama_barang, SUM(pengiriman.sisa) AS total_sisa
                            from pengiriman
                            inner join barang on barang.id = pengiriman.id_barang
                            WHERE DATE(pengiriman.create_at) BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 6 DAY) AND CURRENT_DATE()
                            GROUP BY barang.id
                            ORDER BY total_sisa DESC
                            limit 10;
                        """
        cursor.execute(select_query)
        dataReturn= cursor.fetchall()

        return dataReturn
                    
    def selectPerbandingan(self, nama_barang_a,nama_barang_b, tanggal_awal, tanggal_akhir):
        self.nama_barang_a = nama_barang_a
        self.nama_barang_b = nama_barang_b
        self.tanggal_awal = tanggal_awal
        self.tanggal_akhir = tanggal_akhir

        cursor = mysql.get_db().cursor()
        select_query = """  SELECT b.nama_barang, SUM(p.laku)
                            FROM barang b
                            INNER JOIN pengiriman p ON p.id_barang = b.id
                            WHERE date(p.create_at) BETWEEN %s AND %s
                            AND b.nama_barang IN (%s, %s)
                            GROUP BY b.nama_barang;
                    """
        cursor.execute(select_query, (self.tanggal_awal, self.tanggal_akhir, self.nama_barang_a, self.nama_barang_b))
        dataPerbandingan= cursor.fetchall()
        
        return dataPerbandingan
