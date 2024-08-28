# Autor: Gilberto Gutiérrez Vázquez
# Semestre: 6   Grupo: M

import ply.lex as lex
from flask import Flask, render_template, request

app = Flask(__name__)

reserved = {
    'fora' : 'FOR',
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

t_FOR = r'for'
t_WHILE = r'while'
t_DO = r'do'
t_IF = r'if'
t_ELSE = r'else'
t_STATIC = r'static'
t_VOID = r'void'
t_INT = r'int'
t_PUBLIC = r'public'
t_MAIN = r'main'
t_ignore = ' \t\r'

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        t.type = 'VARIABLE'
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
t_PUNTO = r'.'
t_PUNTOCOMA = r';'

def t_error(t): 
    print('Caracter no valido',t.value[0])
    t.lexer.skip(1)


@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        code = request.form.get('code')

        lexer = lex.lex()
        lexer.input(code)
 
        result_lexema = []
        token_count = { 'RESERVADA': 0, 'DELIMITADOR': 0, 'IDENTIFICADOR': 0, 'SIMBOLO': 0, 'OPERADOR': 0, 'NUMERO': 0 }

        for tok in lexer:
            if tok.type in reserved.values():
                descripcion = "RESERVADA"
            elif tok.type in delimitador.values():
                descripcion = "DELIMITADOR"
            elif tok.type in identificador.values():
                descripcion = "IDENTIFICADOR"
            elif tok.type == "VARIABLE":
                descripcion = "IDENTIFICADOR"
            elif tok.type in simbolo.values():
                descripcion = "SIMBOLO"
            elif tok.type in operador.values():
                descripcion = "OPERADOR"
            else:
                descripcion = "NUMERO"
    
            result_lexema.append((descripcion, tok.value, tok.lineno))
            token_count[descripcion] += 1

        return render_template('index.html', tokens=result_lexema, code=code, token_count=token_count)
    return render_template('index.html', code=None)
 
if __name__ == "__main__":
    app.run(debug=True)