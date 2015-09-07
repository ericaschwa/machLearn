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
def organize(data):
	# initialize all years between 1966 and 2014 to a revenue of 0
	years = []
	for n in range(1966,2015):
		years.append({"year":n,"amount":0})

	# add all amounts to the appropriate year
	for item in data:
		for val in years:
			itemYear = item['date'] # TODO
			if (val['year'] == itemYear):
				val['amount'] += item['amount']
				break

	print data[0]['date']
	print data[4]['date']

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

# organize data by subscription ID and print
years = organize(data)
# for val in years:
# 	print val

# print find_highest(years)
# print find_lowest(years)

# also save this data structure as a JSON file
j = json.dumps(years)
with open('years.json', 'w') as f:
    f.write(j)
f.closed
	