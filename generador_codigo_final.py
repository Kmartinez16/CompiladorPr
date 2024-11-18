class GeneradorCodigoFinal:
    def __init__(self, codigo_intermedio):
        self.codigo_intermedio = codigo_intermedio.splitlines()
        self.codigo_final = []

    def traducir_a_codigo_final(self):
        """Convierte el código intermedio a instrucciones de máquina/hardware"""
        for linea in self.codigo_intermedio:
            # Convertir cada línea a pseudo-código ensamblador
            if "=" in linea:
                partes = linea.split("=")
                dest = partes[0].strip()
                expr = partes[1].strip()
                self.codigo_final.append(f"MOV {dest}, {expr}")
            elif "+" in linea or "-" in linea or "*" in linea or "/" in linea:
                # Instrucciones más complejas
                pass
        return "\n".join(self.codigo_final)
