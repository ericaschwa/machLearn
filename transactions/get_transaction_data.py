###############################################################################
#																		      #
# 	This program reads in data about financial transactions (id,              #
#	subscription, amount, and date) from an excel spreadsheet, and prints     #
#	this data in JSON form to a file.										  #
#																			  #
###############################################################################

import json
import xlrd
import csv
from collections import OrderedDict

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

# get the transaction data, turn it from csv format into JSON format
# source: https://www.mindsumo.com/contests/credit-card-transactions
def make_data():
	# Open the workbook
	with open('subscription_report-2.csv') as csvfile:
		reader = csv.DictReader(csvfile)

		transactionData = []

		# Iterate through each row in worksheet and fetch values into dict
		for row in reader:
			data = OrderedDict()
			data['id'] = row['Id']
			data['subscription'] = row['Subscription ID']
			data['amount'] = row['Amount (USD)']
			data['date'] = row['Transaction Date']
			transactionData.append(data)
	
	# Put the list of dicts to JSON
	j = json.dumps(transactionData)
	with open('data.json', 'w') as f:
	    f.write(j)
	f.closed

# get the transaction data, turn it from csv format into JSON format
# source: https://www.mindsumo.com/contests/credit-card-transactions
# note: only gets the date and the subscription ID
def make_dates_data():
	# Open the workbook
	with open('subscription_report-2.csv') as csvfile:
		reader = csv.DictReader(csvfile)

		transactionData = []

		# Iterate through each row in worksheet and fetch values into dict
		for row in reader:
			data = OrderedDict()
			data['subscription'] = row['Subscription ID']
			data['date'] = row['Transaction Date']
			transactionData.append(data)
	
	# Put the list of dicts to JSON
	j = json.dumps(transactionData)
	with open('data.json', 'w') as f:
	    f.write(j)
	f.closed

# get the transaction data, turn it from csv format into JSON format
# source: https://www.mindsumo.com/contests/credit-card-transactions
# note: only gets the date, the amount, and the subscription ID
def make_amount_data():
	# Open the workbook
	with open('subscription_report-2.csv') as csvfile:
		reader = csv.DictReader(csvfile)

		transactionData = []

		# Iterate through each row in worksheet and fetch values into dict
		for row in reader:
			data = OrderedDict()
			data['subscription'] = row['Subscription ID']
			data['amount'] = row['Amount (USD)']
			data['date'] = row['Transaction Date']
			transactionData.append(data)
	
	# Put the list of dicts to JSON
	j = json.dumps(transactionData)
	with open('dataBonus.json', 'w') as f:
	    f.write(j)
	f.closed

# get the year cuttoff data, turn it from excel format into JSON format
# (I put the year cuttoff data in, in order to make the first bonus question
# easier)
# TODO: is there a way to do this without the excel file? Maybe a built in
# python function?
def make_years():
	# Open the workbook
	wb = xlrd.open_workbook('years.xlsx')
	sh = wb.sheet_by_index(0)

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

#make_data()
make_dates_data()
make_amount_data()
make_years()
