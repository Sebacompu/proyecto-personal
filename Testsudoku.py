import unittest
from parameterized import parameterized
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
    
    @parameterized.expand([
        ('6', 7, 0),
        ('8', 8, 0),
        ('9', 8, 3),
        ('6', 6, 0),
        ('6', 6, 3),
        ('3', 0, 2),
        ('7', 0, 3),
        ('5', 1, 7),
        ('8', 3, 2),
        ('2', 6, 2)])
    def test_fila_invalida(self, num, fila, columna):
        self.assertEqual(self.juego.Ingresar_Numero(num, fila, columna), "Ingrese un numero correcto")

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

        self.assertEqual(False, self.juego.Gana())

    @parameterized.expand([
        ('8', 0, 2),
        ('6', 3, 1),
        ('1', 8, 3),
        ('7', 5, 7),
        ('1', 6, 3),
        ('2', 6, 5),
        ('3', 0, 5),
        ('9', 0, 8),
        ('6', 7, 0),
        ('2', 8, 6)])
    def test_columna_invalida(self, num, fila, columna):
        self.assertEqual(self.juego.Ingresar_Numero(num, fila, columna), "Ingrese un numero correcto")

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

        self.assertEqual(False, self.juego.Gana())

    @parameterized.expand([
        ('1', 0, 2),
        ('5', 3, 1),
        ('2', 8, 3),
        ('1', 5, 7),
        ('3', 6, 3)])
    def test_FilaYColumna_correcto(self, num, fila, columna):
        self.assertTrue(self.juego.FilaYColumna(fila, columna, num))

    @parameterized.expand([
        ('6', 0, 6),
        ('5', 8, 6),
        ('4', 8, 5),
        ('3', 5, 3),
        ('1', 5, 7),
        ('6', 5, 6),
        ('8', 2, 5),
        ('9', 6, 8),
        ('3', 0, 2),
        ('8', 8, 1),])
    def test_bloque_invalida(self, num, fila, columna):
        self.assertEqual(self.juego.Ingresar_Numero(num, fila, columna), "Ingrese un numero correcto")

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

        self.assertEqual(False, self.juego.Gana())

    @parameterized.expand([
        ('2', 0, 2),
        ('3', 0, 6),
        ('1', 8, 0),
        ('1', 8, 6),
        ('5', 3, 1)])
    def test_bloque_Valida(self, num, fila, columna):
        self.assertTrue(self.juego.Bloque(num, fila, columna))

    @parameterized.expand([
        ('4', 3, 4),
        ('6', 3, 8),
        ('1', 4, 0),
        ('5', 4, 3),
        ('9', 0, 0),
        ('2', 1, 5),
        ('7', 4, 0),
        ('3', 7, 4),
        ('7', 2, 7),
        ('2', 4, 3)])
    def test_valor_fijo(self, num, fila, columna):
        self.assertEqual(self.juego.Ingresar_Numero(num, fila, columna), "Numero Fijo")

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

        self.assertEqual(False, self.juego.Gana())

    @parameterized.expand([
        ('2', 0, 2),
        ('4', 1, 1),
        ('1', 8, 2),
        ('3', 7, 7),
        ('4', 0, 8)])
    def test_numero_ingresado(self, num, fila, columna):
        self.assertEqual(self.juego.Ingresar_Numero(num, fila, columna), "Numero Correcto")

        self.assertEqual(False, self.juego.Gana())

    def test_Gana(self):
        self.juego = Sudoku([
            '531171111',
            '611195111',
            '198111161',
            '811161113',
            '411813111',
            '711121116',
            '161111281',
            '111419115',
            '111181171'
        ])

        self.assertTrue(self.juego.Gana())


if __name__ == "__main__":
    unittest.main()

    