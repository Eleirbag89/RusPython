# coding: latin-1
import ply.lex as lex

reserved = {
   'sono' : 'SONO',
   'finche' : 'FINCHE',
   'urla' : 'URLA',
   'padanialibera':'PADANIALIBERA',
   'altrimenti':'ALTRIMENTI',
   'minore':'MINORE',
   'maggiore':'MAGGIORE',
   'uguale':'UGUALE',
   'espelli':'ESPELLI',
   'espellili':'ESPELLILI',
   'attenzione':'ATTENZIONE',
   'basta':'BASTA',
   'respingiamo':'START_PARAMS',
   'tornino':'TORNINO',
   'a':'A',
   'al':'AL',
   'casa':'CASA',
   'loro':'LORO',
   'e':'E',
   'ricordate':'RICORDATE',
   'per':'PER',
   'ogni':'OGNI',
   'in':'IN',
   'sgombera':'SGOMBERA',
   'deporta':'DEPORTA',
   'raderemo':'RADEREMO',
   'al':'AL',
   'suolo':'SUOLO',
   'da':'DA',
   'dalla':'DALLA',
   'di':'DI',
   'la':'LA',
   'dimensione':'DIMENSIONE',
   'nella':'NELLA',
   'cella':'CELLA',
   'ditemi':'DITEMI',
   'cosa':'COSA',
   'volete':'VOLETE',
   'scegliete':'SCEGLIETE',
   'fra':'FRA',
   'rubano':'RUBANO',
   'ruba':'RUBA',
   'segrega':'SEGREGA',
   'mandiamo':'MANDIAMO',
   'lavorare':'LAVORARE',
   'con':'CON',
   'spione':'SPIONE',
   'ama':'AMA',
   'odia':'ODIA',
   'ascolta':'ASCOLTA',
   'che':'CHE',
   'regala':'REGALA',
   'euri':'EURI',
   'dico':'DICO',
   'uccidiamo':'UCCIDIAMO',
   'rifiutiamo':'RIFIUTIAMO',
   'esiste':'ESISTE',
   'cartella':'CARTELLA',
   'leggermente':'LEGGERMENTE',
   'infame':'INFAME',
}
tokens = [
	'NAME','NUMBER',
	'PLUS','MINUS','TIMES','DIVIDE','EQUALS','QUESTION_MARK','ESCLAMATION_POINT',
	'LPAREN','RPAREN','COMMA', 'POINT', 'DQUOTE', 'SEMICOLON','DPOINT'
	] + list(reserved.values())

#TOKENS

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if not(lex.dquotes):
		t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

def t_NUMBER(t):
	r'\d+'
	if not(lex.dquotes):
		t.value = int(t.value)    
		return t
	t.type = 'NAME'
	return t

def t_POINT(t):
	r'\.'
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = '.'
	return t

def t_COMMA(t):
	r'\,'
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = ','
	return t
	
def t_SLASH(t):
	r'\\'
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = '\\'
	return t

def t_QUESTION_MARK(t):
	r'\?'
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = '?'
	return t

def t_ESCLAMATION_POINT(t):
	r'\!'
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = '!'
	return t

def t_DPOINT(t):
	r'\:'
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = ':'
	return t

def t_LTAG(t):
	r'\<'
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = '<'
	return t

def t_RTAG(t):
	r'\>'
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = '>'
	return t

def t_SEMICOLON(t):
	r'\;'
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = ';'
	return t

def t_DIVIDE(t):
	r'/'
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = '/'
	return t
	
def t_EQUALS(t):
	r'è'
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = 'è'
	return t
	
def t_PLUS(t):
	r'\+'
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = '+'
	return t

def t_MINUS(t):
	r'-'
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = '-'
	return t	
	
def t_TIMES(t):
	r'\*'
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = '*'
	return t	
		
def t_LPAREN(t):
	r'\('
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = '('
	return t	

def t_RPAREN(t):
	r'\)'
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = ')'
	return t	
	
def t_SPACE(t):
	r'\ '
	if lex.dquotes:
		t.type = 'NAME'  # Check for reserved words
		t.value = ' '
		return t
	else: pass
	
def t_DQUOTE(t):
	r'\"'
	lex.dquotes = not(lex.dquotes)
	return t

# Ignored characters
t_ignore = "\t"

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

# Build the lexer
lex.dquotes= False
lex.lex()
