###############################################################################
#																			  #
# 	This program does not exhibit machine learning persay. Instead, it is an  #
#	attempt at the 2015 Mindsumo challenge. This module specifically focuses  #
#   on the first bonus challenge; the main challenge and the second bonus 	  #
#   challenge are dealt with in other modules. The question is as folows:	  #
#																			  #
#	"Give annual revenue numbers for all years between 1966 and 2014. Which   #
#	years had the highest revenue growth, and highest revenue loss?" 		  #													 	  #
#	(source: https://www.mindsumo.com/contests/credit-card-transactions)	  #
#																			  #
###############################################################################

import json
import sys

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################


###############################################################################
#									MAIN									  #
###############################################################################

#open file containing data json
with open('organizedData.json', 'r') as f:
    read_data = f.read()
    data = json.loads(read_data)
f.closed
	