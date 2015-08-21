###############################################################################
#																		      #
# 	This program reads in data structures containing crime and election       #
#	data from JSON files and excels, combines them into one json		      #
#	object, and prints this JSON object to a file.						      #
#																			  #
#	Used crime data because that was the data available to me.				  #
#																			  #
###############################################################################

import json
import xlrd
from collections import OrderedDict

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

# get the election results by state and year
# (0 means republican; 1 means democrat)
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
		elections['prev'] = int(row_values[3])
		elections_list.append(elections)

		elections = OrderedDict()
		row_values = sh.row_values(rownum)
		elections['state'] = row_values[0]
		elections['year'] = int(row_values[1] - 2)
		elections['result'] = int(row_values[2])
		elections['prev'] = int(row_values[3])
		elections_list.append(elections)

		elections = OrderedDict()
		row_values = sh.row_values(rownum)
		elections['state'] = row_values[0]
		elections['year'] = int(row_values[1] - 1)
		elections['result'] = int(row_values[2])
		elections['prev'] = int(row_values[3])
		elections_list.append(elections)

		elections = OrderedDict()
		row_values = sh.row_values(rownum)
		elections['state'] = row_values[0]
		elections['year'] = int(row_values[1])
		elections['result'] = int(row_values[2])
		elections['prev'] = int(row_values[3])
		elections_list.append(elections)
		
	# Serialize the list of dicts to JSON
	j = json.dumps(elections_list)
	with open('electiondata.json', 'w') as f:
	    	f.write(j)
	f.closed

# get the energy production results by state and year
# source: http://www.eia.gov/electricity/data/state/
def make_energy_data():
	# Open the workbook
	wb = xlrd.open_workbook('annual_generation_state.xls')
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
		elections['prev'] = int(row_values[3])
		elections_list.append(elections)
		
	# Serialize the list of dicts to JSON
	j = json.dumps(elections_list)
	with open('energydata.json', 'w') as f:
	    	f.write(j)
	f.closed

# get financial data for each state by year, from excel files
# http://www.census.gov/prod/2011pubs/11statab/stlocgov.pdf
# http://www.census.gov/compendia/statab/2011/2011edition.html
# http://www.census.gov/compendia/statab/cats/state_local_govt_finances_employment/state_government_finances.html
# files in downloads folder
def make_state_data():
	return 0

# get election data by state and year
def get_election_data():
	#open file containing data json
	with open('electiondata.json', 'r') as f: 
	     read_data = f.read()
	     electiondata = json.loads(read_data)
	f.closed
	return electiondata

# get crime data by state and year
def get_crime_data():
	#open file containing data json
	# to use file that includes the test data (accuracy: 0.962962962963)
	with open('crimedata.json', 'r') as f:
	     read_data = f.read()
	     crimedata = json.loads(read_data)
	f.closed
	return crimedata

# combines the election data and the crime data into one structure
def combine_structures(elections, crimedata):
	data = []
	for x in range(0, len(crimedata)): # for each state
	 	# for each year in the state
		for y in range(0, len(crimedata[x]['data'])):
			if (crimedata[x]['data'][y]['year'] >= 1973 and
				crimedata[x]['data'][y]['year'] <= 2012 and
				crimedata[x]['name'] != 'USA'):
				for i in range(0,len(elections)):
					if (elections[i]['state'] == crimedata[x]['name'] and
						elections[i]['year'] ==
						crimedata[x]['data'][y]['year']):
						this = crimedata[x]['data'][y]
						dataPt = {
							"result": 				elections[i]['result'],
							"index":				this['index'],
							"violent":				this['violent'],
							"property":				this['property'],
							"murder":				this['murder'],
							"forcible rape":		this['forcible rape'],
							"robbery":				this['robbery'],
							"aggravated assault": 	this['aggravated assault'],
							"burglary":				this['burglary'],
							"larceny theft":		this['larceny theft'],
							"vehicle theft":		this['vehicle theft'],
							"state": 				elections[i]['state'],
							"year": 				elections[i]['year'],
							"prev":					elections[i]['prev']
						}
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

