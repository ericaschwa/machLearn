###############################################################################
#																			  #
# 	This program does not exhibit machine learning persay. Instead, it is an  #
#	attempt at the 2015 Mindsumo challenge. This module specifically focuses  #
#   on the main challenge; the bonus questions are dealt with in other 		  #
#   modules. The challenge is as folows:		 							  #
#																			  #
#	"Using the transactions data attached below, ..." (by the run time of  	  #
#	this program, these transactions will be stored in JSON format in a   	  #
#   file called data.json) "... write a script in Java, Python, C/C++, or 	  #
#	JavaScript that outputs a list of subscription IDs, their subscription 	  #
#	type (daily, monthly, yearly, one-off), and the duration of their 		  #
#	subscription. 														 	  #
#	(source: https://www.mindsumo.com/contests/credit-card-transactions)	  #
#																			  #
###############################################################################

import json
import sys

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

# organizes the data by subscription ID so that the program can then print
# the list of subscription IDs, their subscription type, and the duration of
# their subscripton.
def organize(data):
	IDs = []
	for item in data:
		ID = item['subscription']
		alreadyHas = false
		for val in IDs:
			if (val['id'] == ID):
				alreadyHas = true
				val['subscriptions'].append({ "id": 	item['id'],
											  "amount": item['amount'],
											  "date": item['date']
											})
		if (not alreadyHas):
			IDs.append({
				"id": ID,
				"subscriptions": [{"id": 		item['id'],
								   "amount": 	item['amount'],
								   "date": 		item['date']
								  }]
				})


# categorizes subscriptions by whether they're daily, monthly, yearly, or
# one-off
def categorize(data):
	return 1

###############################################################################
#									MAIN									  #
###############################################################################

#open file containing data json
with open('data.json', 'r') as f:
    read_data = f.read()
    data = json.loads(read_data)
f.closed

# organize data by subscription ID and print
organizedData = organize(data)
print organizedData