import ply.yacc as yacc
import ply.lex as lex
from flask import Flask, render_template, request
from lexico import tokens, crear_lexer, reserved, delimitador, operador, signos

app = Flask(__name__)

errores = []
var = []
var2 = []

def p_programa(p):
    '''programa : PROGRAMA IDENTIFICADOR PABIERTO PCERRADO LABIERTO cuerpo LCERRADO'''

def p_cuerpo(p):
    '''cuerpo : inicializacion leer igual imprimir final '''

def p_inicializacion(p):
    '''inicializacion : INT variables PUNTOCOMA'''

def p_variables(p):
    '''variables : VARIABLE variables
                   | COMA variables
                   | vacio
                   '''
    
    if (len(p) == 3) and p[1] != ',':
        var.append(p[1])


def p_leer(p):
    '''leer : READ VARIABLE PUNTOCOMA leer
              | READ VARIABLE PUNTOCOMA'''
    
    if p[2] not in var:
        error_msg = f"Error: Variable '{p[2]}' no declarada"
        errores.append(error_msg)

    var2.append(p[2])

def p_igual(p):
    '''igual : VARIABLE IGUAL VARIABLE SUMA VARIABLE PUNTOCOMA'''

    if p[1] not in var:
        error_msg = f"Error: Variable '{p[1]}' no declarada"
        errores.append(error_msg)

    for vari in [p[3], p[5]]:
        if vari not in var2:
            if vari in var:
                error_msg = f"Error: Variable '{vari}' no leída antes"
                errores.append(error_msg)
            else:
                error_msg = f"Error: Variable '{vari}' no declarada"
                errores.append(error_msg)

def p_imprimir(p):
    '''imprimir : PRINTF PABIERTO COMILLA cadena COMILLA PCERRADO PUNTOCOMA'''

def p_cadena(p):
    '''cadena : CADENA CADENA CADENA
                '''

def p_final(p):
    '''final : END PUNTOCOMA'''

# Manejo de errores en el parser
def p_error(p):
    if p:
        if p.type == 'CADENA':
            pass
        else:
            error_msg = f"Error de sintaxis en '{p.value}' en la línea {p.lineno}"
            errores.append(error_msg)
    else:
        error_msg = "Error de sintaxis: EOF inesperado"
        errores.append(error_msg)

def p_vacio(p):
    'vacio :'
    pass

@app.route('/', methods = ['GET','POST'])
def index():
    global errores
    global var
    global var2

    errores = []
    var = []
    var2 = []
    color = 0

    if request.method == 'POST':
        boton = request.form.get('submit_type')
        if boton == 'lexico':
            code = request.form.get('code')
            lexer = crear_lexer()
            lexer.input(code)
            

            result_lexema = []
            token_count = { 'RESERVADA': 0, 'DELIMITADOR': 0, 'OPERADOR': 0, 'SIGNO': 0, 'VARIABLE': 0, 'IDENTIFICADOR': 0, 'CADENA': 0 }

            for tok in lexer:
                if tok.type in reserved.values():
                    descripcion = "RESERVADA"
                    result_lexema.append((tok.lineno, tok.value, "X", "", "", "", "", "", "" ))
                elif tok.type in delimitador.values():
                    descripcion = "DELIMITADOR"
                    result_lexema.append((tok.lineno, tok.value, "", "X", "", "", "", "", "" ))
                elif tok.type in operador.values():
                    descripcion = "OPERADOR"
                    result_lexema.append((tok.lineno, tok.value, "", "", "X", "", "", "", "" ))
                elif tok.type in signos.values():
                    descripcion = "SIGNO"
                    result_lexema.append((tok.lineno, tok.value, "", "", "", "X", "", "", "" ))
                elif tok.type == 'VARIABLE':
                    descripcion = "VARIABLE"
                    result_lexema.append((tok.lineno, tok.value, "", "", "", "", "X", "", "" ))
                elif tok.type == 'IDENTIFICADOR':
                    descripcion = "IDENTIFICADOR"
                    result_lexema.append((tok.lineno, tok.value, "", "", "", "", "", "X", "" ))
                else:
                    descripcion = tok.type
                    result_lexema.append((tok.lineno, tok.value, "", "", "", "", "", "", "X" ))

                token_count[descripcion] += 1

            result_lexema.append(("", "Total", *token_count.values()))
            

            return render_template('index.html', code=code,  tokens=result_lexema, valor=1)
    
        else:
            code = request.form.get('code')
            parser = yacc.yacc()

            try:
                parser.parse(code)
                if errores:
                    result = "Código no aceptado."
                else:
                    result = "Código aceptado."
                    color = 1
            except Exception as e:
                errores.append(str(e))
                result = "Error al analizar el código."

            return render_template('index.html', code=code, errores=errores, color=color, resultado=result, valor=2)

        
    return render_template('index.html', code=None, valor=0)


if __name__ == "__main__":
    app.run(debug=True)

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