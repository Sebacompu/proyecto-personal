from sudokumio import Sudoku
from Api import api


class Interfaz():

    def __init__(self):
        self.Su = Sudoku(api())

    def verificar_entero(self, n):
        return (0 < n < 10)
           
    def Recorrer(self, foc):
        return (0 <= foc < 9)
           

    def Play(self):
        print("         COMIENZA EL JUEGO")
        for i in range(0, 9):
            for j in range(0, 9):
                print(self.Su.tablero[i][j], end = " | " )
            print(" ")
            
       
        try:
            print("Ingrese fila donde desea poner el numero ( 0 a 8 )")
            f = input(">>")
            if self.Recorrer(int(f)) == True:
                print("Ingrese columna donde desea poner el numero ( 0 a 8 )")
                c = input(">>")
                if self.Recorrer(int(c)) == True:
                    print("Ingrese numero")
                    n = input(">>")
                    if self.verificar_entero(int(n)) == True:
                        print(self.Su.Ingresar_Numero(n, int(f), int(c)))
                    else:
                        print('Ingrese un numero correcto')
                else:
                    print('Ingrese un numero correcto')
            else:
                print('Ingrese un numero correcto')
        except Exception as w:
            print(w)
            print('Ingrese un numero correcto')

    

juego = Interfaz()

while juego.Su.Gana() is False:
    juego.Play()