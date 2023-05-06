import os
class Menu():

    def mostrarMenu(self):
        os.system('cls')
        op = int (input('''
--------------->Menu Principal<---------------

1. Hacer Carga (test)
2. Mostrar mayor y menor por variable(3.1)
3. Mostar temperatura promedio del mes (3.2)
4. Ver valores por dia (3.3)
0. Salir

Su opcion: '''))
        return op
    
    def manejadorMenu(self, op, xVM): ## xVM = manejador Variables Meteorologicas
        if op == 1:
            self.opc1(xVM)
        
        elif op == 2:
            self.opc2(xVM)

        elif op == 3:
            self.opc3(xVM)

        elif op == 4:
            self.opc4(xVM)
        
        else:
            print ('saliendo...')
            os.system('pause')

    def opc1(self, xVM):
        xVM.cargarDatos()

    def opc2 (self, xVM):
        xVM.mostrarMayoryMenor()
        os.system('pause')

    def opc3 (self, xVM):
        r = xVM.calcularPromedioMes()
        print ('La Temperatura promedio del mes es: {0:.2f}°'.format(r))
        os.system('pause')

    def opc4 (self, xVM):
        os.system('cls')
        xop = int (input ('Ingrese día del mes que desea listar: '))
        xVM.listarPorDia(xop-1)
        os.system('pause')
