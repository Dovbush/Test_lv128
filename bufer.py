import MySQLdb

class _connect2db():
	def __init__ (self):
		db = MySQLdb.connect (host= "85.10.205.173", user= "lamp128",
							passwd= "Rfhnjyrf", db="testbase128", charset= 'utf8' )
		self.cursor = db.cursor()
		self.all_symbol = ["=", ">", "<", "!=", "<>", ">=", "<="]
		

class tabl_products (_connect2db):
	
	def __init__ (self):
		_connect2db.__init__(self)
		self.rows = {}
		self.all_colums = ["ProductID", "ProductName", "SupplierID", 
				"CategoryID", "QuantityPerUnit", "UnitPrice", "UnitsInStock",
				"UnitsOnOrder", "ReorderLevel", "Discontinued"]
		self.all_symbol = ["=", ">", "<", "!=", "<>", ">=", "<="]

	def view_all(self):
		self.cursor.execute ("SELECT * FROM Products")
		numrows = int(self.cursor.rowcount)
		for x in range(0,numrows):
			self.rows[x] = self.cursor.fetchone()
		return self.rows

	def view_data(self):
		self.cursor.execute ("SELECT Products.ProductID, \
			Products.ProductName, Products.QuantityPerUnit, \
			Products.UnitPrice, Products.UnitsInStock, \
			Products.UnitsOnOrder FROM Products")
		numrows = int(self.cursor.rowcount)
		for x in range(0,numrows):
			self.rows[x] = self.cursor.fetchone()
		return self.rows

	def product_row (self, colum_name, symbol, colum_data):
		if colum_name in self.all_colums:
			if symbol in self.all_symbol:
				sql = "SELECT * FROM Products WHERE Products."
				sql += colum_name + " " + symbol + " " + colum_data
				self.cursor.execute (sql)
				numrows = int(self.cursor.rowcount)
				for x in range(0,numrows):
					self.rows[x] = self.cursor.fetchone()
				return self.rows
			else:
				return ValueError, "Wrong symbol"
		else:
			return ValueError, "Wrong colum name"



class tabl_categories (_connect2db):
	
	def __init__ (self):
		_connect2db.__init__(self)
		self.rows = {}
		self.all_colums = ["CategoryID", "CategoryName", "Description"]
		self.all_symbol = ["=", ">", "<", "!=", "<>", ">=", "<="]

	def view_all(self):
		self.cursor.execute ("SELECT * FROM Categories")
		numrows = int(self.cursor.rowcount)
		for x in range(0,numrows):
			self.rows[x] = self.cursor.fetchone()
		return self.rows

	def categories_row (self, colum_name, symbol, colum_data):
		if colum_name in self.all_colums:
			if symbol in self.all_symbol:
				sql = u"SELECT * FROM Categories WHERE Categories."
				sql = sql + str(colum_name)+ " "+ str(symbol)+ " "+ str(colum_data)
				self.cursor.execute(str(sql))
				numrows = int(self.cursor.rowcount)		
				for x in range(0,numrows):
					self.rows[x] = self.cursor.fetchone()
				return self.rows
			else:
				return ValueError, "Wrong symbol"
		else:
			return ValueError, "Wrong colum name"
class tabl_region(_connect2db):
	def __init__(self):
		self.rows={}
		_connect2db.__init__(self)
		self.all_colums = ["RegionId", "RegionDescription"]

	def print_region(self, colum_name=None, symbol=None, colum_data=None):
			"""if you call the method without arguments will show 
			       the entire table, with arguments make filter"""
			if not colum_name and not symbol and not colum_data:
				self.cursor.execute ("SELECT * FROM Region")
			if colum_name in self.all_colums:
				if symbol in self.all_symbol:
					sql = "SELECT * FROM Region WHERE Region.%s %s %s" % (colum_name, symbol, colum_data)
					self.cursor.execute (sql)
				else:
					return ValueError, "Wrong symbol"
			else:
				return ValueError, "Wrong colum name"
			desc = self.cursor.description	
			numrows = int(self.cursor.rowcount)
			print "%s %s" % (desc[0][0], desc[1][0])
			self.rows = self.cursor.fetchall()
			for i in range(0,numrows):	
				print self.rows[i][0],"      ", self.rows[i][1]
			return self.rows	
