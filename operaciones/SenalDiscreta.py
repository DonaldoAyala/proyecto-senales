class SenalDiscreta:

    # Constructor
    # Si no se envían argumentos, se asignan los valores por defecto
    # Solo un dato = 0, indice de inicio = 0, tipo de señal = finita = no periódica
    def __init__(self, datos = [0], indice_inicio = 0, periodica = False):
        self.datos = datos
        self.indice_inicio = indice_inicio
        self.periodica = periodica

    def es_periodica (self) -> bool:
        if ( self.periodica ):
            return True
        else:
            return False

    def es_finita (self) -> bool:
        if ( self.periodica ):
            return False
        else:
            return True

    def obtener_longitud (self) -> int:
        return len(self.datos)

    def obtener_datos (self):
        return self.datos

    def asignar_datos (self, datos):
        self.datos = datos

    def obtener_indice_inicio (self) -> int:
        return self.indice_inicio

    def asignar_indice_inicio (self, indice_inicio):
        self.indice_inicio = indice_inicio

    def __str__(self):
        return str(self.datos) + " inicio: " + str(self.indice_inicio) + " periodica: " + str(self.periodica)
