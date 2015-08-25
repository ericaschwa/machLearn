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
	for rownum in range(0, sh.nrows):
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

	energyData = []
	states  =  [
		'Alaska', 	   	 'Alabama', 	  'Arkansas',		'Arizona',
		'California',	 'Colorado',	  'Connecticut',    'Delaware',
		'Florida',		 'Georgia',	   	  'Hawaii',		    'Iowa',
		'Idaho',		 'Illinois',	  'Indiana',		'Kansas',
		'Kentucky',	   	 'Louisiana',	  'Massachusetts',  'Maryland',
		'Maine',		 'Michigan',	  'Minnesota',	    'Missouri',
		'Mississippi',   'Montana',	   	  'North Carolina', 'North Dakota',
		'Nebraska',	  	 'New Hampshire', 'New Jersey',	    'New Mexico',
		'Nevada',		 'New York',	  'Ohio',			'Oklahoma',
		'Oregon',		 'Pennsylvania',  'Rhode Island',	'South Carolina',
		'South Dakota',	 'Tennessee',	  'Texas',		    'Utah',
		'Virginia',		 'Vermont',	   	  'Washington',	    'Wisconson',
	 	'West Virginia', 'Wyoming'
	]

	# Iterate through each row in worksheet and fetch values into dict
	for year in range (1990, 2014):
		for state in states:
			# get data for each state in each year
			energy = OrderedDict()
			energy['state'] = state
			energy['year'] = year
			energy['coal'] = 0.0
			energy['hydro'] = 0.0
			energy['natural gas'] = 0.0
			energy['petroleum'] = 0.0
			energy['wind'] = 0.0
			energy['wood'] = 0.0
			energy['nuclear'] = 0.0
			energy['biomass'] = 0.0
			energy['other gas'] = 0.0
			energy['geothermal'] = 0.0
			energy['pumped storage'] = 0.0
			energy['solar'] = 0.0

			# get data for each type of energy
			for rownum in range(0, sh.nrows):
				row_values = sh.row_values(rownum)
				if (row_values[1] == state and int(row_values[0]) == year):
					if (row_values[3] == 'Coal'):
						energy['coal'] += row_values[4]
					elif (row_values[3] == 'Hydroelectric Conventional'):
						energy['hydro'] += row_values[4]
					elif (row_values[3] == 'Natural Gas'):
						energy['natural gas'] += row_values[4]
					elif (row_values[3] == 'Petroleum'):
						energy['petroleum'] += row_values[4]
					elif (row_values[3] == 'Wind'):
						energy['wind'] += row_values[4]
					elif (row_values[3] == 'Wood and Wood Derived Fuels'):
						energy['wood'] += row_values[4]
					elif (row_values[3] == 'Nucelear'):
						energy['nuclear'] += row_values[4]
					elif (row_values[3] == 'Other Biomass'):
						energy['biomass'] += row_values[4]
					elif (row_values[3] == 'Other Gases'):
						energy['other gas'] += row_values[4]
					elif (row_values[3] == 'Geothermal'):
						energy['geothermal'] += row_values[4]
					elif (row_values[3] == 'Pumped Storage'):
						energy['pumped storage'] += row_values[4]
					elif (row_values[3] == 'Solar Thermal and Photovoltaic'):
						energy['solar'] += row_values[4]

			energyData.append(energy)
	
	#Serialize the list of dicts to JSON
	j = json.dumps(energyData)
	with open('energydata.json', 'w') as f:
	    	f.write(j)
	f.closed

# get the median income in 2013 by state and year
# source: https://www.census.gov/hhes/www/income/data/statemedian/
def make_income_data():
	# Open the workbook
	wb = xlrd.open_workbook('income.xls')
	sh = wb.sheet_by_index(0)

	incomeData = []

	# Iterate through each row in worksheet and fetch values into dict
	for rownum in range(0, sh.nrows):
		row_values = sh.row_values(rownum)
		for colnum in range(0, 24):
			data = OrderedDict()
			data['state'] = row_values[0]
			data['year'] = 2013 - colnum
			data['income'] = row_values[2 * colnum + 1]
			data['income stderr'] = row_values[2 * colnum + 2]
			incomeData.append(data)
	
	#Serialize the list of dicts to JSON
	j = json.dumps(incomeData)
	with open('incomedata.json', 'w') as f:
	    	f.write(j)
	f.closed

# get the 1900 population in each state
# source: http://www.census.gov/popest/data/historical/1990s/index.html
def make_popchange_data():
	# Open the workbook
	wb = xlrd.open_workbook('1900_populations.xlsx')
	sh = wb.sheet_by_index(0)

	popData = []

	# Iterate through each row in worksheet and fetch values into dict
	for rownum in range(0, sh.nrows):
		row_values = sh.row_values(rownum)
		data = OrderedDict()
		data['state'] = row_values[0]
		data['1900 pop'] = row_values[1]
		popData.append(data)
	
	#Serialize the list of dicts to JSON
	j = json.dumps(popData)
	with open('populationdata.json', 'w') as f:
	    	f.write(j)
	f.closed

# get election data by state and year
def get_election_data():
	#open file containing data json
	with open('electiondata.json', 'r') as f: 
	     read_data = f.read()
	     electiondata = json.loads(read_data)
	f.closed
	return electiondata

# get energy data by state and year
def get_energy_data():
	#open file containing data json
	# to use file that includes the test data
	with open('energydata.json', 'r') as f:
	     read_data = f.read()
	     energyData = json.loads(read_data)
	f.closed
	return energyData

# get income data by state and year
def get_income_data():
	#open file containing data json
	# to use file that includes the test data
	with open('incomedata.json', 'r') as f:
	     read_data = f.read()
	     incomeData = json.loads(read_data)
	f.closed
	return incomeData

# get 1900s population data by state
def get_popchange_data():
	#open file containing data json
	# to use file that includes the test data (accuracy: 0.962962962963)
	with open('populationdata.json', 'r') as f:
	     read_data = f.read()
	     popdata = json.loads(read_data)
	f.closed
	return popdata

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
def combine_crimes(elections, crimedata):
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
							"population":			this['population'],
							"state": 				elections[i]['state'],
							"year": 				elections[i]['year'],
							"prev":					elections[i]['prev']
						}
						data.append(dataPt)
						break
	return data

# combines the energy data and the election/crime data into one structure
def combine_energy(crimedata, energyData):
	data = []
	for x in range(0, len(crimedata)): # for each state
		if (crimedata[x]['year'] >= 1990 and crimedata[x]['year'] <= 2012):
			for i in range(0,len(energyData)):
				if (energyData[i]['state'] == crimedata[x]['state'] and
					energyData[i]['year'] == crimedata[x]['year']):
					crime = crimedata[x]
					energy = energyData[i]
					dataPt = {
						"result": 				crime['result'],
						"index":				crime['index'],
						"violent":				crime['violent'],
						"property":				crime['property'],
						"murder":				crime['murder'],
						"forcible rape":		crime['forcible rape'],
						"robbery":				crime['robbery'],
						"aggravated assault": 	crime['aggravated assault'],
						"burglary":				crime['burglary'],
						"larceny theft":		crime['larceny theft'],
						"vehicle theft":		crime['vehicle theft'],
						"population":			crime['population'],
						"state": 				crime['state'],
						"year": 				crime['year'],
						"prev":					crime['prev'],
						"coal":					energy['coal'],
						"hydro":				energy['hydro'],
						"natural gas":			energy['natural gas'],
						"petroleum":			energy['petroleum'],
						"wind":					energy['wind'],
						"wood":					energy['wood'],
						"nuclear":				energy['nuclear'],
						"biomass":				energy['biomass'],
						"other gas":			energy['other gas'],
						"geothermal":			energy['geothermal'],
						"pumped storage":		energy['pumped storage'],
						"solar":				energy['solar']
					}
					data.append(dataPt)
					break
	return data

# combines the income data and the election/energy/crime data into one structure
def combine_income(crimedata, incomeData):
	data = []
	for x in range(0, len(crimedata)): # for each state
		for i in range(0,len(incomeData)):
			if (incomeData[i]['state'] == crimedata[x]['state'] and
				incomeData[i]['year'] == crimedata[x]['year']):
				crime = crimedata[x]
				income = incomeData[i]
				dataPt = {
					"result": 				crime['result'],
					"index":				crime['index'],
					"violent":				crime['violent'],
					"property":				crime['property'],
					"murder":				crime['murder'],
					"forcible rape":		crime['forcible rape'],
					"robbery":				crime['robbery'],
					"aggravated assault": 	crime['aggravated assault'],
					"burglary":				crime['burglary'],
					"larceny theft":		crime['larceny theft'],
					"vehicle theft":		crime['vehicle theft'],
					"population":			crime['population'],
					"state": 				crime['state'],
					"year": 				crime['year'],
					"prev":					crime['prev'],
					"coal":					crime['coal'],
					"hydro":				crime['hydro'],
					"natural gas":			crime['natural gas'],
					"petroleum":			crime['petroleum'],
					"wind":					crime['wind'],
					"wood":					crime['wood'],
					"nuclear":				crime['nuclear'],
					"biomass":				crime['biomass'],
					"other gas":			crime['other gas'],
					"geothermal":			crime['geothermal'],
					"pumped storage":		crime['pumped storage'],
					"solar":				crime['solar'],
					#"income":				income['income'],
					"income stderr":		income['income stderr']
				}
				data.append(dataPt)
				break
	return data

# combines the 1900s population data (will be used to calculate population
# change) and the election/income/energy/crime data into one structure
def combine_1900pop(crimedata, popdata):
	for data in crimedata:
		for state in popdata:
			if (data['state'] == state['state']):
				data['pop change'] = (data['population'] - state['1900 pop'])/state['1900 pop']
	return crimedata

###############################################################################
#									MAIN									  #
###############################################################################

make_election_data()
make_energy_data()
make_income_data()
make_popchange_data()
elections = get_election_data()
energyData = get_energy_data()
incomeData = get_income_data()
crimedata = get_crime_data()
popData = get_popchange_data()
data = combine_crimes(elections, crimedata)
data = combine_energy(data, energyData)
data = combine_income(data, incomeData)
data = combine_1900pop(data, popData)
j = json.dumps(data)
with open('data.json', 'w') as f:
	    	f.write(j)
f.closed

