from lex import crear_lexer
from sintactico import crear_parser, errores, graficar_arbol

lexer = crear_lexer()
parser = crear_parser()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue

   errores.clear()

   lexer.input(s)

   result = parser.parse(s, lexer=lexer)
   print(result)
   print(errores)