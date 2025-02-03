import unittest

# Funciones a probar
def isnumber(a):
    try: 
        float(a) 
        return True 
    except ValueError: 
        return False

def division(a, b):
    """División de dos números, con control de división por cero."""
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b


class TestCalculadora(unittest.TestCase):

    # Pruebas para la función isnumber (Caja Negra)
    def test_isnumber_valid_numbers(self):
        # Casos con números válidos
        self.assertTrue(isnumber(10))          # 10 es un número
        self.assertTrue(isnumber(-5))          # -5 es un número
        self.assertTrue(isnumber(3.14))        # 3.14 es un número decimal
        self.assertTrue(isnumber('123'))       # '123' se puede convertir a número
        self.assertTrue(isnumber('3.14'))      # '3.14' se puede convertir a número

    def test_isnumber_invalid_values(self):
        # Casos con valores no numéricos
        self.assertFalse(isnumber('abc'))      # 'abc' no es un número
        self.assertFalse(isnumber('hello'))    # 'hello' no es un número
        self.assertFalse(isnumber([1, 2, 3]))  # Lista no es un número
        self.assertFalse(isnumber({'key': 'value'}))  # Diccionario no es un número

    # Pruebas para la función division (Caja Negra)
    def test_division_valid(self):
        # Casos de división válidos
        self.assertEqual(division(10, 2), 5.0)          # 10 / 2 = 5.0
        self.assertEqual(division(-9, 3), -3.0)         # -9 / 3 = -3.0
        self.assertEqual(division(6.0, 2), 3.0)         # 6.0 / 2 = 3.0
        self.assertEqual(division(0, 10), 0.0)          # 0 / 10 = 0.0

    def test_division_by_zero(self):
        # Caso de división por cero
        self.assertEqual(division(10, 0), "Error: No se puede dividir entre cero.")  # División por cero

if __name__ == '__main__':
    unittest.main()

