###############################################################################
#																		      #
# 	This program reads in data about financial transactions (id,              #
#	subscription, amount, and date) from an excel spreadsheet, and prints     #
#	this data in JSON form to a file.										  #
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
	wb = xlrd.open_workbook('subscription_report.xls')
	sh = wb.sheet_by_index(0)

	transactionData = []

	# Iterate through each row in worksheet and fetch values into dict
	for rownum in range(1, sh.nrows):
		row_values = sh.row_values(rownum)
		data = OrderedDict()
		data['id'] = row_values[0]
		data['subscription'] = row_values[1]
		data['amount'] = row_values[2]
		data['data'] = row_values[3]
		transactionData.append(data)
	
	# Put the list of dicts to JSON
	j = json.dumps(transactionData)
	with open('data.json', 'w') as f:
	    f.write(j)
	f.closed


###############################################################################
#									MAIN									  #
###############################################################################

make_data()
