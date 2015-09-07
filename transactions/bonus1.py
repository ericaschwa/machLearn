###############################################################################
#																			  #
# 	This program does not exhibit machine learning persay. Instead, it is an  #
#	attempt at the 2015 Mindsumo challenge. This module specifically focuses  #
#   on the first bonus challenge; the main challenge and the second bonus 	  #
#   challenge are dealt with in other modules. The question is as folows:	  #
#																			  #
#	"Give annual revenue numbers for all years between 1966 and 2014. Which   #
#	years had the highest revenue growth, and highest revenue loss?" 		  #
#	(source: https://www.mindsumo.com/contests/credit-card-transactions)	  #
#																			  #
###############################################################################

import json
import sys

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

# organizes the data by year so that the program can then print
# the list of years, and the revenue each year
def organize(data, yearData):
	# initialize all years between 1966 and 2014 to a revenue of 0
	years = []
	for n in range(1966,2015):
		years.append({"year":n,"amount":0})

	# set the "date" attribute of each data item to a correct year value
	for item in data:
		for m in range(0,49):
			if (item['date'] >= yearData[m]['date'] and
				item['date'] < yearData[m+1]['date']):
				item['date'] = 1966 + m

	# add all amounts to the appropriate year
	for item in data:
		for val in years:
			if (val['year'] == item['date']):
				val['amount'] += item['amount']
				break

	return years


def find_highest(data):
	return 1

def find_lowest(data):
	return 1

###############################################################################
#									MAIN									  #
###############################################################################

#open file containing data json
with open('data.json', 'r') as f:
    read_data = f.read()
    data = json.loads(read_data)
f.closed

#open file containing data json
with open('yearData.json', 'r') as f:
    read_data = f.read()
    yearData = json.loads(read_data)
f.closed

# organize data by subscription ID and print
years = organize(data, yearData)
for val in years:
	print val

# print find_highest(years)
# print find_lowest(years)
	