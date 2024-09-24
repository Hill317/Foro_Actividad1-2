import ply.yacc as yacc
from lexico import tokens
from flask import Flask, render_template, request

app = Flask(__name__)

errores = []

def p_programa(p):
    '''programa : declaracion_metodo bloque'''
    print("Programa reconocido.")

def p_declaracion_metodo(p):
    '''declaracion_metodo : PUBLIC STATIC VOID MAIN PABIERTO PCERRADO'''
    print("Declaración del método main reconocida.")

def p_bloque(p):
    '''bloque : LABIERTO declaracion LCERRADO'''
    print("Bloque de código reconocido.")

def p_declaracion(p):
    '''declaracion : INT VARIABLE IGUAL numero PUNTOCOMA'''
    print(f"Declaración reconocida: {p[2]} asignado a {p[4]}.")

# def p_tipo(p):
#     '''tipo : INT'''
#     p[0] = 'int'

def p_numero(p):
    '''numero : NUMERO PUNTO NUMERO
                 | NUMERO'''

# Manejo de errores en el parser
def p_error(p):
    if p:
        error_msg = f"Error de sintaxis en '{p.value}' en la línea {p.lineno}"
    else:
        error_msg = "Error de sintaxis: EOF inesperado"
    errores.append(error_msg)

@app.route('/', methods = ['GET','POST'])
def index():
    global errores
    errores = []
    color = 0

    if request.method == 'POST':
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

        return render_template('index.html', code=code, errores=errores, color=color, resultado=result)
    return render_template('index.html', code=None)

# s = '''
# public static void main()
# {
#     int n = 23.23;
# }
# '''