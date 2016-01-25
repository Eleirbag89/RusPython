# coding: latin-1
# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.
# -----------------------------------------------------------------------------

import ply.yacc as yacc
import ruspylex
import ruspyparser
import util
import sys

def main(argv=None):
	if argv is None:
		argv = sys.argv
	debug = False
	if argv[1] == "-d":
		debug = True
		argv.remove("-d")
	try:
		in_file = open(argv[1],"r")
		s = in_file.read()
		in_file.close()
		#s = raw_input('calc > ')   # use input() on Python 3
	except EOFError:
		print("Eccezione")
	
	params = argv[2:]
	header=util.addInputParamers(params)
	s = util.caseInsensitivize(s)		
	util.first_pass(s)
	modu = header + ruspyparser.parse(s)
	if debug:
		print "Programma"
		print modu
		print "Execution"
	exec(compile(modu, filename="<string>", mode="exec"))
	if debug:
		print "END"

if __name__ == "__main__":
    main()
