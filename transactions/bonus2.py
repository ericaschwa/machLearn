def solution(S):
    lines = S.split('/n')
    return process_file (lines, 0)

def process_file(lines, index):
    if index > len(lines) - 1:
        return 0
    elif len(lines[index].split('.')) > 1:
        return length_without_spaces(lines[index]) + 1
    elif index + 1 < len(lines):
        inner_count = process_file(lines, index+1)
         if num_spaces(lines[index+1]) > num_spaces(lines[index]):
            if inner_count > 0:
                return 1 + length_without_spaces(lines[index]) + inner_count
        else:
            return inner_count
    else:
        return 0

def num_spaces(string):
    return len(string.split(' ')) - 1

def length_without_spaces(string):
    return len((" " + string).split()[0])

print length_without_spaces("    lsdkd")
print num_spaces("    lsdkd")


###############################################################################
#                                                                              #
#     This program does not exhibit machine learning persay. Instead, it is an  #
#    attempt at the 2015 Mindsumo challenge. This module specifically focuses  #
#   on the second bonus challenge; the main challenge and the first bonus       #
#   challenge are dealt with in other modules. The question is as folows:      #
#                                                                              #
#    "Predict annual revenue for year 2015 (based on historical retention and  #
#    new subscribers)"                                                             #
#    (source: https://www.mindsumo.com/contests/credit-card-transactions)      #
#                                                                              #
###############################################################################

#import json
#import sys
#from bonus1 import organize

###############################################################################
#                             FUNCTION DEFINITIONS                              #
###############################################################################


###############################################################################
#                                    MAIN                                      #
###############################################################################

#open file containing data json
#with open('dataBonus.json', 'r') as f:
#    read_data = f.read()
#    data = json.loads(read_data)
#f.closed

#years = organize(data)

#print years


#print data[0]
