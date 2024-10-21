import ply.yacc as yacc
from lex import tokens, crear_lexer
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx

errores = []

class Nodo:
    def __init__(self, tipo, izquierdo=None, derecho=None, valor=None):
        self.tipo = tipo
        self.izquierdo = izquierdo
        self.derecho = derecho
        self.valor = valor

    def __repr__(self):
        if self.valor is not None:
            return f'NUMERO({self.valor})'
        return f'NODO({self.tipo})'

def p_inicio(p):
    '''inicio : inicio SUMA medio
              | inicio RESTA medio
              | medio'''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = Nodo('SUMA', izquierdo=p[1], derecho=p[3])
        elif p[2] == '-':
            p[0] = Nodo('RESTA', izquierdo=p[1], derecho=p[3])
    else:
        p[0] = p[1]

def p_medio(p):
    '''medio : medio MULTI final
              | medio DIVI final
              | final'''
    if len(p) == 4:
        if p[2] == '*':
            p[0] = Nodo('MULTI', izquierdo=p[1], derecho=p[3])
        elif p[2] == '/':
            if p[3].valor == 0:
                errores.append("Error: División por cero")
                p[0] = None
            else:
                p[0] = Nodo('DIVI', izquierdo=p[1], derecho=p[3])
    else:
        p[0] = p[1]

def p_final(p):
    '''final : PABIERTO inicio PCERRADO
              | NUMERO
              | DECIMAL'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = Nodo('NUMERO', valor=float(p[1]))

def p_error(p):
    if p:
        error_msg = f"Error de sintaxis con '{p.value}'"
    else:
        error_msg = "Error de sintaxis: EOF inesperado"
    errores.append(error_msg)

def crear_arbol():
    parser = yacc.yacc()
    return parser

def graficar_arbol(nodo):
    G = nx.DiGraph()

    def agregar_nodo(nodo, parent=None):
        if nodo.valor is not None:
            G.add_node(nodo.valor)
        else:
            G.add_node(nodo.tipo)

        if parent:
            if nodo.valor is not None:
                G.add_edge(parent, nodo.valor)
            else:
                G.add_edge(parent, nodo.tipo)

        if nodo.izquierdo:
            agregar_nodo(nodo.izquierdo, nodo.tipo if nodo.valor is None else nodo.valor)
        if nodo.derecho:
            agregar_nodo(nodo.derecho, nodo.tipo if nodo.valor is None else nodo.valor)

    agregar_nodo(nodo)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10)
    plt.savefig("static/arbol_sintactico.png")
    plt.close()
