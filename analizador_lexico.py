import sys
sys.dont_write_bytecode = True
import os
print("Cargando analizador desde:", os.path.abspath(__file__))
import re
import ply.lex as lex

# Definición de tokens de PLY
tokens = (
    'IDENTIFICADOR', 'ASIGNAR', 'SUMA', 'RESTA', 'MULT', 'DIV', 'POTENCIA', 'MODULO',
    'ENTERO', 'PARIZQ', 'PARDER', 'LLAIZQ', 'LLADER', 'CORIZQ', 'CORDER', 'PUNTOCOMA',
    'MENORQUE', 'MAYORQUE', 'MENORIGUAL', 'MAYORIGUAL', 'IGUAL', 'DISTINTO',
    'AND', 'OR', 'NOT', 'PALABRA_CLAVE', 'LITERAL_CADENA', 'LITERAL_BOOLEANO', 'LITERAL_NULO'
)

# Lista extendida de palabras clave en Python
PALABRAS_CLAVE_PYTHON = r'\bif\b|\belse\b|\bwhile\b|\bfor\b|\breturn\b|\bprint\b|\binput\b|\bdef\b|\bclass\b|\bimport\b|\bas\b|\bfrom\b|\bpass\b|\bcontinue\b|\bbreak\b|\band\b|\bor\b|\bnot\b|\bin\b|\bis\b|\bNone\b|\bTrue\b|\bFalse\b|\blambda\b|\bwith\b|\btry\b|\bexcept\b|\braise\b|\bfinally\b|\bdel\b|\bglobal\b|\bnonlocal\b|\byield\b|\basync\b|\bawait\b'

# Especificación de tokens
t_ASIGNAR = r'='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_POTENCIA = r'\*\*'
t_MODULO = r'%'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_PUNTOCOMA = r';'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_IGUAL = r'=='
t_DISTINTO = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

# Definir la regla para los números enteros
def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Definir la regla para las palabras clave
def t_PALABRA_CLAVE(t):
    r'\bif\b|\belse\b|\bwhile\b|\bfor\b|\breturn\b|\bprint\b|\binput\b|\bdef\b|\bclass\b|\bimport\b|\bas\b|\bfrom\b|\bpass\b|\bcontinue\b|\bbreak\b|\band\b|\bor\b|\bnot\b|\bin\b|\bis\b|\bNone\b|\bTrue\b|\bFalse\b|\blambda\b|\bwith\b|\btry\b|\bexcept\b|\braise\b|\bfinally\b|\bdel\b|\bglobal\b|\bnonlocal\b|\byield\b|\basync\b|\bawait\b'
    return t

# Definir la regla para los literales de cadena
def t_LITERAL_CADENA(t):
    r'f?"[^"\n]*"|f?\'[^\']*\''
    return t

# Definir la regla para booleanos
def t_LITERAL_BOOLEANO(t):
    r'\bTrue\b|\bFalse\b'
    t.value = True if t.value == 'True' else False
    return t

# Definir la regla para literales nulos
def t_LITERAL_NULO(t):
    r'\bNone\b'
    t.value = None
    return t

# Definir la regla para identificadores
def t_IDENTIFICADOR(t):
    r'[A-Za-z_]\w*'
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejar nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejar errores léxicos
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Crear el analizador léxico
analizador = lex.lex()