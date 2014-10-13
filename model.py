import MySQLdb

class _db_connect():
	def __init__(self):
		db = MySQLdb.connect(host="85.10.205.173", user="lamp128", passwd="Rfhnjyrf",
					db="testbase128")
		self.cursor = db.cursor()


class Products(_db_connect):
	def __init__(self):
		_db_connect.__init__(self)

	def all_products(self):
		self.cursor.execute("SELECT * FROM Products")
		all_prod = self.cursor.fetchall()
		return all_prod

	def prod_by_id(self, id):
		self.cursor.execute("SELECT * FROM Products WHERE ProductID = " + str(id))
		prod = self.cursor.fetchall();
		return prod;

	def prod_count(self):
		self.cursor.execute("SELECT * FROM Products")
		count = self.cursor.rowcount
		return count

	def prod_by_cat(self, id):
		self.cursor.execute("SELECT * FROM Products WHERE CategoryID = " + str(id))
		prod = self.cursor.fetchall();
		return prod
