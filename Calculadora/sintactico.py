import ply.yacc as yacc
from lex import tokens, crear_lexer

errores = []

def p_inicio(p):
    '''inicio : inicio SUMA medio
              | inicio RESTA medio
              | medio'''
    if len(p) == 4:  # Si la regla tiene una operación
        # Crear un nodo con el operador y conectar los operandos como hijos
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]  # Pasar el valor de "medio"

def p_medio(p):
    '''medio : medio MULTI final
              | medio DIVI final
              | final'''
    if len(p) == 4:  # Si la regla tiene una operación
        # Crear un nodo con el operador y conectar los operandos como hijos
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            if p[3] == 0:  # Verificar si el divisor es cero
                errores.append("Error: División por cero")
                p[0] = None  # O cualquier valor que decidas retornar en caso de error
            else:
                p[0] = p[1] / p[3]
    else:
        p[0] = p[1]  # Pasar el valor de "final"

def p_final(p):
    '''final : PABIERTO inicio PCERRADO
              | NUMERO
              | DECIMAL'''
    if len(p) == 4:  # Paréntesis
        p[0] = p[2]  # Pasar el valor dentro de los paréntesis
    else:
        p[0] = float(p[1])  # Convertir a número flotante

# Manejo de errores en el parser
def p_error(p):
    if p:
        error_msg = f"Error de sintaxis con '{p.value}'"
    else:
        error_msg = "Error de sintaxis: EOF inesperado"
    errores.append(error_msg)

def crear_parser():
    parser = yacc.yacc()
    return parser

