class Sudoku():
    
    def __init__(self, tablero):

        self.tablero = [[0 for __ in range(9)] for _ in range(9)]
        self.tableroV = [[0 for __ in range(9)] for _ in range(9)]
        i = -1
        j = -1
        for fila in tablero:
            i += 1
            j = -1
            for valor in fila:
                j += 1
                if valor.isdigit():
                    self.tablero[i][j] = valor
                    self.tableroV[i][j] = valor
                if valor == 'x':
                    self.tablero[i][j] = valor
                    self.tableroV[i][j] = valor

    def Bloque(self, num, fila, columna):

        # Se fija que el valor no se repita en el bloque

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

    def FilaYColumna(self, i, j, num):

        # Se fija que no se repita el valor en filas y columnas

        for columna in range(0, 9):
            if num == self.tablero[i][columna]:
                return False
        for fila in range(0, 9):
            if num == self.tablero[fila][j]:
                return False

        return True

    def verificar_x(self, i, j):
        if self.tableroV[i][j] == 'x':
            return True

        return False

    def Gana(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.tablero[i][j] == 'x':
                    return False

        return True

    def Ingresar_Numero(self, num, i, j):

        if self.Gana is True:
            return ' ¡Ganaste! '

        if self.verificar_x(i, j) is True:
            if self.FilaYColumna(i, j, num) is True:
                if self.Bloque(num, i, j) is True:
                    self.tablero[i][j] = num
                    return("Numero Correcto")

                else:
                    return("Ingrese un numero correcto")

            else:
                return("Ingrese un numero correcto")

        else:
            return("Numero Fijo")