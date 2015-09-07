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
		data['date'] = row_values[3]
		transactionData.append(data)
	
	# Put the list of dicts to JSON
	j = json.dumps(transactionData)
	with open('data.json', 'w') as f:
	    f.write(j)
	f.closed

# get the year cuttoff data, turn it from excel format into JSON format
# (I put the year cuttoff data in, in order to make the first bonus question
# easier)
def make_years():
	# Open the workbook
	wb = xlrd.open_workbook('subscription_report.xls')
	sh = wb.sheet_by_index(1)

	yearData = []

	# Iterate through each row in worksheet and fetch values into dict
	for rownum in range(0, sh.nrows):
		row_values = sh.row_values(rownum)
		data = OrderedDict()
		data['date'] = row_values[0]
		yearData.append(data)
	
	# Put the list of dicts to JSON
	j = json.dumps(yearData)
	with open('yearData.json', 'w') as f:
	    f.write(j)
	f.closed


###############################################################################
#									MAIN									  #
###############################################################################

make_data()
make_years()
