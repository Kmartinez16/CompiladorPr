
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASIGNAR CORDER CORIZQ DISTINTO DIV ENTERO IDENTIFICADOR IGUAL LITERAL_BOOLEANO LITERAL_CADENA LITERAL_NULO LLADER LLAIZQ MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MODULO MULT NOT OR PALABRA_CLAVE PARDER PARIZQ POTENCIA PUNTOCOMA RESTA SUMAdeclaracion : IDENTIFICADOR ASIGNAR expresion PUNTOCOMAdeclaracion : expresion PUNTOCOMAexpresion : expresion SUMA expresion\n                 | expresion RESTA expresion\n                 | expresion MULT expresion\n                 | expresion DIV expresion\n                 | expresion POTENCIA expresion\n                 | expresion MODULO expresionexpresion : ENTEROexpresion : IDENTIFICADORexpresion : PARIZQ expresion PARDER'
    
_lr_action_items = {'IDENTIFICADOR':([0,5,6,8,9,10,11,12,13,],[2,15,15,15,15,15,15,15,15,]),'ENTERO':([0,5,6,8,9,10,11,12,13,],[4,4,4,4,4,4,4,4,4,]),'PARIZQ':([0,5,6,8,9,10,11,12,13,],[5,5,5,5,5,5,5,5,5,]),'$end':([1,7,24,],[0,-2,-1,]),'ASIGNAR':([2,],[6,]),'PUNTOCOMA':([2,3,4,15,16,17,18,19,20,21,22,23,],[-10,7,-9,-10,24,-3,-4,-5,-6,-7,-8,-11,]),'SUMA':([2,3,4,14,15,16,17,18,19,20,21,22,23,],[-10,8,-9,8,-10,8,8,8,8,8,8,8,-11,]),'RESTA':([2,3,4,14,15,16,17,18,19,20,21,22,23,],[-10,9,-9,9,-10,9,9,9,9,9,9,9,-11,]),'MULT':([2,3,4,14,15,16,17,18,19,20,21,22,23,],[-10,10,-9,10,-10,10,10,10,10,10,10,10,-11,]),'DIV':([2,3,4,14,15,16,17,18,19,20,21,22,23,],[-10,11,-9,11,-10,11,11,11,11,11,11,11,-11,]),'POTENCIA':([2,3,4,14,15,16,17,18,19,20,21,22,23,],[-10,12,-9,12,-10,12,12,12,12,12,12,12,-11,]),'MODULO':([2,3,4,14,15,16,17,18,19,20,21,22,23,],[-10,13,-9,13,-10,13,13,13,13,13,13,13,-11,]),'PARDER':([4,14,15,17,18,19,20,21,22,23,],[-9,23,-10,-3,-4,-5,-6,-7,-8,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracion':([0,],[1,]),'expresion':([0,5,6,8,9,10,11,12,13,],[3,14,16,17,18,19,20,21,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracion","S'",1,None,None,None),
  ('declaracion -> IDENTIFICADOR ASIGNAR expresion PUNTOCOMA','declaracion',4,'p_declaracion_asignar','prue.py',24),
  ('declaracion -> expresion PUNTOCOMA','declaracion',2,'p_declaracion_expr','prue.py',31),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresion_operaciones','prue.py',35),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion_operaciones','prue.py',36),
  ('expresion -> expresion MULT expresion','expresion',3,'p_expresion_operaciones','prue.py',37),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_operaciones','prue.py',38),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_expresion_operaciones','prue.py',39),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_operaciones','prue.py',40),
  ('expresion -> ENTERO','expresion',1,'p_expresion_numero','prue.py',56),
  ('expresion -> IDENTIFICADOR','expresion',1,'p_expresion_nombre','prue.py',60),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_grupo','prue.py',69),
]