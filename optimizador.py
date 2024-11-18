class Optimizador:
    def __init__(self, codigo_intermedio):
        self.codigo_intermedio = codigo_intermedio.splitlines()

    def optimizar(self):
        """Aplica optimizaciones simples al código intermedio"""
        optimizado = []
        for linea in self.codigo_intermedio:
            # Eliminar operaciones redundantes (x = x + 0, etc.)
            if "+ 0" in linea or "- 0" in linea:
                optimizado.append(linea.replace(" + 0", "").replace(" - 0", ""))
            elif "* 1" in linea or "/ 1" in linea:
                optimizado.append(linea.replace(" * 1", "").replace(" / 1", ""))
            elif "* 0" in linea:
                partes = linea.split("=")
                optimizado.append(f"{partes[0].strip()} = 0")
            else:
                optimizado.append(linea)
        return "\n".join(optimizado)
