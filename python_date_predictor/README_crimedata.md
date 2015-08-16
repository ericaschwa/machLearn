This program exhibits machine learning by reading in crime data by year, and based on correct examples, predicts
whether a given set of crime data occurred before or after the mean year from the data set (1987).

To run: python "date_predictor.py"

This program is 80% accurate when presented new data, and takes a relatively long amount of time (5 minutes)
to do this, because the data set is large and because the standard for accuracy is relatively high considering
the fact that crime data alone can not perfectly predict a year.

As it currently stands, the program takes in data for all 50 states over a time span of 50 years. For each state, predicts each year using all other years' data structures, and prints the accuracy with which it made these predictions. Also, at the end of the analysis, prints out the total set of all years that it predicted wrongly.

Most inaccuracies in this program are centered around the mean year in the data set, which is to be expected.
The mistakes of this program plotted on a frequency table by year form a bell curve centered around that year.
