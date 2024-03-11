from app import app
from flask_mail import *

app.secret_key = "teserah saya"
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'kuelestarii@gmail.com'
app.config['MAIL_PASSWORD'] =  'idrc npxg ivvq ncxq'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)