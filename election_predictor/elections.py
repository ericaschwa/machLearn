#########################################################################################################################
#																														#
# 	This program exhibits machine learning by reading in various pieces of data by state and year, and based on 		#
#	correct examples, predicts the outcome of the closest upcoming presidential election to that date in that state.	#
#																														#
#########################################################################################################################

import json

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

# hold off on writing this program until data gathering process is done

###############################################################################
#									MAIN									  #
###############################################################################

#open file containing data json
with open('data.json', 'r') as f:
    read_data = f.read()
    data = json.loads(read_data)
f.closed

print data[0]