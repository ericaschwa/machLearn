import json
import sys

def adjust_weights (data, weights):
	#print data
	return

def set_year_score (data):
	print data
	return

#calculate averages
def calculate_averages():
	population_score = 0.0
	index_score = 0.0
	violent_score = 0.0	
	property_score = 0.0
	murder_score = 0.0
	fr_score = 0.0
	robbery_score = 0.0
	aa_score = 0.0
	burglary_score = 0.0
	lt_score = 0.0
	vt_score = 0.0
	count = 0.0
	for i in range (0, 50):
		years_measured = len(crimedata[i]['data'])
		for j in range(0, years_measured):
			population_score += weights['population'] * crimedata[i]['data'][j]['population']
			index_score += weights['index'] * crimedata[i]['data'][j]['index']
			violent_score += weights['violent'] * crimedata[i]['data'][j]['violent']
			property_score += weights['property'] * crimedata[i]['data'][j]['property']
			murder_score += weights['murder'] * crimedata[i]['data'][j]['murder']
			fr_score += weights['forcible rape'] * crimedata[i]['data'][j]['forcible rape']
			robbery_score += weights['robbery'] * crimedata[i]['data'][j]['robbery']
			aa_score += weights['aggravated assault'] * crimedata[i]['data'][j]['aggravated assault']
			burglary_score += weights['burglary'] * crimedata[i]['data'][j]['burglary']
			lt_score += weights['larceny theft'] * crimedata[i]['data'][j]['larceny theft']
			vt_score += weights['vehicle theft'] * crimedata[i]['data'][j]['vehicle theft']
			count += 1
	population_avg = population_score / count
	index_avg = index_score / count
	violent_avg = violent_score / count
	property_avg = property_score / count
	murder_avg = murder_score / count
	fr_avg = fr_score / count
	robbery_avg = robbery_score / count
	aa_avg = aa_score / count
	burglary_avg = burglary_score / count
	lt_avg = lt_score / count
	vt_avg = vt_score / count
	return


#open file containing data json
with open('crimedata.json', 'r') as f:
     read_data = f.read()
     crimedata = json.loads(read_data)
f.closed

#initialize weights
weights = {"population":0.0,"index":0.0,"violent":0.0,"property":0.0,
			"murder":0.0,"forcible rape":0.0,"robbery":0.0,"aggravated assault":0.0,
			"burglary":0.0,"larceny theft":0.0,"vehicle theft":0.0}


calculate_averages()

#adjust weights
all_correct = 0
while (all_correct == 0):
	all_correct = 1
	for i in range (0, 50):
		years_measured = len(crimedata[i]['data'])
		for j in range(0, years_measured):
			if ((set_year_score(crimedata[i]['data'][j]) > 0 and crimedata[i]['data'][j]['year'] < 1987) or
				(set_year_score(crimedata[i]['data'][j]) <= 0 and crimedata[i]['data'][j]['year'] >= 1987)):
				#all_correct = 0
				adjust_weights(crimedata[i]['data'][j], weights)
print weights



			# if (set_year_score(crimedata[i]['data'][j]) > 0 && crimedata[i]['data'][j]['year'] < 1987):
			# 	#weights too high for things above avg
			# else if (set_year_score(crimedata[i]['data'][j]) <= 0 && crimedata[i]['data'][j]['year'] >= 1987):
			# 	#weights too low for things above avg



#   state name: crimedata[i]['name'] i is between 0 and 49
#   data: crimedata[i]['data']
#   jth year: crimedata[i]['data'][j]['year']... j is between 0 and 54
#   


# whether the score is less than or greater than the average - adjust weights based on that!!!!!!