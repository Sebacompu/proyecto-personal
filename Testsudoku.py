import unittest
from sudokumio import Sudoku


class TestSudoku(unittest.TestCase):

    def setUp(self):
        self.juego = Sudoku([
            '53xx7xxxx',
            '6xx195xxx',
            'x98xxxx6x',
            '8xxx6xxx3',
            '4xx8x3xx1',
            '7xxx2xxx6',
            'x6xxxx28x',
            'xxx419xx5',
            'xxxx8xx79'
        ])


    #Compara el 5 con un valor de x
    def test_repeticion_fila(self):
        self.assertEqual(self.juego.Ingresar_Numero('7', 0, 2), "ingrese otro numero")
        self.assertEqual(self.juego.tablero, [ 
            ['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
           ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
           ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
           ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
           ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
           ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
           ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
           ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
           ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])

        

    def test_repeticion_en_bloque(self):
        self.assertEqual(self.juego.Ingresar_Numero("5",0,2), "ingrese otro numero")
        self.assertEqual(self.juego.tablero,[ 
            ['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
            ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
            ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
            ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
            ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
            ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
            ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
            ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
            ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])

    def test_repeticion_columna(self):
        self.assertEqual(self.juego.Ingresar_Numero('7', 2, 6), "ingrese otro numero")
        self.assertEqual(self.juego.tablero, [ 
            ['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
           ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
           ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
           ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
           ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
           ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
           ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
           ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
           ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])
    
    def test_verifica_si_hay_numero(self):
        self.assertEqual(self.juego.Ingresar_Numero('1', 5, 0), "Numero fijo")
        self.assertEqual(self.juego.tablero, [ 
            ['5', '3', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
           ['6', 'x', 'x', '1', '9', '5', 'x', 'x', 'x'],
           ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
           ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
           ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
           ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
           ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
           ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
           ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])

    def test_Ingresar_Numero(self):
        self.assertEqual("numero ingresado", self.juego.Ingresar_Numero('4', 0, 2))
        self.assertEqual("numero ingresado", self.juego.Ingresar_Numero('4', 1, 1))

        self.assertEqual(self.juego.tablero, [
            ['5', '3', '4', 'x', '7', 'x', 'x', 'x', 'x'],
            ['6', '4', 'x', '1', '9', '5', 'x', 'x', 'x'],
            ['x', '9', '8', 'x', 'x', 'x', 'x', '6', 'x'],
            ['8', 'x', 'x', 'x', '6', 'x', 'x', 'x', '3'],
            ['4', 'x', 'x', '8', 'x', '3', 'x', 'x', '1'],
            ['7', 'x', 'x', 'x', '2', 'x', 'x', 'x', '6'],
            ['x', '6', 'x', 'x', 'x', 'x', '2', '8', 'x'],
            ['x', 'x', 'x', '4', '1', '9', 'x', 'x', '5'],
            ['x', 'x', 'x', 'x', '8', 'x', 'x', '7', '9']])   
            
        self.assertEqual(False, self.juego.Gana())

    def test_Gana(self):
        self.juego = Sudoku([ 
            ['5', '3', '1', '1', '7', '1', '1', '1', '1'],
           ['6', '1', '1', '1', '9', '5', '1', '1', '1'],
           ['1', '9', '8', '1', '1', '1', '1', '6', '1'],
           ['8', '1', '1', '1', '6', '1', '1', '1', '3'],
           ['4', '1', '1', '8', '1', '3', '1', '1', '1'],
           ['7', '1', '1', '1', '2', '1', '1', '1', '6'],
           ['1', '6', '1', '1', '1', '1', '2', '8', '1'],
           ['1', '1', '1', '4', '1', '9', '1', '1', '5'],
           ['0', '1', '1', '1', '8', '1', '1', '7', '9']])
        self.assertEqual("Ganaste", self.juego.Ingresar_Numero("4",8,0))
        self.assertTrue(self.juego.Gana())




if __name__ == "__main__":
    unittest.main()
