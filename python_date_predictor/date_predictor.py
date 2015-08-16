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
	averages = {"index":0.0,"violent":0.0,"property":0.0,"murder":0.0,
		   		"forcible rape":0.0,"robbery":0.0, "aggravated assault":0.0,
		   		"burglary":0.0,"larceny theft":0.0,"vehicle theft":0.0}
	for val in averages:
		count = 0.0
		score = 0.0
		states_measured = len(crimedata)
		for i in range (0, states_measured):
			years_measured = len(crimedata[i]['data'])
			for j in range(0, years_measured):
				score += crimedata[i]['data'][j][val]
				count += 1.0
		averages[val] = score/count
	return averages

def year_avg():
	count = 0.0
	score = 0.0
	states_measured = len(crimedata)
	for x in range (0, states_measured):
		years_measured = len(crimedata[x]['data'])
		for n in range (0, years_measured):
			score += crimedata[x]['data'][n]['year']
			count += 1.0
	return score / count


###############################################################################
#									MAIN									  #
###############################################################################

#open file containing sample data json
with open('crimedata.json', 'r') as f: # to use file that includes the test data (accuracy: 0.962962962963)
     read_data = f.read()
     crimedata = json.loads(read_data)
f.closed

wrong_years = []
total = 0.0
states_measured = len(crimedata)
for x in range (0, states_measured):
	if (crimedata[x]['data'] != []):
		#adjust weights until reaching statistical significance for accuracy
		num_correct = 0.0
		weights = {"index":0.0,"violent":0.0,"property":0.0,"murder":0.0,
		   		"forcible rape":0.0,"robbery":0.0, "aggravated assault":0.0,
		   		"burglary":0.0,"larceny theft":0.0,"vehicle theft":0.0}
		averages = calculate_averages()
		count = 0.1
		start = time.time()
		end = time.time()
		while ((num_correct/count < 0.95) and (end-start < 30)): # for full struct: between .9121 and .9123; .9085 and .9090 for "clean weights"
			for i in range (0, states_measured): # for just last 7: between .900 and .908
				if (i != x):
					years_measured = len(crimedata[i]['data'])
					for j in range(0, years_measured):
						data = set_score(crimedata[i]['data'][j])
						if ((data['score']  > 0.0 and data['year'] < 1986) or
							(data['score'] <= 0.0 and data['year'] >= 1986)):
							adjust_weights(data, weights, averages)
						else:
							num_correct += 1.0
						count += 1.0
						if (count == 1.1): # gets rid of the .1 at the end of count which was originally there to avoid division by 0
							count = 1.0
			end = time.time()
		#now, decide for test data: set scores, measure accuracy of guesses
		num_correct_test = 0.0
		count_test = 0.1
		years_measured = len(crimedata[x]['data'])
		for n in range (0, years_measured):
			data = set_score(crimedata[x]['data'][n])
			if ((data['score']  > 0.0 and data['year'] < 1986) or
				(data['score'] <= 0.0 and data['year'] >= 1986)):
				wrong_years.append(data['year'])
			else:
				num_correct_test += 1.0
			count_test += 1.0
			total += 1.0
			if (count_test == 1.1): # gets rid of the .1 at the end of count_test which was originally there to avoid division by 0
				count_test = 1.0
		print num_correct_test / count_test
print wrong_years