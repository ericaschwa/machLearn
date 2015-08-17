#########################################################################################################################
#																														#
# 						This program is a virtual calculator. Calculates user's math expressionsself. 					#
#					User presses enter when done typing expression; enters Q when done using calculator.				#
#					Each component must be separated from others by a space, except for	parentheses.					#
#																														#
#########################################################################################################################

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################


#TODO: PEMDAS

# global variable representing the stack containing various parts of the expression, ordered according to parentheses
expressionStack = []

# carries out function of calculator for one-line calculation, taking parentheses into account.
# Calculations can build upon previous calculations.
def calculate (expression):
	parenthStack = []
	for val in expression:
		if (val == "("):
			parenthStack.append(val)
			expressionStack.append("")
		elif (val == ")"):
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
				return 1
		else:
			if (len(expressionStack) > 0):
				top = expressionStack.pop()
			else:
				top = ""
			top += val
			expressionStack.append(top)
	if (len(parenthStack) != 0):
		print "Error: parentheses do not match up"
		return 1
	if (len(expressionStack) > 0):
		top = expressionStack.pop()
	else:
		top = ""
	top = evaluate(top)
	expressionStack.append(top + " ")
	print top

# evaluates an expression within a parentheses set
def evaluate (expression):
	parts = expression.split(" ")
	if (len(parts) < 3):
		return expression
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
		'^': str(pow(float(a), float(b))), #first
		'%': str(float(a) % float(b)), #second
	}[exp]

###############################################################################
#									MAIN									  #
###############################################################################

# Get user-inputted math expression
user_input = raw_input()
while (user_input != "Q"):
	calculate(user_input)
	user_input = raw_input()
