import ply.lex as lex

reserved = {
    'programa' : 'PROGRAMA',
    'int' : 'INT',
    'printf' : 'PRINTF',
    'end' : 'END',
    'read' : 'READ'
}

delimitador = {
    '(' : 'PABIERTO',
    ')' : 'PCERRADO',
    '{' : 'LABIERTO',
    '}' : 'LCERRADO',
    '"' : 'COMILLA',
}

operador = {
    '=' : 'IGUAL',
    '+' : 'SUMA',
}

signos = {
    ';' : 'PUNTOCOMA',
    ',' : 'COMA',
}

tokens = ['VARIABLE', 'IDENTIFICADOR', 'CADENA'] + list(reserved.values()) + list(delimitador.values()) + list(operador.values()) + list(signos.values())

t_ignore = ' \t\r'

def t_IDENTIFICADOR(t):
    r'Suma'
    return t

def t_VARIABLE(t):
    r'\w+'
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        if len(t.value) == 1:
            t.type = 'VARIABLE'
        else:
            t.type = 'CADENA'
    return t

t_PABIERTO = r'\('
t_PCERRADO = r'\)'
t_LABIERTO = r'\{'
t_LCERRADO = r'\}'
t_ignore_COMILLA = r'"'
t_IGUAL = r'='
t_SUMA = r'\+'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_PUNTOCOMA = r';'
t_ignore_COMA = r','

def t_error(t): 
    print('Caracter no valido',t.value[0])
    t.lexer.skip(1)

def crear_lexer():
    lexer = lex.lex()
    return lexer

# data = '''
# programa Suma(){\
#     int a,b,c;
#     read a;
#     read b;
#     c=a+b;
# printf ("la suma es");
# end;
# }
# '''

# lexer.input(data)

# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok.type, tok.value)