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
#	subscription."														 	  #
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
			print val['id'], ID
			if (val['id'] == ID): # ID already appears, put data in with that
				alreadyHas = 1
				val['dates'].append(item['date'])
				break
		if (alreadyHas == 0): # ID is new, create a new entry for it
			IDs.append({
				"id": 			ID,
				"duration":		0, # default value for duration
				"type":			'one-off', # default value for type
				"dates":		[item['date']]
			})
	IDs = categorize(IDs)
	return IDs


# categorizes subscriptions by whether they're daily, monthly, yearly, or
# one-off. Sets "type" attribute of data.
# also calculates the duration of each subscription, and sets the "duration"
# attribute of the data.
# given that each data item's "dates" array is already sorted (since the
# csv file was sorted by date)
def categorize(data):
	for val in data:
		items = val['dates']

		# this works because the subscriptions list is sorted by date
		val['duration'] = items[len(items)-1] - items[0]

		# if there are one or fewer items, the type is one-off (the default)
		if (len(items) > 1):
			# this works because the subscriptions list is sorted by date
			diff = items[1] - items[0]
			if (diff > -1 and diff < 3): # daily, room for error of 2
				val['type'] = 'daily'
			elif (diff > 27 and diff < 33): # monthly, room for error of 3
				val['type'] = 'monthly'
			elif (diff > 360 and diff < 370): # yearly, room for error of 5
				val['type'] = 'yearly'
			else:
				print "ERROR: type of some entries doesn't fit into a category"

	return data

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
for val in organizedData:
	print val['id'], val['type'], val['duration']
