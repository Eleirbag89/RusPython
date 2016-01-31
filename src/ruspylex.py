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
}
tokens = [
	'NAME','NUMBER',
	'PLUS','MINUS','TIMES','DIVIDE','EQUALS','QUESTION_MARK','ESCLAMATION_POINT',
	'LPAREN','RPAREN','COMMA', 'POINT', 'DQUOTE', 'SEMICOLON'
	] + list(reserved.values())

# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_COMMA   = r'\,'
t_POINT  = r'\.'
t_SEMICOLON  = r'\;'
t_QUESTION_MARK  = r'\?'
t_ESCLAMATION_POINT  = r'\!'
t_DIVIDE  = r'/'
t_EQUALS  = r'è'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if not(lex.dquotes):
		t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t
	
def t_DQUOTE(t):
	r'\"'
	lex.dquotes = not(lex.dquotes)
	return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

# Build the lexer
lex.dquotes= False
lex.lex()
