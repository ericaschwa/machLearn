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


###############################################################################
#									MAIN									  #
###############################################################################

make_dates_data()
make_amount_data()
