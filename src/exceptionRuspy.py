def no_var_found(varName, line):
	print("Undeclared immigrant "+varName.rstrip()+" on line "+str(line))
	exit()

def no_input_found(varName, line):
	print("No immigrant "+varName.rstrip()+" on the frontier of line "+str(line))
	exit()

def no_freedom_Padania():
	print("Syntax error: No freedom for Padania")
	exit()
