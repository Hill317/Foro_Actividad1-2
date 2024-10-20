import ply.lex as lex

delimitador = {
    '(' : 'PABIERTO',
    ')' : 'PCERRADO'
}

operador = {
    '+' : 'SUMA',
    '-' : 'RESTA',
    '*' : 'MULTI',
    '/' : 'DIVI',
}

tokens = ['NUMERO', 'DECIMAL'] + list(operador.values()) + list(delimitador.values())

t_ignore = ' \n\t\r'

t_PABIERTO = r'\('
t_PCERRADO = r'\)'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTI = r'\*'
t_DIVI = r'\/'

def t_DECIMAL(t):
    r'\d*\.\d+'
    t.value = round(float(t.value), 4)
    return t

t_NUMERO = r'\d+'

def t_error(t): 
    print('Caracter no valido',t.value[0])
    t.lexer.skip(1)

def crear_lexer():
    lexer = lex.lex()
    return lexer

# data = "((22-5)*9)/7.55557"

# lexer = crear_lexer()
# lexer.input(data)

# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok.type, tok.value)