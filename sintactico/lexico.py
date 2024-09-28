import ply.lex as lex

reserved = {
    'for' : 'FOR',
    'int' : 'INT',
}

delimitador = {
    '(' : 'PABIERTO',
    ')' : 'PCERRADO',
    '{' : 'LABIERTO',
    '}' : 'LCERRADO'
}

identificador = {
    'i' : 'I',
    'System' : 'SYSTEM',
    'out' : 'OUT',
    'println' : 'PRINTLN'
}

simbolo = {
    '.' : 'PUNTO',
    ';' : 'PUNTOCOMA'
}

operador = {
    '=' : 'IGUAL',
    '<=' : 'MENORIGUAL',
    '++' : 'INCREMENTO',
    '+' : 'CONCATENACION',
}

tokens = ['NUMERO', 'CADENA'] + list(reserved.values()) + list(delimitador.values()) + list(identificador.values()) + list(simbolo.values()) + list(operador.values())

t_ignore = ' \t\r'

def t_INT(t):
    r'int'
    return t

def t_FOR(t):
    r'for'
    return t

def t_I(t):
    r'i'
    return t

def t_SYSTEM(t):
    r'System'
    return t

def t_OUT(t):
    r'out'
    return t

def t_PRINTLN(t):
    r'println'
    return t


t_PABIERTO = r'\('
t_PCERRADO = r'\)'
t_LABIERTO = r'\{'
t_LCERRADO = r'\}'
t_MENORIGUAL = r'<='
t_IGUAL = r'='
t_CONCATENACION = r'\+'
t_INCREMENTO = r'\+\+'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_NUMERO = r'\d+'
t_PUNTOCOMA = r';'
t_PUNTO = r'.'
t_CADENA = r'\".*?\"'

def t_error(t): 
    print('Caracter no valido',t.value[0])
    t.lexer.skip(1)

# lexer = lex.lex()

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