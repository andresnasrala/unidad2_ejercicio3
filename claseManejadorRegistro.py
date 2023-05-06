import csv
import os
from claseManejadorRegistro import Registro

class manejadorRegistro():
    __fila = 0
    __columna = 0
    __lista = []

    def __init__(self, filas=30, columna=24):
        self.__fila = filas
        self.__columna = columna


    def mostrarDatos(self):
        for i in range (len(self.__lista)):
            for j in range (len(self.__lista[i])):
                print (self.__lista[i][j].getPresion())

    def cargarDatos (self):
        for i in range (30):
            lista=[]
            for j in range (24):
                lista.append(0)
            self.__lista.append(lista)
        bandera = True
        path = './Datos_Meteorologicos.csv'
        archivo = open(path, 'r')
        reader = csv.reader(archivo, delimiter =',')
        for fila in reader:
            dia = int(fila[0]) 
            hora = int(fila[1]) 
            temp = int(fila[2])
            hum = int(fila[3])
            pre = int(fila[4])
            xRegistro = Registro(temp, hum, pre)
            self.__lista[dia-1][hora] = xRegistro    
        print('Carga Lista!')
        os.system('pause')


    def mostrarMayoryMenor (self):
        os.system('cls')

        temperaturamadiama = 0
        humedadmadiama = 0
        presionmadiama = 0

        temperaturaminima = 9999
        humedadminima = 9999
        presionminima = 9999

        dia = 0 
        hora = 0 

        print ('---> VALORES MAdiaMOS <---')

        for i in range (len (self.__lista)):
            for j in range (len (self.__lista[i])):
                if (self.__lista[i][j].getTemperatura() > temperaturamadiama):
                    temperaturamadiama = self.__lista[i][j].getTemperatura()
                    dia = i+1
                    hora = j
        print (f'->La temperatura mádiama es {temperaturamadiama}. Del día: {dia} a la hora: {hora}')
        for i in range (len (self.__lista)):
            for j in range (len (self.__lista[i])):
                if (self.__lista[i][j].getHumedad() > humedadmadiama):
                    humedadmadiama = self.__lista[i][j].getHumedad()
                    dia = i+1
                    hora = j
        print (f'->La humedad mádiama es {humedadmadiama}. Del día: {dia} a la hora: {hora}')
        for i in range (len (self.__lista)):
            for j in range (len (self.__lista[i])):
                if (self.__lista[i][j].getPresion() > presionmadiama):
                    presionmadiama = self.__lista[i][j].getPresion()
                    dia = i+1
                    hora = j


        print (f'->La presion mádiama es {presionmadiama}. Del día: {dia} a la hora: {hora}')



        print ('''---> VALORES MINIMOS <--- ''')

        for i in range (len (self.__lista)):
            for j in range (len (self.__lista[i])):
                if (self.__lista[i][j].getTemperatura() < temperaturaminima):
                    temperaturaminima = self.__lista[i][j].getTemperatura()
                    dia = i+1
                    hora = j
        print (f'->La temperatura minima es {temperaturaminima}. Del día: {dia} a la hora: {hora}')


        for i in range (len (self.__lista)):
            for j in range (len (self.__lista[i])):
                if (self.__lista[i][j].getHumedad() < humedadminima):
                    humedadminima = self.__lista[i][j].getHumedad()
                    dia = i+1
                    hora = j
        print (f'->La humedad minima es {temperaturaminima}. Del día: {dia} a la hora: {hora}')



        for i in range (len (self.__lista)):
            for j in range (len (self.__lista[i])):
                if (self.__lista[i][j].getPresion() < presionminima):
                    presionminima = self.__lista[i][j].getPresion()
                    dia = i+1
                    hora = j
        print (f'->La presion minima es {temperaturaminima}. Del día: {dia} a la hora: {hora}')

    def calcularPromedioMes (self):
        audialiar = 0
        cont = 0



        for i in range (len(self.__lista)):
            for j in range (len (self.__lista[i])):
                audialiar += int (self.__lista[i][j].getTemperatura())
                cont += 1
        return float (audialiar / cont)
    


    def listarPorDia (self, dia):  
        print ('______________________________________________')
        print ('|{:^10} {:^10} {:^10} {:^10}|'. format('Hora', 'Temperatura', 'Humedad', 'Presion'))
        print ('|--------------------------------------------|')
        for j in range (len (self.__lista[dia])):
            print ('|{:^10} {:^10} {:^10} {:^10} |'. format(j, self.__lista[dia][j].getTemperatura(), self.__lista[dia][j].getHumedad(), self.__lista[dia][j].getPresion()))
        print ('|____________________________________________|\n')