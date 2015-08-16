# the tricky part of this is the parenthesis (store in stack)
#########################################################################################################################
#																														#
# 						This program is a virtual calculator. Calculates user's math expressionsself. 					#
#					User presses enter when done typing expression; enters Q when done using calculator.				#
#					Each component must be separated from others by a space, except for	parentheses.					#
#																														#
#########################################################################################################################

# TODO: negatives
# TODO: order of ops other than parentheses

###############################################################################
#							 FUNCTION DEFINITIONS							  #
###############################################################################

parenthStack = []
expressionStack = []
# evaluate a user-entered expression
def calculate (expression):
	parenthStack = []
	expressionStack = []
	expressionString = ""
	for val in expression:
		if (val == "("):
			parenthStack.append(val)
			expressionStack.append(expressionString)
			expressionString = ""
		elif (val == ")"):
			if (len(parenthStack) > 0):
				parenthStack.pop()
				prev = expressionStack.pop()
				expressionString = prev + evaluate(expressionString)
				expressionString = evaluate(expressionString)
				expressionStack.append(expressionString)
			else:
				print "Error: parentheses do not match up"
				return 1
		else:
			expressionString += val
	if (len(parenthStack) != 0):
		print "Error: parentheses do not match up"
		return 1
	#print evaluate(expressionString)
	# print evaluate(expressionStack.pop())
	# if (len(expressionStack) > 0):
	# 	prev = expressionStack.pop()
	# 	expressionString = prev + evaluate(expressionString)
	# 	expressionString = evaluate(expressionString)
	# 	expressionStack.append(expressionString)

	print expressionStack
	print expressionString

	# while (len(expressionStack) > 1):
	# 	prev = evaluate(expressionStack.pop())
	# 	expressionStack.append(prev + expressionStack.pop())
	# print expressionStack

	return 0

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

def f (a,exp,b):
	return {
		'+': str(float(a) + float(b)),
		'-': str(float(a) - float(b)),
		'*': str(float(a) * float(b)),
		'/': str(float(a) / float(b)),
		'^': str(pow(float(a), float(b))),
		'%': str(float(a) % float(b)),
	}[exp]

###############################################################################
#									MAIN									  #
###############################################################################

# Get user-inputted math expression
user_input = raw_input()
while (user_input != "Q"):
	calculate(user_input)
	user_input = raw_input()
