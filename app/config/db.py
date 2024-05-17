from app import app #penting
from app.config.key import *

from flaskext.mysql import MySQL

db_user = 'root'
db_password = 'yehez123'
db_name = 'kue_basah'
db_host = 'localhost'

app.config['MYSQL_DATABASE_USER'] = db_user
app.config['MYSQL_DATABASE_PASSWORD'] = db_password
app.config['MYSQL_DATABASE_DB'] = db_name
app.config['MYSQL_DATABASE_HOST'] = db_host

mysql = MySQL(app)
conn = mysql.connect()
if conn:
    print('koneksi berhasil')
else:
    print('koneksi gagal')
