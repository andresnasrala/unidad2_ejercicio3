class Registro():
    __temperatura = int
    __humedad = int
    __presion = int

    def __init__(self, temperatura=0, humedad=0, presion=0):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion

    def getPresion(self):
        return self.__presion
    
    def getTemperatura (self):
        return self.__temperatura
    
    def getHumedad (self):
        return self.__humedad