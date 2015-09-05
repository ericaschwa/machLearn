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
		alreadyHas = 0
		for val in IDs:
			if (val['id'] == ID):
				alreadyHas = 1
				val['subscriptions'].append({
					"id":		item['id'],
					"amount":	item['amount'],
					"date":		item['date'],
					"duration":	0,
					"type":		'one-off'
				})
				break
		if (alreadyHas == 0):
			IDs.append({
				"id": ID,
				"subscriptions":[{
					"id":		item['id'],
					"amount":	item['amount'],
					"date":		item['date'],
					"duration":	0,
					"type":		'one-off'
				}]
			})
	IDs = categorize(IDs)
	IDs = calcDuration(IDs)
	return IDs


# categorizes subscriptions by whether they're daily, monthly, yearly, or
# one-off. Sets "type" attribute of data.
def categorize(data):
	# sort data by date (date is in terms of days)
	data = insertionSort(data)

	# then categorize it
	for val in data:
		items = val['subscriptions']
		# if there are fewer than two items, the type is one-off (the default)
		if (len(items) < 2):
			break


def calcDuration(data):
	return 1

# sorts the data items by date
def insertionSort(array):
	for val in range(0,len(array)):
		data = array[val]['subscriptions']
		for index in range(1,len(data)):
			currentvalue = data[index]
			position = index
			while (position > 0 and data[position - 1]['date'] > currentvalue['date']):
				data[position] = data[position - 1]
				position = position - 1
			data[position] = currentvalue
	return array


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
# print organizedData