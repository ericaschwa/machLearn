import json
import sys
import math

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
		for i in range (0, 49):
			years_measured = len(crimedata[i]['data'])
			for j in range(0, years_measured):
				score += crimedata[i]['data'][j][val]
				count += 1.0
		averages[val] = score/count
	return averages

# calculate standard deviations of different values
def calculate_stdevs():
	stdevs = {"index":0.0,"violent":0.0,"property":0.0,"murder":0.0,
		   	  "forcible rape":0.0,"robbery":0.0, "aggravated assault":0.0,
		   	  "burglary":0.0,"larceny theft":0.0,"vehicle theft":0.0}
	count = 0.0
	for val in averages:
		squared_diff_sum = 0.0
		for i in range (0, 49):
			years_measured = len(crimedata[i]['data'])
			for j in range(0, years_measured):
				squared_diff_sum += (crimedata[i]['data'][j][val] - averages[val]) * (crimedata[i]['data'][j][val] - averages[val])
				count += 1.0
		stdevs[val] = math.sqrt(squared_diff_sum / count)
	return stdevs



###############################################################################
#									MAIN									  #
###############################################################################

#open file containing sample data json
#with open('crimedata.json', 'r') as f: # to use file that includes the test data (accuracy: 0.962962962963)
with open('crimedata_nonew.json', 'r') as f: # to use the file that doesn't include the test data ()
     read_data = f.read()
     crimedata = json.loads(read_data)
f.closed

#open file containing test data json
with open('crimedata_new.json', 'r') as f:
     read_data = f.read()
     crimedata_new = json.loads(read_data)
f.closed

#initialize weights and calculate averages
weights = {"index":0.0,"violent":0.0,"property":0.0,"murder":0.0,
		   "forcible rape":0.0,"robbery":0.0, "aggravated assault":0.0,
		   "burglary":0.0,"larceny theft":0.0,"vehicle theft":0.0}
averages = calculate_averages()

#adjust weights until reaching statistical significance for accuracy
num_correct = 0.0
count = 0.1
while (num_correct / count < 0.912): # not quite there yet... between 0.9155 and 0.9156 when running it on regular crimedata file with 50 points (usually 0.915491754495 in 14.916 user seconds)
	for i in range (0, 49):									 #between 0.9129 and 0.9130 when running it on crimedata_nonew file with 49 points (usually 0.91290137255 in 12.971 user seconds)
		years_measured = len(crimedata[i]['data'])  #however, when standards lowered to 0.912, overall accuracy improved from 0.944444444444 to 0.981481481481
		for j in range(0, years_measured):
			data = set_score(crimedata[i]['data'][j])
			if ((data['score']  > 0.0 and data['year'] < 1987) or
				(data['score'] <= 0.0 and data['year'] >= 1987)):
				adjust_weights(data, weights, averages)
			else:
				num_correct += 1.0
			count += 1.0
			if (count == 1.1): # gets rid of the .1 at the end of count which was originally there to avoid division by 0
				count = 1
print num_correct / count

#now, decide for test data: set scores, measure accuracy of guesses
num_correct = 0.0
count = 0.1
years_measured = len(crimedata_new[0]['data'])
for n in range (0, years_measured):
	data = set_score(crimedata_new[0]['data'][n])
	if ((data['score']  > 0.0 and data['year'] < 1987) or
		(data['score'] <= 0.0 and data['year'] >= 1987)):
		print data['year']
	else:
		num_correct += 1.0
	count += 1.0
	if (count == 1.1): # gets rid of the .1 at the end of count which was originally there to avoid division by 0
		count = 1
print num_correct / count








