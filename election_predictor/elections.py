###############################################################################
#                                                                              #
#     This program exhibits machine learning by reading in various pieces of       #
#    data by state and year, and based on correct examples, predicts the       #
#    outcome of the closest upcoming presidential election to that date in       #
#    that state.                                                                  #
#                                                                              #
#    Used crime data because that was the data available to me.                  #
#                                                                              #
#        Accuracy: 0.581837381204 without energy data                           #
#                  0.716528162512 with energy data                              #
#                  0.709141274238 with income data                               #
#                  0.736842105263 with just income stderr                       #
#                  0.722068328717 with population change data                   #
#                  0.722991689751 with minimum wage data                       #
#                                                                              #
#         Accuracy values and significance of the difference between these      #
#            values and a 50% accuracy (guessing)                              #
#            P value and statistical significance:                               #
#              The two-tailed P value is less than 0.0001                          #
#              By conventional criteria, this difference is considered to be       #
#            extremely statistically significant.                               #
#                                                                              #
#             (source: http://graphpad.com/quickcalcs/oneSampleT2/)              #
#                                                                              #
###############################################################################

import json
import sys
import math
import time

###############################################################################
#                             FUNCTION DEFINITIONS                              #
###############################################################################

# adjust the weights in response to an incorrect answer; alters the weights
def adjust_weights (data, weights, averages):
    for val in averages:
        if (data[val] > averages[val]):
            if (data['score'] > 0.0):
                weights[val] -= 1.0
             else:
                 weights[val] += 1.0
    return

# set score which will be used to classify the year of the data; alters the data
def set_score (data):
    data['score'] = 0.0
    for val in weights:
         data['score'] += data[val] * weights[val]
    return data

#calculate averages of different values
def calculate_averages():
    averages = {
        "index":0.0,           "violent":0.0,                 "property":0.0,
        "murder":0.0,           "forcible rape":0.0,        "robbery":0.0,
        "burglary":0.0,           "aggravated assault":0.0,   "larceny theft":0.0,
        "vehicle theft":0.0,   "year":0.0,                    "prev":0.0,
        "coal":0.0,            "hydro":0.0,                "natural gas":0.0,
        "petroleum":0.0,        "wind":0.0,                    "wood":0.0,
        "nuclear":0.0,            "biomass":0.0,                "other gas": 0.0,
        "geothermal":0.0,        "pumped storage":0.0,       "solar":0.0,
        "income stderr":0.0
    }
    for val in averages:
        count = 0.0
        score = 0.0
        for i in range (0, len(data)):
            score += data[i][val]
            count += 1.0
        averages[val] = score/count
    return averages

###############################################################################
#                                    MAIN                                      #
###############################################################################

#open file containing data json
with open('data.json', 'r') as f:
    read_data = f.read()
    data = json.loads(read_data)
f.closed

num_correct_test = 0.0
count_test = 0.1
for x in range (0, len(data)):
    #adjust weights until reaching certain time limit
    weights = {
        "index":0.0,           "violent":0.0,                 "property":0.0,
        "murder":0.0,           "forcible rape":0.0,        "robbery":0.0,
        "burglary":0.0,           "aggravated assault":0.0,   "larceny theft":0.0,
        "vehicle theft":0.0,   "year":0.0,                    "prev":0.0,
        "coal":0.0,            "hydro":0.0,                "natural gas":0.0,
        "petroleum":0.0,        "wind":0.0,                    "wood":0.0,
        "nuclear":0.0,            "biomass":0.0,                "other gas": 0.0,
        "geothermal":0.0,        "pumped storage":0.0,       "solar":0.0,
        "income stderr":0.0
    }
    averages = calculate_averages()
    start = time.time()
    end = time.time()

    while (end-start < .2): # only give each data item .5 seconds, or 1 second
    # measurements made before addition of income data:
    # .5 gives an accuracy of 0.716528162512,
    # while 1 gives an accuracy of 0.713758079409
        for i in range (0, len(data)):
            if (i != x):
                data[i] = set_score(data[i])
                if ((data[i]['score']  > 0.0 and data[i]['result'] == 0) or
                    (data[i]['score'] <= 0.0 and data[i]['result'] == 1)):
                    adjust_weights(data[i], weights, averages)
        end = time.time()

    #now, decide for test data: set scores, measure accuracy of guesses
    data[x] = set_score(data[x])
    if (not((data[x]['score']  > 0.0 and data[x]['result'] == 0) or
            (data[x]['score'] <= 0.0 and data[x]['result'] == 1))):
        num_correct_test += 1.0
    count_test += 1.0
    # gets rid of the .1 at the end of count
    # which was originally there to avoid division by 0
    if (count_test == 1.1):
        count_test = 1.0

print num_correct_test / count_test
