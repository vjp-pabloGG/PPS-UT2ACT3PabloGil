def suma(a, b):
    """Suma de dos números."""
    return a + b

def resta(a, b):
    """Resta de dos números."""
    return a - b

def multiplicacion(a, b):
    """Multiplicación de dos números."""
    return a * b

def division(a, b):
    """División de dos números, con control de división por cero."""
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

def isnumber(a):
    try: 
        float(a) 
        return True 
    except ValueError: 
        return False

def mayorCero(a):
    """Indica si el número pasado es mayor que cero."""
    return a > 0

def calculadora():
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    operacion = input("Ingrese el número de la operación (1/2/3/4): ")

    if operacion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if operacion == '1':
            print("Resultado:", suma(num1, num2))
        elif operacion == '2':
            print("Resultado:", resta(num1, num2))
        elif operacion == '3':
            print("Resultado:", multiplicacion(num1, num2))
        elif operacion == '4':
            print("Resultado:", division(num1, num2))
    else:
        print("Operación no válida")

if __name__ == "__main__":
    calculadora()