This program exhibits machine learning by reading in crime data by year, and based on correct examples, predicts
whether a given set of crime data occurred before or after the mean year from the data set (1987).

To run: python "date_predictor.py"

This program is 80% accurate when presented new data, and takes a relatively long amount of time (5 minutes)
to do this, because the data set is large and because the standard for accuracy is relatively high considering
the fact that crime data alone can not perfectly predict a year.

Most inaccuracies in this program are centered around the mean year in the data set, which is to be expected.
The mistakes of this program plotted on a frequency table by year form a bell curve centered around that year.
