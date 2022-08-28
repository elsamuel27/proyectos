def sqrt(num):
    return num ** 0.5


class Ecuaciones2Grado:
    def calcular(self, A, B, C):
        if ((B**2)-4*A*C) < 0:
            print("No es posible sacar raíz cuadrada de un número negativo, operación cancelada")
        else:
            x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
            x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
            print(f"""\
            Las soluciones de la ecuación son: 
            x1 = {x1}
            x2 = {x2}
            """)


class Circulo:
    pi = 3.1415

    def __init__(self, radio: float):
        self.radio = radio

    def obtener_area(self):
        print(self.pi * self.radio ** 2)

    def obtener_diametro(self):
        print(self.radio * 2)


print("Bienvenido a la calculadora del samuel\nEscribe la operación que quieras realizar")
print("a: Resolver una ecuación de segundo grado")
print("b: Obtener valor de un círculo a partir de su radio")
print("c: Resolver una función")
problema = input()

if problema == "a":
    try:
        print("Introduce los siguientes valores")
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))

        ec = Ecuaciones2Grado()
        ec.calcular(a, b, c)

    except:
        print("Has puesto un valor un poco extraño. Sólo se admiten decimales")

elif problema == "b":
    print("¿Qué valor quieres sacar?")
    print("1: Área")
    print("2: Diámetro\n")
    valor = input()

    if valor == "1":
        try:
            x = float(input("Introduce el radio de un círculo: "))
            a = Circulo(x)
            a.obtener_area()

        except:
            print("Has puesto un valor un poco extraño. Sólo se admiten decimales")

    elif valor == "2":
        try:
            x = float(input("Introduce el radio de un círculo: "))
            a = Circulo(x)
            a.obtener_diametro()

        except:
            print("Has puesto un valor un poco extraño. Sólo se admiten decimales")
