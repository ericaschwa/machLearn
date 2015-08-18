#########################################################################################################################
#																														#
# 	This program exhibits machine learning by reading in various pieces of data by state and year, and based on 		#
#	correct examples, predicts the outcome of the closest upcoming presidential election to that date in that state.	#
#																														#
#########################################################################################################################

import xlrd
from collections import OrderedDict
import json

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

# get the election results by state and year (0 means republican; 1 means democrat)
# source: http://www.270towin.com/states/
def save_election_data():
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

def combine_structures(elections, crimedata):
	data = []
	state_num = len(crimedata)
	for x in range(0, state_num):
		if (crimedata[x]['data'] != []):
			years_measured = len(crimedata[x]['data'])
			for y in range(0, years_measured):
				if (crimedata[x]['data'][y]['year'] >= 1973 and crimedata[x]['data'][y]['year'] <= 2012 and crimedata[x]['name'] != 'USA'):
					state = crimedata[x]['name']
					years = []
					for i in range(0,len(elections)):
						if (elections[i]['state'] == state and elections[i]['year'] == crimedata[x]['data'][y]['year']):
							print elections[i]
							print crimedata[x]['data'][y]
		
					
					


###############################################################################
#									MAIN									  #
###############################################################################
save_election_data()
elections = get_election_data()
crimedata = get_crime_data()
data = combine_structures(elections, crimedata)
