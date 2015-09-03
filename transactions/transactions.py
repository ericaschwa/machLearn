###############################################################################
#																			  #
# 	This program exhibits machine learning by reading in various pieces of 	  #
#	data by state and year, and based on correct examples, predicts the 	  #
#	outcome of the closest upcoming presidential election to that date in 	  #
#	that state.																  #
#																			  #
#	Used crime data because that was the data available to me.				  #
#																			  #
#		Accuracy: 0.581837381204 without energy data 						  #
#				  0.716528162512 with energy data							  #
#				  0.709141274238 with income data 							  #
#				  0.736842105263 with just income stderr 					  #
#				  0.722068328717 with population change data 				  #
#				  0.722991689751 with minimum wage data 					  #
#																			  #
# 		Accuracy values and significance of the difference between these	  #
#			values and a 50% accuracy (guessing)							  #
#			P value and statistical significance: 							  #
#  			The two-tailed P value is less than 0.0001						  #
#  			By conventional criteria, this difference is considered to be 	  #
#			extremely statistically significant. 							  #
#																			  #
#			 (source: http://graphpad.com/quickcalcs/oneSampleT2/)			  #
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
with open('data.json', 'r') as f:
    read_data = f.read()
    data = json.loads(read_data)
f.closed
