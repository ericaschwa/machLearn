This program exhibits machine learning by reading in all types of data
(crime, election, energy use, income, population change, etc.) by year,
and based on correct examples, predicts whether a given state in a given
year voted democratic or republican.

To acquire data: python "get_election_data.py"
To run: python "elections.py"

This program is 73% accurate, and takes a relatively long amount of time
(15 minutes) to do this, because the data set is large and because the
standard for accuracy is relatively high considering
the fact that this data is not sufficient to truly predict an election.
When held to 4 minutes, the program's accuracy drops to 70%.

As it currently stands, the program takes in data for all 50 states
over a time span of 25 years. For each year in each state, predicts
each year using all other state-years' data structures. At the end
of the analysis, prints out its accuracy.
