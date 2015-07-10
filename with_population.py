import json
import sys

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

#alters the weights
def adjust_weights (data, weights):
	for val in averages:
	 	if (data[val] > averages[val]):
			if (data['score'] > 0):
				weights[val] -= 1.0
	 		else:
	 			weights[val] += 1.0
	return

#alters the data
def set_score (data):
	data['score'] = 0;
	for val in weights:
	 	data['score'] += data[val] * weights[val]
	return data

#calculate averages
def calculate_averages():
	averages = {'population':0.0,'index':0.0,'violent':0.0,'property':0.0,
				'murder':0.0,'forcible rape':0.0,'robbery':0.0,
				'aggravated assault':0.0,'burglary': 0.0,'larceny theft':0.0,
				'vehicle theft':0}
	scores = {'population':0.0,'index':0.0,'violent':0.0,'property':0.0,
				'murder':0.0,'forcible rape':0.0,'robbery':0.0,
				'aggravated assault':0.0,'burglary': 0.0,'larceny theft':0.0,
				'vehicle theft':0}
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


###############################################################################
#									MAIN									  #
###############################################################################

#open file containing data json
with open('crimedata.json', 'r') as f:
     read_data = f.read()
     crimedata = json.loads(read_data)
f.closed

#initialize weights
weights = {"population":0.0,"index":0.0,"violent":0.0,"property":0.0,
		   "murder":0.0,"forcible rape":0.0,"robbery":0.0,
		   "aggravated assault":0.0,"burglary":0.0,"larceny theft":0.0,
		   "vehicle theft":0.0}


averages = calculate_averages()

#adjust weights
# all_correct = 0
# while (all_correct == 0):
# 	all_correct = 1
num_correct = 0.0;
count = 0.0;
for k in range (0,2000):
	for i in range (0, 50):
		years_measured = len(crimedata[i]['data'])
		for j in range(0, years_measured):
			data = set_score(crimedata[i]['data'][j])
			if ((data['score']  > 0 and data['year'] < 1987) or
				(data['score'] <= 0 and data['year'] >= 1987)):
				#all_correct = 0
				adjust_weights(data, weights)
			else:
				num_correct += 1
			count += 1
print num_correct / count
print weights
