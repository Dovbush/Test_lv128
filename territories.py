import MySQLdb

class _db_connect():
	def __init__(self):
		db = MySQLdb.connect(host="85.10.205.173", user="lamp128", passwd="Rfhnjyrf",
					db="testbase128")
		self.cursor = db.cursor()

class territories (_db_connect):
	def __init__ (self):
		_db_connect.__init__(self)
		self.rows = {}
		self.ter_columns = ["TerritoryID", "TerritoryDescription", "RegionID"]
		#self.all_symbol = ["=", ">", "<", "!=", "<>", ">=", "<="]
	def all_print(self):
		self.cursor.execute ("SELECT * FROM Territories")
		numrows = int(self.cursor.rowcount)
		for x in range(0,numrows):
			self.rows[x] = self.cursor.fetchone()
		return self.rows
	def data_print(self):
		self.cursor.execute ("SELECT Territories.TerritoryID, \
			Territories.TerritoryDescription FROM Territories")
		numrows = int(self.cursor.rowcount)
		for x in range(0,numrows):
			self.rows[x] = self.cursor.fetchone()
		return self.rows
	def descr_row (self, column_name, column_data):
		if column_name in self.ter_columns:
			territ = "SELECT * FROM Territories WHERE TerritoryDescription."
			territ += column_name +  " " + column_data
			self.cursor.execute (territ)
			numrows = int(self.cursor.rowcount)
			for x in range(0,numrows):
				self.rows[x] = self.cursor.fetchone()
			return self.rows
		else:
			return ValueError, "Wrong name of column"


def view (func):
	for i in func:
		print func[i]
	""" test bufer block """
A = territories ()
view(A.data_print())




