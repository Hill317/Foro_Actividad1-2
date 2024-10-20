import ply.yacc as yacc
from lex import tokens, crear_lexer


errores = []

def p_inicio(p):
    '''inicio : inicio SUMA medio
              | inicio RESTA medio
              | medio'''
    if len(p) == 4:  # Si la regla tiene una operación
        if p[2] == '+':
            p[0] = p[1] + p[3]  # Sumar
        elif p[2] == '-':
            p[0] = p[1] - p[3]  # Restar
    else:
        p[0] = p[1]  # Pasar el valor de "medio"

def p_medio(p):
    '''medio : medio MULTI final
              | medio DIVI final
              | final'''
    if len(p) == 4:  # Si la regla tiene una operación
        if p[2] == '*':
            p[0] = p[1] * p[3]  # Multiplicar
        elif p[2] == '/':
            p[0] = p[1] / p[3]  # Dividir
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

# lexer = crear_lexer()
# parser = crear_parser()

# while True:
#    try:
#        s = input('calc > ')
#    except EOFError:
#        break
#    if not s: continue
#    lexer.input(s)

#    result = parser.parse(s, lexer=lexer)
#    print(result)
#    print(errores)