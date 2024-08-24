# Autor: Gilberto Gutiérrez Vázquez
# Semestre: 6   Grupo: M
import ply.lex as lex
from flask import Flask, render_template, request

app = Flask(__name__)

reserved = {
    'for' : 'FOR',
    'while' : 'WHILE',
    'do' : 'DO',
    'if' : 'IF',
    'else' : 'ELSE'
}

tokens = ['PABIERTO','PCERRADO'] + list(reserved.values())

t_FOR = r'for'
t_WHILE = r'while'
t_DO = r'do'
t_IF = r'if'
t_ELSE = r'else'
t_ignore = ' \t\n\r'

t_PABIERTO = r'\('
t_PCERRADO = r'\)'

def t_error(t): 
    print('Caracter no valido',t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        code = request.form.get('code')
        lexer.input(code)
 
        result_lexema = [
            (f"Reservada {code.type.capitalize()}" if code.type in reserved.values() else "Parentesis de apertura" if code.type == "PABIERTO" else "Parentesis de cierre", code.value)
            for code in lexer
        ]
        return render_template('index.html', tokens=result_lexema, code=code)
    return render_template('index.html', code=None)
 
if __name__ == "__main__":
    app.run(debug=True)