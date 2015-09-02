###############################################################################
#																			  #
# 	This program lists the prime numbers up to a given number using			  #
#	the Seive of Eratosthenes algorithm. The user inputs this stopping		  #
#	point number on the command line. 										  #
#	User cannot input a negative number or a non-integer.				  	  #
#																			  #
###############################################################################

import math
import sys

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

# checks for any numbers in the array that are multiples of the "current"
# number. This does not include the number itself.
def check(current, arr):
	for val in arr:
		if (val["num"] != current and val["num"] % current == 0):
			val["prime"] = 0
	return arr

###############################################################################
#									MAIN									  #
###############################################################################

# get number to be checked and find its square root
number = int(sys.argv[1])
sqrt = math.sqrt(float(number))

# number we will start with when looking for multiples
current = 2.0

# initialize array containing numbers 1 through the given number to default
# values (1 being never prime; all other values being prime, for now)
lst = range(1,number+1)
arr = []
for val in lst:
	arr.append({
		"num": val,
		"prime": 1
	})
arr[0]["prime"] = 0

# checks the array for each integer between 2 and the square root of the
# given number, seeing if it can find any multiples, and if so, marking those
# numbers as not prime
while (current < sqrt):
	arr = check(current, arr)
	current += 1

# display results
print arr
