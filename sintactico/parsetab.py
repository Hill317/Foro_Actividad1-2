
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVI DO ELSE FOR IF IGUAL INT LABIERTO LCERRADO MAIN MULTI NUMERO PABIERTO PCERRADO PUBLIC PUNTO PUNTOCOMA RESTA STATIC SUMA VARIABLE VOID WHILEprograma : declaracion_metodo bloquedeclaracion_metodo : PUBLIC STATIC VOID MAIN PABIERTO PCERRADObloque : LABIERTO declaracion LCERRADOdeclaracion : INT VARIABLE IGUAL numero PUNTOCOMAnumero : NUMERO PUNTO NUMERO\n                 | NUMERO'
    
_lr_action_items = {'PUBLIC':([0,],[3,]),'$end':([1,4,10,],[0,-1,-3,]),'LABIERTO':([2,17,],[5,-2,]),'STATIC':([3,],[6,]),'INT':([5,],[8,]),'VOID':([6,],[9,]),'LCERRADO':([7,18,],[10,-4,]),'VARIABLE':([8,],[11,]),'MAIN':([9,],[12,]),'IGUAL':([11,],[13,]),'PABIERTO':([12,],[14,]),'NUMERO':([13,19,],[16,20,]),'PCERRADO':([14,],[17,]),'PUNTOCOMA':([15,16,20,],[18,-6,-5,]),'PUNTO':([16,],[19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'declaracion_metodo':([0,],[2,]),'bloque':([2,],[4,]),'declaracion':([5,],[7,]),'numero':([13,],[15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> declaracion_metodo bloque','programa',2,'p_programa','sintactico.py',8),
  ('declaracion_metodo -> PUBLIC STATIC VOID MAIN PABIERTO PCERRADO','declaracion_metodo',6,'p_declaracion_metodo','sintactico.py',12),
  ('bloque -> LABIERTO declaracion LCERRADO','bloque',3,'p_bloque','sintactico.py',16),
  ('declaracion -> INT VARIABLE IGUAL numero PUNTOCOMA','declaracion',5,'p_declaracion','sintactico.py',20),
  ('numero -> NUMERO PUNTO NUMERO','numero',3,'p_numero','sintactico.py',28),
  ('numero -> NUMERO','numero',1,'p_numero','sintactico.py',29),
]