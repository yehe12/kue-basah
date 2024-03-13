from flask import session
from app import app
from app.config.db import *

class Tagihan:
	
    def selectTagihan(self):
        cursor = mysql.get_db().cursor()
        select_query =  """ 
                            SELECT
                                DATE(tagihan.create_at) AS create_at,
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
                                DATE(tagihan.create_at),tagihan.status, supplier.nama_suplier
                            ORDER BY   
                                create_at desc, nama_supplier;
                        """
        cursor.execute(select_query)
        dataTagihan = cursor.fetchall()

        return dataTagihan
        
    def selectPengirimanOne(self, create_at, nama_supplier):
        self.create_at = create_at
        self.nama_supplier = nama_supplier
        
        cursor = mysql.get_db().cursor()
        select_one = """
                        SELECT   
                            DATE(tagihan.create_at) AS create_at,
                            supplier.nama_suplier,
                            barang.nama_barang,
                            sum(tagihan.qty),
                            SUM(tagihan.neto) AS total_neto
                        FROM   
                            tagihan
                        INNER JOIN   
                            barang ON barang.id = tagihan.id_barang
                        INNER JOIN   
                            supplier ON supplier.id = barang.id_supplier
                        where supplier.nama_suplier = %s AND date(tagihan.create_at) = date(%s)
                        GROUP BY   
                            DATE(tagihan.create_at), supplier.nama_suplier, barang.nama_barang
                        ORDER BY   
                            DATE(tagihan.create_at), supplier.nama_suplier, barang.nama_barang
                    """
        cursor.execute(select_one, (self.nama_supplier, self.create_at))
        
        dataBarangOne = cursor.fetchall()
        
        return dataBarangOne
    
    def insertTagihan(self, id_pembelian, id_barang, qty, neto):
        self.id_pembelian = id_pembelian
        self.id_barang = id_barang
        self.qty = qty
        self.neto = neto

        cursor = mysql.get_db().cursor()
        insert_query = "INSERT INTO tagihan (id_pembelian, id_barang, qty, neto, status, create_at) VALUES (%s, %s, %s, %s, 'Belum Lunas', now())"
        cursor.execute(insert_query, (self.id_pembelian, self.id_barang, self.qty, self.neto))
        mysql.get_db().commit()
        cursor.close()
        
        return
    
    def selectIdBarang(self, create_at, nama_supplier):
        self.create_at = create_at
        self.nama_supplier = nama_supplier
        
        cursor = mysql.get_db().cursor()
        
        select_query = "SELECT distinct  tagihan.id_barang FROM tagihan JOIN barang ON tagihan.id_barang = barang.id JOIN supplier ON barang.id_supplier = supplier.id WHERE DATE(tagihan.create_at) = DATE(%s) AND supplier.nama_suplier = %s"
        cursor.execute(select_query, (self.create_at, self.nama_supplier))
        
        dataIdBarang = cursor.fetchall()
        
        return dataIdBarang, self.create_at
    
    def updateStatus(self, id, create_at):
        self.create_at = create_at
        self.id = id
        
        cursor = mysql.get_db().cursor()
        update_query = "UPDATE tagihan SET status = 'Lunas' WHERE id_barang = %s AND DATE(tagihan.create_at) = DATE(%s)"
        cursor.execute(update_query, (self.id, self.create_at))
        mysql.get_db().commit()
        cursor.close()
        
    def deleteTagihan(self, id_pembelian, id_barang):
        self.id_pembelian = id_pembelian
        self.id_barang = id_barang
        cursor = mysql.get_db().cursor()

        delete_query = "DELETE FROM tagihan WHERE id_pembelian=%s AND id_barang = %s"
        cursor.execute(delete_query, (self.id_pembelian, self.id_barang))
        mysql.get_db().commit()
        cursor.close()
        
    def selectFullTagihan(self, nama_supplier, create_at):
        
        self.create_at = create_at
        self.nama_supplier = nama_supplier
        
        cursor = mysql.get_db().cursor()
        select_query = """
                        select barang.nama_barang, barang.harga_beli, pengiriman.stok, pengiriman.sisa, pengiriman.laku, date(pengiriman.create_at )
                        from pengiriman
                        join barang on barang.id = pengiriman.id_barang 
                        join supplier on supplier.id = barang.id_supplier
                        where supplier.nama_suplier = %s
                        and date(pengiriman.create_at) = date(%s)"""
                        
        cursor.execute(select_query, (self.nama_supplier, self.create_at))
        
        dataFullTagihan = cursor.fetchall()
        
        return dataFullTagihan
            
    def sendEmail(self, email, jumlah_tagihan, dataFullTagihan):
        self.email = email
        self.dataFullTagihan = dataFullTagihan
        self.jumlah_tagihan = jumlah_tagihan
        
        email = self.email[0]

        email_body = "Daftar Barang : \n\n"

        for row in self.dataFullTagihan:
            email_body += f"Tanggal Pengiriman : {row[5]}\n"
            email_body += f"Nama Barang : {row[0]}\n"
            email_body += f"Harga : {row[1]}\n"
            email_body += f"Stok : {row[2]}\n"
            email_body += f"Sisa : {row[3]}\n"
            email_body += f"Laku : {row[4]}\n"
            email_body += f"Jumlah Harga : {row[1] * row[4]}"
            email_body += "\n__________________________________________\n"
        
        email_body += f"\n Jumlah Tagihan : {self.jumlah_tagihan}"
            
        msg = Message(subject='Pemberitahuan Status Pembayaran Tagihan', sender='orang@example.com', recipients=[email])
        msg.body = email_body
        
        mail.send(msg)