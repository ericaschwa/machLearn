###############################################################################
#																			  #
# 	This program lists the prime numbers up to a given number using			  #
#	the Seive of Eratosthenes algorithm. The user inputs this stopping		  #
#	point number on the command line. 										  #
#	User cannot input a negative numbe or a non-integer.				  	  #
#																			  #
###############################################################################

import math
import sys

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

def check(current, arr):
	return arr

###############################################################################
#									MAIN									  #
###############################################################################


number = int(sys.argv[1])
sqrt = math.sqrt(float(number))
current = 0.0
lst = range(1,number+1)
arr = []

for val in lst:
	arr.append({
		"num": val,
		"prime": 1
	})


while (current < sqrt):
	arr = check(current, arr)
	current += 1

print arr