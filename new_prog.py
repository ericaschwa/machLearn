import json
import sys
import math

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

# adjust the weights in response to an incorrect answer; alters the weights
def adjust_weights (data, weights, averages, stdevs):
	for val in averages:
	 	# if (data[val] > averages[val] and
	 	# 	data[val] < averages[val] + stdevs[val]*3):
		if (data[val] > averages[val]):
			if (data['score'] > 0):
				weights[val] -= 1.0
	 		else:
	 			weights[val] += 1.0
	 	# if (data[val] > averages[val] + stdevs[val]*3):
	 	# 	print data[val]
	 	# 	print averages[val] + stdevs[val]*2
	return

# set score which will be used to classify the year of the data; alters the data
def set_score (data):
	data['score'] = 0;
	for val in weights:
	 	data['score'] += data[val] * weights[val]
	return data

#calculate averages of different values
def calculate_averages():
	averages = {"index":0.0,"violent":0.0,"property":0.0,"murder":0.0,
		   		"forcible rape":0.0,"robbery":0.0, "aggravated assault":0.0,
		   		"burglary":0.0,"larceny theft":0.0,"vehicle theft":0.0}
	scores = {"index":0.0,"violent":0.0,"property":0.0,"murder":0.0,
		   	  "forcible rape":0.0,"robbery":0.0, "aggravated assault":0.0,
		   	  "burglary":0.0,"larceny theft":0.0,"vehicle theft":0.0}
	count = 0.0
	for i in range (0, 40):
		years_measured = len(crimedata[i]['data'])
		for j in range(0, years_measured):
			for val in scores:
				scores[val] += crimedata[i]['data'][j][val]
			count += 1
	for val in averages:
		averages[val] = scores[val]/count
	return averages

# calculate standard deviations of different values
def calculate_stdevs():
	stdevs = {"index":0.0,"violent":0.0,"property":0.0,"murder":0.0,
		   	  "forcible rape":0.0,"robbery":0.0, "aggravated assault":0.0,
		   	  "burglary":0.0,"larceny theft":0.0,"vehicle theft":0.0}
	count = 0  
	for val in averages:
		squared_diff_sum = 0
		for i in range (0, 50):
			years_measured = len(crimedata[i]['data'])
			for j in range(0, years_measured):
				squared_diff_sum += (crimedata[i]['data'][j][val] - averages[val]) * (crimedata[i]['data'][j][val] - averages[val])
				count += 1
		stdevs[val] = math.sqrt(squared_diff_sum / count)
	return stdevs



###############################################################################
#									MAIN									  #
###############################################################################

#open file containing data json
with open('crimedata.json', 'r') as f:
     read_data = f.read()
     crimedata = json.loads(read_data)
f.closed

#initialize weights and calculate averages
weights = {"index":0.0,"violent":0.0,"property":0.0,"murder":0.0,
		   "forcible rape":0.0,"robbery":0.0, "aggravated assault":0.0,
		   "burglary":0.0,"larceny theft":0.0,"vehicle theft":0.0}
averages = calculate_averages()
stdevs = calculate_stdevs()

#adjust weights until reaching statistical significance for accuracy
num_correct = 0.0
count = 1.0
while (num_correct / count < 0.9153): # not quite there yet... between 0.9153 and 0.916
	for i in range (0, 50):
		years_measured = len(crimedata[i]['data'])
		for j in range(0, years_measured):
			data = set_score(crimedata[i]['data'][j])
			if ((data['score']  > 0 and data['year'] < 1987) or
				(data['score'] <= 0 and data['year'] >= 1987)):
				adjust_weights(data, weights, averages, stdevs)
			else:
				num_correct += 1
			count += 1
print num_correct / count
print weights
