from flask import session
from app import app
from app.config.db import *

class User:
    
    def selectLogin(self, username, password):
        self.username = username
        self.password = password
        
        cursor = mysql.get_db().cursor()
        read_query = "SELECT * FROM user WHERE username=%s AND password=%s"
        cursor.execute(read_query, (self.username, self.password))
        user = cursor.fetchone()
        cursor.close()
        
        return user
    
    def getLogout(self):
        
        session.pop('loggedin', None)
        session.pop('email_verified_at', None)
        session.pop('id', None)
        session.pop('name', None)
        session.pop('username', None)
