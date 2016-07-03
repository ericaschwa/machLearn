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
import datetime
from datetime import datetime

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

START_YEAR = 1966
END_YEAR = 2015

# organizes the data by year so that the program can then print
# the list of years, and the revenue each year
def organize(data):

	# initialize all years between 1966 and 2014 to a revenue of 0
	years = {}
	for n in range(START_YEAR - 1,END_YEAR):
		years[n] = 0

	# add all amounts to the appropriate year
	for item in data:
		item['date'] = datetime.strptime(item['date'], '%m/%d/%Y')
		years[item['date'].year] += int(item['amount'])

	# calculate revenue changes for all years between 1966 and 2015
	revenuechanges = {}
	for i in range(START_YEAR, END_YEAR):
		revenuechanges[i] = years[i] - years[i-1]

	return revenuechanges


def find_highest(data):
	return 1

def find_lowest(data):
	return 1

###############################################################################
#									MAIN									  #
###############################################################################

#open file containing data json
with open('dataBonus.json', 'r') as f:
    read_data = f.read()
    data = json.loads(read_data)
f.closed

# organize data by subscription ID and print years with highest growth and highest loss
years = organize(data)
print max(years, key=years.get) # highest growth
print min(years, key=years.get) # highest loss
	