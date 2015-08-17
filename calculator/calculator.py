#########################################################################################################################
#																														#
# 						This program is a virtual calculator. Calculates user's math expressionsself. 					#
#					User presses enter when done typing expression; enters Q when done using calculator.				#
#					Each component must be separated from others by a space, except for	parentheses.					#
#																														#
#########################################################################################################################

import math

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

# carries out function of calculator for one-line calculation, taking parentheses into account.
# Calculations can build upon previous calculations.
def calculate (expression, expressionStack):
	parenthStack = []
	if (not(expression[0] == '^' or expression[0] == '*' or expression[0] == '/' or expression[0] == '%' or expression[0] == '+' or expression[0] == '-')):
		expressionStack = [] # start fresh with new stack
	for val in expression:
		if (val == "("): # start of a parenthesized statement
			parenthStack.append(val)
			expressionStack.append("")
		elif (val == ")"): # end of a parenthesized statement; evaluate the statement and push the result back to the stack
			if (len(parenthStack) > 0):
				parenthStack.pop()
				prev = expressionStack.pop()
				prev = evaluate(prev)
				if (len(expressionStack) > 0):
					top = expressionStack.pop()
				else:
					top = ""
				top += prev
				expressionStack.append(top)
			else:
				print "Error: parentheses do not match up"
				return []
		else: # non-parenthesis value added; push it to the stack
			if (len(expressionStack) > 0):
				top = expressionStack.pop()
			else:
				top = ""
			top += val
			expressionStack.append(top)
	if (len(parenthStack) != 0):
		print "Error: parentheses do not match up"
		return []
	if (len(expressionStack) > 0):
		top = expressionStack.pop()
	else:
		top = ""
	top = evaluate(top)
	expressionStack.append(top + " ")
	print top
	return expressionStack

# evaluates an expression within a parentheses set
def evaluate (expression):
	parts = expression.split(" ")
	if (len(parts) < 3):
		return expression

	# E in PEMDAS
	i = 0
	while (i < len(parts)):
		if (parts[i] == '^'):
			parts[i - 1] = str(math.pow(int(float(parts[i - 1])), int(float(parts[i + 1]))))
			parts.pop(i)
			parts.pop(i)
		i += 1

	# M and D in PEMDAS (and mod)
	i = 0
	while (i < len(parts)):
		if (parts[i] == '*'):
			parts[i - 1] = str(float(parts[i - 1]) * float(parts[i + 1]))
			parts.pop(i)
			parts.pop(i)
		elif (parts[i] == '/'):
			parts[i - 1] = str(float(parts[i - 1]) / float(parts[i + 1]))
			parts.pop(i)
			parts.pop(i)
		elif (parts[i] == '%'):
			parts[i - 1] = str(float(parts[i - 1]) % float(parts[i + 1]))
			parts.pop(i)
			parts.pop(i)
		i += 1

	# A and S in PEMDAS
	start = parts[0]
 	expIndex = 1
 	endIndex = 2
 	while (endIndex < len(parts) and expIndex < len(parts)):
 		exp = parts[expIndex]
 		end = parts[endIndex]
 		start = f(start, exp, end)
 		expIndex += 2
 		endIndex += 2
 	return start

# applies whatever operation user wanted (+ , -, *, /, ^, or %) to the numbers entered and returns the result
def f (a,exp,b):
 	return {
		'+': str(float(a) + float(b)), #third
		'-': str(float(a) - float(b)), #third
		'*': str(float(a) * float(b)), #second
		'/': str(float(a) / float(b)), #second
		'^': str(math.pow(int(float(a)), int(float(b)))), #first
		'%': str(float(a) % float(b)), #second
 	}[exp]

###############################################################################
#									MAIN									  #
###############################################################################

# Get user-inputted math expression
user_input = raw_input()
expressionStack = []
while (user_input != "Q"):
	expressionStack = calculate(user_input, expressionStack)
	user_input = raw_input()
