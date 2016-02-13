# coding: latin-1
from ply import *
import ruspylex
import exceptionRuspy

# Precedence rules for the arithmetic operators

tokens = ruspylex.tokens
precedence = (
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('right','UMINUS'),
	)

# dictionary of names (for storing variables)
names = { }
variable_counter=[0]
variable_counter[0]=0

def p_program_statements(p):
	'program : statements PADANIALIBERA'
	p[0] = p[1]

def p_program_statements_bad(p):
	'program : statements'
	exceptionRuspy.no_freedom_Padania()
	

def p_statements_statement(p):
	'statements : statement statements'
	tmp = p[1]
	if p[2] != "":
		tmp = str(tmp)+"\n"+str(p[2])
	p[0] = tmp
	
def p_statements_empty_statement(p):
	'statements : empty_statement'
	p[0] = ""
	
def p_statement_empty(p):
    'empty_statement :'
    p[0] = ""
    
def p_statement_expression(p):
	'statement : expression'
	p[0] = p[1]
	
def p_statement_function(p):
	'statement : ATTENZIONE variable ESCLAMATION_POINT params end_params statements BASTA'
	tmp = "global "+str(p[2]).rstrip().replace(" ", "_")+"\n"
	tmp = tmp + "def "+str(p[2]).rstrip().replace(" ", "_")+"("+p[4]+"):"
	substm = str(p[6]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	p[0] = tmp

def p_statement_function_invoke(p):
	'expression : RICORDATE variable ESCLAMATION_POINT params_actual A CASA LORO'
	tmp = str(p[2]).rstrip().replace(" ", "_")+"("+p[4]+")"
	p[0] = tmp

def p_statement_function_thread(p):
	'''expression : MANDIAMO variable A LAVORARE CON params_actual ESCLAMATION_POINT
				  | MANDIAMO variable A LAVORARE ESCLAMATION_POINT'''
	tmp = "import thread\n"
	if len(p) > 6:
		tmp = tmp + "thread.start_new_thread("+str(p[2]).rstrip().replace(" ", "_")+",("+p[6]+",))"
	else:
		tmp = tmp + "thread.start_new_thread("+str(p[2]).rstrip().replace(" ", "_")+",())"
	p[0] = tmp
	
def p_function_end_params(p):
	'end_params : TORNINO A CASA LORO'
	p[0] = ""

def p_function_params(p):
	'''params : variable E params
			  | variable
			  |'''
	varName = ""
	if len(p) == 1:
		p[0] = ""
	else:
		try:
			varName = names[p[1]] 
		except KeyError:
			names[p[1]] = "fun"+str(variable_counter[0])
			variable_counter[0] = variable_counter[0]+1
			varName = names[p[1]]
		if len(p) < 3:
			p[0] = varName.rstrip()
		else:
			p[0] = varName.rstrip()+","+str(p[3]).rstrip()

def p_function_params_actual(p):
	'''params_actual : expression E params_actual
			  | expression
			  |'''
	if len(p) == 1:
		p[0] = ""
	else:
		if len(p) < 3:
			p[0] = str(p[1]).rstrip()
		else:
			p[0] = str(p[1]).rstrip()+","+str(p[3]).rstrip()
	
def p_statement_return(p):
	'''statement : ESPELLI statement
				 | ESPELLILI statement'''
	p[0] = "return " + str(p[2]) 
	
def p_statement_assign(p):
	'''statement : variable EQUALS expression
				 | variable SONO expression'''
	varName = ""
	try:
		varName = names[p[1]] 
	except KeyError:
		names[p[1]] = "var"+str(variable_counter[0])
		variable_counter[0] = variable_counter[0]+1
		varName = names[p[1]]
	p[0] = str(varName) + "=" + str(p[3]) 
	
def p_statement_open_file_read(p):
	'expression : LEGGERMENTE expression'
	p[0] = "open("+p[2]+", 'r')"
	
def p_statement_read_all_file(p):
	'expression : expression INFAME'
	p[0] = p[1]+".read()"

def p_statement_assign_socket(p):
	'statement : variable EQUALS SPIONE'
	varName = ""
	try:
		varName = names[p[1]] 
	except KeyError:
		names[p[1]] = "var"+str(variable_counter[0])
		variable_counter[0] = variable_counter[0]+1
		varName = names[p[1]]
	p[0] = str(varName) + "= socket.socket(socket.AF_INET, socket.SOCK_STREAM)" 

def p_expression_bind_socket(p):
	'expression : statement AMA expression E ODIA expression'
	p[0] = str(p[1]) +".bind(("+p[3]+","+p[6]+"))"
	
def p_expression_listen_socket(p):
	'expression : statement ASCOLTA A expression'
	p[0] = str(p[1]) +".listen("+p[4]+")"

def p_expression_receive_socket(p):
	'expression : statement CHE REGALA expression EURI'
	p[0] = str(p[1]) +".recv("+p[4]+")"
	
def p_expression_sendall_socket(p):
	'expression : DICO A statement DPOINT expression ESCLAMATION_POINT'
	p[0] = str(p[3]) +".sendall("+p[5]+")"

def p_expression_close_socket(p):
	'expression : UCCIDIAMO statement ESCLAMATION_POINT'
	p[0] = str(p[2]) +".close()"
	
def p_expression_accept_socket(p):
	'expression : RIFIUTIAMO statement ESCLAMATION_POINT'
	p[0] = str(p[2]) +".accept()"
	
def p_statement_if(p):
	'''expression : variable EQUALS expression QUESTION_MARK statements POINT
				  | variable SONO expression QUESTION_MARK statements POINT
				  | variable MINORE expression QUESTION_MARK statements POINT
				  | variable MAGGIORE expression QUESTION_MARK statements POINT'''
	try:
		if p[2] == "minore":
			tmp = "if "+str(names[p[1]])+" < "+str(p[3])+":"
		elif p[2] == "maggiore":
			tmp = "if "+str(names[p[1]])+" > "+str(p[3])+":"
		else:
			tmp = "if "+str(names[p[1]])+" == "+str(p[3])+":"
	except:
		var_or_input(p[1], p.lineno(1))
	substm = str(p[5]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	p[0] = tmp
	
def p_statement_if_file(p):
	'expression : ESISTE expression QUESTION_MARK statements POINT'

	tmp = "import os.path\nif os.path.exists("+str(p[2])+"):"
	substm = str(p[4]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	p[0] = tmp
	
def p_statement_if_dir(p):
	'expression : CARTELLA expression QUESTION_MARK statements POINT'

	tmp = "import os.path\nif os.path.isdir("+str(p[2])+"):"
	substm = str(p[4]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	p[0] = tmp

def p_expression_string(p):
	'expression : DQUOTE variable DQUOTE'
	p[0] = "\""+str(p[2]).rstrip()+"\""

def p_statement_if_else(p):
	'''expression : variable EQUALS expression QUESTION_MARK statements ALTRIMENTI statements POINT
				  | variable SONO expression QUESTION_MARK statements ALTRIMENTI statements POINT
				  | variable MINORE expression QUESTION_MARK statements ALTRIMENTI statements POINT
				  | variable MAGGIORE expression QUESTION_MARK statements ALTRIMENTI statements POINT'''
	try:
		if p[2] == "minore":
			tmp = "if "+str(names[p[1]])+" < "+str(p[3])+":"
		elif p[2] == "maggiore":
			tmp = "if "+str(names[p[1]])+" > "+str(p[3])+":"
		else:
			tmp = "if "+str(names[p[1]])+" == "+str(p[3])+":"
	except:
		var_or_input(p[1], p.lineno(1))
	substm = str(p[5]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	tmp = tmp + "\nelse:"
	substm = str(p[7]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	p[0] = tmp
	
def p_statement_if_else_file(p):
	'expression : ESISTE expression QUESTION_MARK statements ALTRIMENTI statements POINT'
	tmp = "import os.path\nif os.path.exists("+str(p[2])+"):"
	substm = str(p[4]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	tmp = tmp + "\nelse:"
	substm = str(p[6]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	p[0] = tmp
	
def p_statement_if_else_dir(p):
	'expression : CARTELLA expression QUESTION_MARK statements ALTRIMENTI statements POINT'
	tmp = "import os.path\nif os.path.isdir("+str(p[2])+"):"
	substm = str(p[4]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	tmp = tmp + "\nelse:"
	substm = str(p[6]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	p[0] = tmp

def p_statement_urla(p):
	'statement : URLA expression'
	p[0] = "print "+str(p[2])
	
def p_statement_finche_minore(p):
	'''statement : FINCHE variable MINORE expression SEMICOLON statements POINT
				 | FINCHE variable MAGGIORE expression SEMICOLON statements POINT
				 | FINCHE variable UGUALE expression SEMICOLON statements POINT'''
	op = ""
	if p[3] == "minore":
		op = " < "
	elif p[3] == " maggiore ":
		op = ">"
	elif p[3] == "uguale":
		op = " == "
	tmp = "while "+str(names[p[2]])+op+str(p[4])+":"
	substm = str(p[6]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	p[0] = tmp

def p_expression_binop(p):
	'''expression : statement PLUS statement
				  | statement MINUS statement
				  | statement TIMES statement
				  | statement DIVIDE statement'''
	if p[2] == '+'  : p[0] = str(p[1]) +"+"+ str(p[3])
	elif p[2] == '-': p[0] = str(p[1]) +"-"+ str(p[3])
	elif p[2] == '*': p[0] = str(p[1]) +"*"+ str(p[3])
	elif p[2] == '/': p[0] = str(p[1]) +"/"+ str(p[3])

def p_expression_list_creation(p):
	'''expression : RADEREMO AL SUOLO variable'''
	varName = ""
	try:
		varName = names[p[4]] 
	except KeyError:
		names[p[4]] = "var"+str(variable_counter[0])
		variable_counter[0] = variable_counter[0]+1
		varName = names[p[4]]
	p[0] = "global "+str(varName)+"\n"+str(varName) + "=[]"  
	 
def p_statement_random(p):
	'''statement : SCEGLIETE variable FRA expression E expression'''
	varName = ""
	try:
		varName = names[p[2]] 
	except KeyError:
		names[p[2]] = "var"+str(variable_counter[0])
		variable_counter[0] = variable_counter[0]+1
		varName = names[p[2]]
	p[0] = str(varName) + "= random.randint(" + str(p[4]) +","+ str(p[6]) +")"
	
def p_statement_input_number(p):
	'''statement : DITEMI variable COSA VOLETE'''
	varName = ""
	try:
		varName = names[p[2]] 
	except KeyError:
		names[p[2]] = "var"+str(variable_counter[0])
		variable_counter[0] = variable_counter[0]+1
		varName = names[p[2]]
	p[0] = str(varName) + "= input()"
	
	
def p_expression_list_sgombera(p):
	 '''expression : DA variable SGOMBERA expression
				   | DALLA variable SGOMBERA expression'''
	 p[0] = names[p[2]]+str("[")+str(p[4])+str("]")

def p_expression_list_sublist(p):
	 '''expression : variable RUBANO expression E expression
				   | variable RUBA expression E expression'''
	 first_index = p[3]
	 second_index = p[5]
	 if first_index == "\"\"":
		first_index = ""
	 if second_index == "\"\"":
		second_index = ""
	 p[0] = names[p[1]]+str("[")+str(first_index)+str(":")+str(second_index)+str("]")
	 
	 
def p_expression_cerca(p):
	'''expression : SEGREGA expression IN expression
				   | SEGREGA expression'''
	if len(p) > 4:
		code = p[2]+".split("+p[4]+")"
	else:
		code = p[2]+".split()"
	p[0] = code

def p_expression_list_deporta(p):
	 '''expression : A variable DEPORTA expression
	               | A variable DEPORTA expression NELLA CELLA expression
	               | NELLA variable DEPORTA expression NELLA CELLA expression
	               | NELLA variable DEPORTA expression
	               | AL variable DEPORTA expression NELLA CELLA expression
	               | AL variable DEPORTA expression
	               '''
	 if len(p) <= 5:
		p[0] = names[p[2]]+str(".append(")+str(p[4])+str(")")
	 else:
		p[0] = names[p[2]]+str("[")+str(p[7])+str("] =")+str(p[4])
	 
def p_expression_list_len(p):
	 '''expression : LA DIMENSIONE DI variable'''
	 p[0] = str("len(")+names[p[4]]+str(")")

def p_statement_for_each(p):
	'statement : PER OGNI variable IN variable SEMICOLON statements POINT'
	varName = ""
	try:
		varName = names[p[3]] 
	except KeyError:
		names[p[3]] = "var"+str(variable_counter[0])
		
		variable_counter[0] = variable_counter[0]+1
		varName = names[p[3]]
	tmp = "for "+str(names[p[3]]).rstrip()+" in "+str(names[p[5]])+":"
	substm = str(p[7]).split('\n')
	for stm in substm:
		tmp = tmp +"\n\t"+stm
	p[0] = tmp


def p_expression_uminus(p):
	'expression : MINUS statement %prec UMINUS'
	p[0] = "-"+p[2]

def p_expression_group(p):
	'expression : LPAREN expression RPAREN'
	p[0] = p[2]

def p_expression_numbers(p):
	'expression : numbers'
	p[0] = str(p[1])
def p_numbers_number(p):
	'''numbers : NUMBER
				  | number_float'''
	p[0] = str(p[1])
def p_numbers_number_float(p):
	'number_float : NUMBER COMMA NUMBER'
	p[0] = str(p[1]) + "."+str(p[3])

def p_expression_variable(p):
	'''expression : variable'''
	try:
		p[0] = str(names[p[1]])
	except:
		var_or_input(p[1], p.lineno(1))
		
def p_variable_name(p):
	'''variable : names
				| names COMMA'''
	try:
		p[0] = str(p[1])
	except:
		p[0] = "ERROR"
	
def p_variable_names(p):
	'names : NAME names'
	p[0] = str(p[1])+str(p[2])
		
def p_variable_names_empty(p):
	'names :'
	p[0] = ""

def p_error(p):
	print("Syntax error at line '%s'" % 	p.lexer.lineno)
	print p
	exit()

rparser = yacc.yacc()

def parse(data,debug=0):
    rparser.error = 0
    p = rparser.parse(data,debug=debug,tracking=True)
    if rparser.error: return None
    return p

def var_or_input(varName, line):
	if str(varName).find("bingo") <0:
		exceptionRuspy.no_var_found(varName,line)
	else:
		exceptionRuspy.no_input_found(varName, line)
