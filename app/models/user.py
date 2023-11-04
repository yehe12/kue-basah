from flask import session
from app import app
from app.config.db import *

class User:
	
	def ambil_email_user(self, user_id):
		self.user_id = user_id

		cursor = mysql.get_db().cursor()
		read_query = "SELECT email from user WHERE id=%s;"
		cursor.execute(read_query, (self.user_id))
		user_email = cursor.fetchone()

		return user_email


	#fungsi admin
	def countUser(self):

		cursor = mysql.get_db().cursor()
		select_query = "SELECT count(id) FROM user"
		cursor.execute(select_query)
		count_user = cursor.fetchone()

		return count_user

	def countNewUser(self):

		cursor = mysql.get_db().cursor()
		select_query = "SELECT count(id) FROM user WHERE MONTH(create_at) = MONTH(now()) AND YEAR(create_at) = YEAR(now())"
		cursor.execute(select_query)
		count_new_user = cursor.fetchone()

		return count_new_user

	def selectUser(self):

		cursor = mysql.get_db().cursor()
		select_query = "SELECT * from user"
		cursor.execute(select_query)
		user = cursor.fetchall()

		return user

	def selectRole(self):

		cursor = mysql.get_db().cursor()
		select_query = "SELECT * from role"
		cursor.execute(select_query)
		role = cursor.fetchall()

		return role

	def selectUserDetail(self, id):

		self.id = id
		
		cursor = mysql.get_db().cursor()
		select_query = "SELECT * from user WHERE id=%s"
		cursor.execute(select_query, (self.id))
		user_detail = cursor.fetchone()

		return user_detail

	def updateUser(self, id, name, password, address, phone):

		self.id = id
		self.name = name
		self.password = password
		self.address = address
		self.phone = phone

		cursor = mysql.get_db().cursor()
		update_query = "UPDATE user SET name = %s, password = %s, address = %s, phone = %s WHERE id = %s"
		cursor.execute(update_query, (self.name, self.password, self.address, self.phone, self.id))

		mysql.get_db().commit()
		cursor.close()

	def deleteUser(self, id):

		self.id = id

		cursor = mysql.get_db().cursor()
		delete_query = "DELETE FROM user WHERE id=%s"
		cursor.execute(delete_query, (self.id))

		mysql.get_db().commit()
		cursor.close()

	#akhir fungsi role admin
	
	#fungsi login dan register
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
		session.pop('email', None)

	#akhir fungsi login dan register
