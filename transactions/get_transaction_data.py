###############################################################################
#																		      #
# 	This program reads in data structures containing crime and election       #
#	data from JSON files and excels, combines them into one json		      #
#	object, and prints this JSON object to a file.						      #
#																			  #
#	Used crime data because that was the data available to me.				  #
#																			  #
###############################################################################

import json
import xlrd
from collections import OrderedDict

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

# get the transaction data, turn it from excel format into JSON format
# source: https://www.mindsumo.com/contests/credit-card-transactions
def make_data():
	# Open the workbook
	wb = xlrd.open_workbook('income.xls')
	sh = wb.sheet_by_index(0)

	incomeData = []

	# Iterate through each row in worksheet and fetch values into dict
	for rownum in range(0, sh.nrows):
		row_values = sh.row_values(rownum)
		for colnum in range(0, 24):
			data = OrderedDict()
			data['state'] = row_values[0]
			data['year'] = 2013 - colnum
			data['income'] = row_values[2 * colnum + 1]
			data['income stderr'] = row_values[2 * colnum + 2]
			incomeData.append(data)
	
	#Serialize the list of dicts to JSON
	j = json.dumps(incomeData)
	with open('incomedata.json', 'w') as f:
	    	f.write(j)
	f.closed


###############################################################################
#									MAIN									  #
###############################################################################

make_data()
