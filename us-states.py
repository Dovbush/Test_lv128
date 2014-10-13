import MySQLdb

class _db_connect():
	def __init__(self):
		db = MySQLdb.connect(host="85.10.205.173", user="lamp128", passwd="Rfhnjyrf",
					db="testbase128")
		self.cursor = db.cursor()

class us_states (_db_connect):
	def __init__ (self):
		_db_connect.__init__(self)
		self.rows = {}
		self.us_columns = ["StateId", "StateName", "StateAbbr","StateRegion"]
		#self.all_symbol = ["=", ">", "<", "!=", "<>", ">=", "<="]
	def all_print(self):
		self.cursor.execute ("SELECT * FROM USStates")
		numrows = int(self.cursor.rowcount)
		for x in range(0,numrows):
			self.rows[x] = self.cursor.fetchone()
		return self.rows
	def data_print(self):
		self.cursor.execute ("SELECT USStates.StateId, \
			USStates.StateAbbr FROM USStates")
		numrows = int(self.cursor.rowcount)
		for x in range(0,numrows):
			self.rows[x] = self.cursor.fetchone()
		return self.rows


def view (func):
	for i in func:
		print func[i]
	""" test bufer block """
A = us_states ()
view(A.all_print())
