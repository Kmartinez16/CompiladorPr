import ply.yacc as yacc
from analizador_lexico import tokens, analizador  

import graphviz

# Diccionario para guardar variables y sus valores/tipos
nombres = {}

# ÁRBOL DE SINTAXIS ABSTRACTO (AST)
class NodoAST:
    def __init__(self, tipo, hijos=None, valor=None):
        self.tipo = tipo  # Tipo de nodo (operador, número, etc.)
        self.hijos = hijos if hijos else []  # Hijos (nodos del AST)
        self.valor = valor  # Valor del nodo (en caso de ser un número o identificador)

def p_declaracion_asignar(t):
    'declaracion : IDENTIFICADOR ASIGNAR expresion PUNTOCOMA'
    t[0] = NodoAST("asignacion", [NodoAST("identificador", valor=t[1]), t[3]])

    # Asignación semántica
    nombres[t[1]] = t[3].valor

def p_declaracion_expr(t):
    'declaracion : expresion PUNTOCOMA'
    t[0] = t[1]

def p_expresion_operaciones(t):
    '''expresion : expresion SUMA expresion
                 | expresion RESTA expresion
                 | expresion MULT expresion
                 | expresion DIV expresion
                 | expresion POTENCIA expresion
                 | expresion MODULO expresion'''
    t[0] = NodoAST("operacion", [t[1], t[3]], t[2])

    # Verificación semántica de tipos
    if not isinstance(t[1].valor, (int, float)) or not isinstance(t[3].valor, (int, float)):
        print(f"Error semántico: Operación entre tipos no numéricos en línea {t.lineno(2)}.")
    else:
        
        if t[2] == '+': t[0].valor = t[1].valor + t[3].valor
        elif t[2] == '-': t[0].valor = t[1].valor - t[3].valor
        elif t[2] == '*': t[0].valor = t[1].valor * t[3].valor
        elif t[2] == '/': t[0].valor = t[1].valor / t[3].valor
        elif t[2] == '%': t[0].valor = t[1].valor % t[3].valor
        elif t[2] == '**': t[0].valor = t[1].valor ** t[3].valor

def p_expresion_numero(t):
    'expresion : ENTERO'
    t[0] = NodoAST("numero", valor=t[1])

def p_expresion_nombre(t):
    'expresion : IDENTIFICADOR'
    try:
        t[0] = NodoAST("identificador", valor=nombres[t[1]])
    except LookupError:
        print(f"Error semántico: Variable '{t[1]}' no declarada.")
        t[0] = NodoAST("identificador", valor=None)

# Regla para manejar expresiones entre paréntesis
def p_expresion_grupo(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_error(t):
    if t:
        print(f"Error sintáctico en el valor {t.value}")
    else:
        print("Error sintáctico inesperado")

parser = yacc.yacc()

def graficar_ast(nodo, dot=None, contador=0):
    if dot is None:
        dot = graphviz.Digraph(comment="Árbol de Sintaxis Abstracto")

    nodo_id = str(contador)
    label = f"{nodo.tipo}\n{nodo.valor}" if nodo.valor else nodo.tipo
    dot.node(nodo_id, label)

    for hijo in nodo.hijos:
        contador += 1
        hijo_id = str(contador)
        dot.edge(nodo_id, hijo_id)
        contador = graficar_ast(hijo, dot, contador)

    return contador

def prueba_sintactica(data):
    # Análisis léxico
    print("Análisis léxico:")
    analizador.input(data)
    
    while True:
        tok = analizador.token()
        if not tok:
            break
        print(tok)

    # Análisis sintáctico
    ast = parser.parse(data)
    if ast:
        dot = graphviz.Digraph(comment="Árbol de Sintaxis Abstracto")
        graficar_ast(ast, dot)
        dot.render("ast_output", format="png", cleanup=True)
        print("Árbol de sintaxis generado y guardado como 'ast_output.png'.")
    else:
        print("No se pudo generar el árbol de sintaxis.")

if __name__ == "__main__":
    while True:
        try:
            s = input('>>> ')
        except EOFError:
            break
        if not s: continue
        prueba_sintactica(s)