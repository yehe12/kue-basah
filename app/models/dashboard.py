from flask import session
from app import app
from app.config.db import *

class Dashboard:
	
    def selectProfitDay(self):
        
        cursor = mysql.get_db().cursor()
        select_query = "select sum(laba) from pembelian p WHERE DATE(timestamp) = CURDATE()"
        cursor.execute(select_query)
        profitDay = cursor.fetchone()[0]
        
        return profitDay
    
    def selectProfitWeek(self):
        
        cursor = mysql.get_db().cursor()
        select_query = "SELECT sum(laba) FROM pembelian WHERE DATE(timestamp) BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 6 DAY) AND CURRENT_DATE()"
        cursor.execute(select_query)
        profitWeek = cursor.fetchone()[0]
        
        return profitWeek
    
    def selectOmsetDay(self):
        cursor = mysql.get_db().cursor()
        select_query = "SELECT sum(uang_masuk) FROM pembelian WHERE DATE(timestamp) = CURDATE()"
        cursor.execute(select_query)
        omsetDay =  cursor.fetchone()[0]

        return omsetDay
    
    def selectOmsetWeek(self):
        cursor = mysql.get_db().cursor()
        select_query = "SELECT sum(uang_masuk) FROM pembelian WHERE DATE(timestamp) BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 6 DAY) AND CURRENT_DATE()"
        cursor.execute(select_query)
        omsetWeek =  cursor.fetchone()[0]

        return omsetWeek