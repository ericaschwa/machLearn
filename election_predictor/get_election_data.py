#########################################################################################################################
#																														#
# 	This program reads in data structures containing crime and election data from JSON files and excels, combines		#
#						them into one JSON object, and prints this JSON object to a file.								#
#																														#
#########################################################################################################################

import json
import xlrd
from collections import OrderedDict

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

# get the election results by state and year (0 means republican; 1 means democrat)
# source: http://www.270towin.com/states/
def make_election_data():
	# Open the workbook
	wb = xlrd.open_workbook('elections.xlsx')
	sh = wb.sheet_by_index(0)

	elections_list = []

	# Iterate through each row in worksheet and fetch values into dict
	# add four years for each election result, since elections happen
	# every four years
	for rownum in range(1, sh.nrows):
		elections = OrderedDict()
		row_values = sh.row_values(rownum)
		elections['state'] = row_values[0]
		elections['year'] = int(row_values[1] - 3)
		elections['result'] = int(row_values[2])
		elections_list.append(elections)

		elections = OrderedDict()
		row_values = sh.row_values(rownum)
		elections['state'] = row_values[0]
		elections['year'] = int(row_values[1] - 2)
		elections['result'] = int(row_values[2])
		elections_list.append(elections)

		elections = OrderedDict()
		row_values = sh.row_values(rownum)
		elections['state'] = row_values[0]
		elections['year'] = int(row_values[1] - 1)
		elections['result'] = int(row_values[2])
		elections_list.append(elections)

		elections = OrderedDict()
		row_values = sh.row_values(rownum)
		elections['state'] = row_values[0]
		elections['year'] = int(row_values[1])
		elections['result'] = int(row_values[2])
		elections_list.append(elections)
		
	# Serialize the list of dicts to JSON
	j = json.dumps(elections_list)
	with open('electiondata.json', 'w') as f:
	    	f.write(j)
	f.closed


# get election data by state and year
def get_election_data():
	#open file containing sample data json
	with open('electiondata.json', 'r') as f: # to use file that includes the test data (accuracy: 0.962962962963)
	     read_data = f.read()
	     electiondata = json.loads(read_data)
	f.closed
	return electiondata

# get crime data by state and year
def get_crime_data():
	#open file containing sample data json
	with open('crimedata.json', 'r') as f: # to use file that includes the test data (accuracy: 0.962962962963)
	     read_data = f.read()
	     crimedata = json.loads(read_data)
	f.closed
	return crimedata

# combines the election data and the crime data into one structure
def combine_structures(elections, crimedata):
	data = []
	for x in range(0, len(crimedata)): # for each state
		for y in range(0, len(crimedata[x]['data'])): # for each year in that state
			if (crimedata[x]['data'][y]['year'] >= 1973 and crimedata[x]['data'][y]['year'] <= 2012 and crimedata[x]['name'] != 'USA'):
				for i in range(0,len(elections)):
					if (elections[i]['state'] == crimedata[x]['name'] and elections[i]['year'] == crimedata[x]['data'][y]['year']):
						dataPt = {"result": 			elections[i]['result'],
								  "index":				crimedata[x]['data'][y]['index'],
								  "violent":			crimedata[x]['data'][y]['violent'],
								  "property":			crimedata[x]['data'][y]['property'],
								  "murder":				crimedata[x]['data'][y]['murder'],
								  "forcible rape":		crimedata[x]['data'][y]['forcible rape'],
								  "robbery":			crimedata[x]['data'][y]['robbery'],
								  "aggravated assault":	crimedata[x]['data'][y]['aggravated assault'],
								  "burglary":			crimedata[x]['data'][y]['burglary'],
								  "larceny theft":		crimedata[x]['data'][y]['larceny theft'],
								  "vehicle theft":		crimedata[x]['data'][y]['vehicle theft'],
								  "state": 				elections[i]['state'],
								  "year": 				elections[i]['year']}
						data.append(dataPt)
						break
	return data

###############################################################################
#									MAIN									  #
###############################################################################

make_election_data()
elections = get_election_data()
crimedata = get_crime_data()
data = combine_structures(elections, crimedata)
j = json.dumps(data)
with open('data.json', 'w') as f:
	    	f.write(j)
f.closed

