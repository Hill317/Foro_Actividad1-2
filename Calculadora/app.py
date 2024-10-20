from lex import crear_lexer
from sintactico import crear_parser, errores
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form.get('code')

        lexer = crear_lexer()
        parser = crear_parser()

        errores.clear()

        lexer.input(code)
        resultado = parser.parse(code, lexer=lexer)
        if resultado % 1 == 0:
            resultado = int(resultado)

        return render_template('index.html', valor=1, resultado=resultado)

    return render_template('index.html', valor=0)

if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/', methods = ['GET','POST'])
# def index():
#     global errores
#     global var
#     global var2

#     errores = []
#     color = 0

#     if request.method == 'POST':
#         boton = request.form.get('submit_type')
#         if boton == 'lexico':
#             code = request.form.get('code')
#             lexer = crear_lexer()
#             lexer.input(code)
            

#             result_lexema = []
#             token_count = { 'RESERVADA': 0, 'DELIMITADOR': 0, 'OPERADOR': 0, 'SIGNO': 0, 'VARIABLE': 0, 'IDENTIFICADOR': 0, 'CADENA': 0 }

#             for tok in lexer:
#                 if tok.type in reserved.values():
#                     descripcion = "RESERVADA"
#                     result_lexema.append((tok.lineno, tok.value, "X", "", "", "", "", "", "" ))
#                 elif tok.type in delimitador.values():
#                     descripcion = "DELIMITADOR"
#                     result_lexema.append((tok.lineno, tok.value, "", "X", "", "", "", "", "" ))
#                 elif tok.type in operador.values():
#                     descripcion = "OPERADOR"
#                     result_lexema.append((tok.lineno, tok.value, "", "", "X", "", "", "", "" ))
#                 elif tok.type in signos.values():
#                     descripcion = "SIGNO"
#                     result_lexema.append((tok.lineno, tok.value, "", "", "", "X", "", "", "" ))
#                 elif tok.type == 'VARIABLE':
#                     descripcion = "VARIABLE"
#                     result_lexema.append((tok.lineno, tok.value, "", "", "", "", "X", "", "" ))
#                 elif tok.type == 'IDENTIFICADOR':
#                     descripcion = "IDENTIFICADOR"
#                     result_lexema.append((tok.lineno, tok.value, "", "", "", "", "", "X", "" ))
#                 else:
#                     descripcion = tok.type
#                     result_lexema.append((tok.lineno, tok.value, "", "", "", "", "", "", "X" ))

#                 token_count[descripcion] += 1

#             result_lexema.append(("", "Total", *token_count.values()))
            

#             return render_template('index.html', code=code,  tokens=result_lexema, valor=1)
    
#         else:
#             code = request.form.get('code')
#             parser = yacc.yacc()

#             try:
#                 parser.parse(code)
#                 if errores:
#                     result = "Código no aceptado."
#                 else:
#                     result = "Código aceptado."
#                     color = 1
#             except Exception as e:
#                 errores.append(str(e))
#                 result = "Error al analizar el código."

#             return render_template('index.html', code=code, errores=errores, color=color, resultado=result, valor=2)

        
#     return render_template('index.html', code=None, valor=0)