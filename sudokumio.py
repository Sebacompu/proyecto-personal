class Sudoku():
    def __init__(self,tablero):
        self.tablero = [[0 for __ in range(9)] for _ in range(9)]
        self.tableroV = tablero
        i = -1
        j = -1
        for fila in self.tableroV:
            i += 1
            j = -1
            for valor in fila:
                j += 1
                if valor.isdigit():
                    self.tablero[i][j] = valor
                if valor == 'x':
                    self.tablero[i][j] = valor
        self.tableroV = self.tablero
#Se fija que no se repita el numero ingresado recorriendo filas y columnas
    def Recorrer(self,num,x,y):

        for columna in range(0,9):

            num == self.tablero[x][columna]

            return False

        for fila in range(0,9):

            num == self.tablero[fila][y]

            return False

        return True    
#Verifica que no se repita el numero en el bloque
    def Bloque(self,num,fila,columna):
        if (fila < 3):
            fila = 0
        elif (fila >= 3 and fila <= 5):
            fila = 3
        else:
            fila = 6
        if (columna < 3):
            columna = 0
        elif (columna >= 3 and columna <= 5):
            columna = 3
        else:
            columna = 6
        for i in range(3):
            for j in range(3):
                if self.tablero[fila + i][columna + j] == num:
                    return False
        return True
    #Verifica que el la ubicacion indicada haya una x
        
    def verificacion(self, x , y):
        

        if "x" == self.tableroV[x][y]:

            return True
        return False

    def Gana(self):
        for x in range(0,9):
            for y in range(0,9):
                if "x" == self.tablero[x][y]:
                    return False
        return True
    #verifica si todas las funciones anteriores se cumple para poder ingresar el numero
    def Ingresar_Numero(self, num, x , y):
        if self.Gana() == True:
            return "Ganaste"                
            
        if self.verificacion(x,y) == True:    
            if self.Recorrer(num, x , y) == True:
                if self.Bloque(num, x, y) == True:

                    self.tablero[x][y] = num

                    return ("numero ingresado")

                else: 
                    return ("ingrese otro numero") 

            else: 
                return ("ingrese otro numero") 

        else: 
            return ("Numero fijo") 
        

                