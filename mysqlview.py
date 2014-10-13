import bufer

def show_tab (di):
	for i in di:
		print di[i]

""" test bufer block """
A = bufer.tabl_products ()

show_tab (A.product_row("UnitPrice", "=", "2.5") )

print "####################"

B = bufer.tabl_categories ()
show_tab ( B.categories_row("CategoryID", "=", "1") )

#My test

c=bufer.tabl_region()
c.print_region("RegionId",">","2")