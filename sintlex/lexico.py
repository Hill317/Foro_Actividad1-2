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
    '}' : 'LCERRADO'
}

operador = {
    '=' : 'IGUAL',
    '+' : 'SUMA',
}

tokens = ['NUMERO', 'VARIABLE', 'IDENTIFICADOR', 'PUNTOCOMA', 'CADENA'] + list(reserved.values()) + list(delimitador.values()) + list(operador.values())

t_ignore = ' \t\r'


def t_CADENA(t):
    r'[^\"]+'
    t.type = 'CADENA'
    return t

def t_VARIABLE(t):
    r'[a-z]'
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        t.type = 'VARIABLE'
    return t

def t_IDENTIFICADOR(t):
    r'suma'
    return t

t_PABIERTO = r'\('
t_PCERRADO = r'\)'
t_LABIERTO = r'\{'
t_LCERRADO = r'\}'
t_IGUAL = r'='
t_SUMA = r'\+'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_NUMERO = r'\d+'
t_PUNTOCOMA = r';'

def t_error(t): 
    print('Caracter no valido',t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = '''
programa suma(){\
    int a,b,c;
    read a;
    read b;
    c=a+b;
printf ("la suma es");
end;
}
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.type, tok.value)