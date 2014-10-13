import unittest
import bufer

class test_tabls_products (unittest.TestCase):
	
	def setUp (self):
		self.tp = bufer.tabl_products()
		self.tc = bufer.tabl_categories ()

	def test_product_row1 (self):
		row = {(33L, u'Geitost', 15L, 4L, u'500 g', Decimal('2.5000'), 112, 0, 20, 0)}
		test = self.tp.product_row("UnitPrice", "=", "2.5")
		self.assertDictEqual (test, row)

	def test_product_row2 (self):
		ext = ValueError, "Wrong symbol"
		test = self.tp.product_row("UnitPrice", "==", "2.5")
		self.assertEquals (test, ext)

	def test_product_row3 (self):
		ext = ValueError, "Wrong colum name"
		test = self.tp.product_row("Unit", "=", "2.5")
		self.assertEquals (test, ext)


	def test_categories_row1 (self):
		row = (1L, u'Beverages', u'Soft drinks, coffees, teas, beers, and ales' )
		test = self.tc.categories_row("CategoryID", "=", "1")
		self.assertEquals (test, row)

	def test_categories_row2 (self):
		ext = ValueError, "Wrong symbol"
		test = self.tc.categories_row("CategoryID", "423", "2")
		self.assertEquals (test, ext)

	def test_categories_row3 (self):
		ext = ValueError, "Wrong colum name"
		test = self.tc.categories_row("ID", "=", "4")
		self.assertEquals (test, ext)


if __name__ == '__main__':
	unittest.main()