import ply.lex as lex

reserved = {
    'for' : 'FOR',
    'while' : 'WHILE',
    'do' : 'DO',
    'if' : 'IF',
    'else' : 'ELSE',
    'static' : 'STATIC',
    'void' : 'VOID',
    'int' : 'INT',
    'public' : 'PUBLIC'
}

delimitador = {
    '(' : 'PABIERTO',
    ')' : 'PCERRADO',
    '{' : 'LABIERTO',
    '}' : 'LCERRADO'
}

identificador = {
    'main' : 'MAIN'
}

simbolo = {
    '.' : 'PUNTO',
    ';' : 'PUNTOCOMA'
}

operador = {
    '=' : 'IGUAL',
    '+' : 'SUMA',
    '-' : 'RESTA',
    '*' : 'MULTI',
    '/' : 'DIVI',
}

tokens = ['NUMERO', 'VARIABLE'] + list(reserved.values()) + list(delimitador.values()) + list(identificador.values()) + list(simbolo.values()) + list(operador.values())

t_ignore = ' \t\r'

def t_MAIN(t):
    r'main'
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'VARIABLE')
    return t

t_PABIERTO = r'\('
t_PCERRADO = r'\)'
t_LABIERTO = r'\{'
t_LCERRADO = r'\}'
t_IGUAL = r'='
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTI = r'\*'
t_DIVI = r'\/'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_NUMERO = r'\d+'
t_PUNTOCOMA = r';'
t_PUNTO = r'.'

def t_error(t): 
    print('Caracter no valido',t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# data = '''
# public static void main()
# {
#     int n = 23.23;
# }
# '''

# lexer.input(data)

# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok.type, tok.value)