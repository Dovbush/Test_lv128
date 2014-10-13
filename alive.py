import MySQLdb

class _connect2db(object):
	def __init__(self):
		db = MySQLdb.connect (host= "85.10.205.173", user= "lamp128",
						        passwd= "Rfhnjyrf", db="testbase128", 
						        charset= 'utf8' )
		self.cursor = db.cursor()
		self.all_symbol = ["=", ">", "<", "!=", "<>", ">=", "<="]
		
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
			#head = []
			#for i in range(numrows):
				#head.append(desc[i][0])

			#print head
			#for x in range(0,numrows):
			self.rows = self.cursor.fetchall()
			for i in range(0,numrows):	
				print self.rows[i][0],"      ", self.rows[i][1]
			return self.rows	
#def view(f):
	#for i in f:
		#print i
my=tabl_region()
f=my.print_region("RegionId",">","2")
#view(f)


		
"""class tabl_suppliers(_connect2db):
	def __init__(self):
		self.rows={}
		_connect2db.__init__(self)
		self.all_colums = ["RegionId", "RegionDescription"]

	def print_suppliers(self, colum_name=None, symbol=None, colum_data=None):
			""if you call the method without arguments will show 
			       the entire table, with arguments make filter""
			if not colum_name and not symbol and not colum_data:
				self.cursor.execute ("SELECT * FROM Suppliers")
			if colum_name in self.all_colums:
				if symbol in self.all_symbol:
					sql = "SELECT * FROM Suppliers WHERE Suppliers."
					sql += colum_name + " " + symbol + " " + colum_data	
					self.cursor.execute (sql)
			self.desc = self.cursor.description	
			print "%s %s" % (self.desc[0][0],
			        self.desc[1][0], self.desc[2][0])
			numrows = int(self.cursor.rowcount)
			for x in range(0,numrows):
				self.rows[x] = self.cursor.fetchone()
			for i in range(0,numrows):	
				print self.rows[i][0],"      ", self.rows[i][1]
			return self.rows
my1=tabl_suppliers()
my1.print_suppliers()"""      
