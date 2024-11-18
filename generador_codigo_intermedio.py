class GeneradorCodigoIntermedio:
    def __init__(self):
        self.codigo_intermedio = []
        self.temporales = 0

    def generar_temporal(self):
        """Genera un nuevo temporal"""
        self.temporales += 1
        return f"t{self.temporales}"

    def generar(self, nodo):
        """Genera código intermedio a partir del AST"""
        if nodo.tipo == "numero":
            return str(nodo.valor)
        elif nodo.tipo == "identificador":
            return nodo.valor
        elif nodo.tipo == "operacion":
            izq = self.generar(nodo.hijos[0])
            der = self.generar(nodo.hijos[1])
            temp = self.generar_temporal()
            self.codigo_intermedio.append(f"{temp} = {izq} {nodo.valor} {der}")
            return temp
        elif nodo.tipo == "asignacion":
            identificador = nodo.hijos[0].valor
            expresion = self.generar(nodo.hijos[1])
            self.codigo_intermedio.append(f"{identificador} = {expresion}")

    def obtener_codigo(self):
        """Devuelve el código intermedio generado"""
        return "\n".join(self.codigo_intermedio)
