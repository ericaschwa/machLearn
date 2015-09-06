###############################################################################
#																			  #
# 	This program does not exhibit machine learning persay. Instead, it is an  #
#	attempt at the 2015 Mindsumo challenge. This module specifically focuses  #
#   on the second bonus challenge; the main challenge and the first bonus 	  #
#   challenge are dealt with in other modules. The question is as folows:	  #
#																			  #
#	"Predict annual revenue for year 2015 (based on historical retention and  #
#	new subscribers)" 		  												  #
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

print data[0]
