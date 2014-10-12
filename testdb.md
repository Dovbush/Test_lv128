import MySQLdb

db = MySQLdb.connect(host="85.10.205.173", user="lamp128", passwd="Rfhnjyrf", db="testbase128")


class Database():
	def cust (self, CustomerId, ContactName):
		self.CustomerId = CustomerId
		self.ContactName = ContactName

		return CustomerId, ContactName

	def order_det(self, OrderId, ProductID, UnitPrice, Quantity, Discount):
		self.OrderId = OrderId
		self.ProductID = ProductID
		self.UnitPrice = UnitPrice
		self.Quantity = Quantity
		self.Discount = Discount

		return OrderId, ProductID, UnitPrice, Quantity, Discount

	def query(self, q):
		cursor = self.connection.cursor(MySQLdb.cursor)
		cursor.execute(q)
		return fetchall()

if __name__ == '__main__' :
	db = Database(12, 'Roman')
	
