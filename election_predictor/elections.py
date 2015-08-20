###############################################################################
#																			  #
# 	This program exhibits machine learning by reading in various pieces of 	  #
#	data by state and year, and based on correct examples, predicts the 	  #
#	outcome of the closest upcoming presidential election to that date in 	  #
#	that state.																  #
#																			  #
#	Used crime data because that was the data available to me.				  #
#																			  #
#		Accuracy: 0.581837381204											  #
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
import math
import time

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

# adjust the weights in response to an incorrect answer; alters the weights
def adjust_weights (data, weights, averages):
	for val in averages:
		if (data[val] > averages[val]):
			if (data['score'] > 0.0):
				weights[val] -= 1.0
	 		else:
	 			weights[val] += 1.0
	return

# set score which will be used to classify the year of the data; alters the data
def set_score (data):
	data['score'] = 0.0
	for val in weights:
	 	data['score'] += data[val] * weights[val]
	return data

#calculate averages of different values
def calculate_averages():
	averages = {"index":0.0, "violent":0.0, "property":0.0, "murder":0.0,
			   "forcible rape":0.0, "robbery":0.0, "aggravated assault":0.0,
	   			"burglary":0.0, "larceny theft":0.0, "vehicle theft":0.0,
	   			"year":0.0}
	for val in averages:
		count = 0.0
		score = 0.0
		for i in range (0, len(data)):
			score += data[i][val]
			count += 1.0
		averages[val] = score/count
	return averages

###############################################################################
#									MAIN									  #
###############################################################################

#open file containing data json
with open('data.json', 'r') as f:
    read_data = f.read()
    data = json.loads(read_data)
f.closed

wrong_results = []
num_correct_test = 0.0
count_test = 0.1
for x in range (0, len(data)):
	#adjust weights until reaching certain standard for accuracy
	#(stastistical significance or a time limit)
	num_correct = 0.0
	weights = {"index":0.0, "violent":0.0, "property":0.0, "murder":0.0,
			   "forcible rape":0.0, "robbery":0.0, "aggravated assault":0.0,
	   			"burglary":0.0, "larceny theft":0.0, "vehicle theft":0.0,
	   			"year":0.0}
	averages = calculate_averages()
	count = 0.1
	start = time.time()
	end = time.time()

	while ((num_correct/count < 0.95) and (end-start < .5)):
		for i in range (0, len(data)):
			if (i != x):
				data[i] = set_score(data[i])
				if ((data[i]['score']  > 0.0 and data[i]['result'] == 0) or
					(data[i]['score'] <= 0.0 and data[i]['result'] == 1)):
					adjust_weights(data[i], weights, averages)
				else:
					num_correct += 1.0
				count += 1.0
				# gets rid of the .1 at the end of count
				# which was originally there to avoid division by 0
				if (count == 1.1): 
					count = 1.0
		end = time.time()

	#now, decide for test data: set scores, measure accuracy of guesses
	data[x] = set_score(data[x])
	if ((data[x]['score']  > 0.0 and data[x]['result'] == 0) or
		(data[x]['score'] <= 0.0 and data[x]['result'] == 1)):
		wrong_results.append(data[x]['result'])
	else:
		num_correct_test += 1.0
	count_test += 1.0
	# gets rid of the .1 at the end of count
	# which was originally there to avoid division by 0
	if (count_test == 1.1):
		count_test = 1.0

print num_correct_test / count_test
