from lex import crear_lexer
from sintactico import crear_parser, errores
from arbol import crear_arbol, graficar_arbol
from flask import Flask, render_template, request, url_for, redirect
import os

app = Flask(__name__)

def imprimir_arbol(nodo, nivel=0):
    if nodo is not None:
        print("  " * nivel + repr(nodo))
        imprimir_arbol(nodo.izquierdo, nivel + 1)
        imprimir_arbol(nodo.derecho, nivel + 1)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form.get('code')
        valor = 1

        if 'ir_arbol' in request.form and request.form.get('code') != '':
            if valor == 1:
                return redirect(url_for('arbol', valido=1))

        lexer = crear_lexer()
        parser = crear_parser()
        arbol = crear_arbol()

        errores.clear()

        lexer.input(code)
        result_lexema = []

        for tok in lexer:
            if tok.type == 'PABIERTO':
                descripcion = "Paréntesis izquierdo"
            elif tok.type == 'PCERRADO':
                descripcion = "Paréntesis derecho"
            elif tok.type == 'SUMA':
                descripcion = "Signo suma"
            elif tok.type == 'RESTA':
                descripcion = "Signo resta"
            elif tok.type == 'MULTI':
                descripcion = "Signo multiplicación"
            elif tok.type == 'DIVI':
                descripcion = "Signo división"
            elif tok.type == 'NUMERO':
                descripcion = "Número"
            else:
                descripcion = "Decimal"
                
            result_lexema.append((tok.value, descripcion))

        try:
            resultado = parser.parse(code, lexer=lexer)
            nodos = arbol.parse(code, lexer=lexer)
            if resultado % 1 == 0:
                resultado = int(resultado)
            # Genera el gráfico del árbol
            if nodos:  # Asegúrate de que hay nodos para graficar
                imprimir_arbol(nodos)
                graficar_arbol(nodos)  # Graficar el primer nodo como raíz
                arbol_img = "static/arbol_sintactico.png"  # Ruta de la imagen generada
            else:
                arbol_img = None  # O maneja el caso cuando no hay nodos

        except Exception as e:
            if not resultado:
                pass
            else:
                resultado = errores[0]
                valor = 0
            

        return render_template('index.html', valor=valor, resultado=resultado, tokens=result_lexema)

    return render_template('index.html', valor=0, resultado='')

@app.route('/arbol', methods=['GET', 'POST'])
def arbol():
    if request.method == 'POST':
        if 'ir_index' in request.form:
            return redirect(url_for('index'))

    try:
        valido = int(request.args.get('valido', 0))

        return render_template('arbol.html', valido=valido)
    
    except Exception as e:
        pass

    return render_template('arbol.html', valido=0)

if __name__ == "__main__":
    app.run(debug=True)
