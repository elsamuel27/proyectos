# Constantes
pi = 3.1415


# Función para raíces cuadradas
def sqrt(num):
    return num ** 0.5


# Clase para resolver ecuaciones de segundo grado
class Ecuaciones2Grado:
    def calcular(self, A, B, C):
        if ((B**2)-4*A*C) < 0:
            print("No es posible sacar raíz cuadrada de un número negativo, operación cancelada")
        else:
            x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
            x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
            print(f"Las soluciones de la ecuación son:\nx1 = {x1}\nx2 = {x2}")


# Clase para sacar valores de un Círculo
class Circulo:

    def __init__(self, radio: float):
        self.radio = radio

    def obtener_area(self):
        print("Área:", pi * self.radio ** 2)

    def obtener_diametro(self):
        print("Diámetro:", self.radio * 2)


print("Bienvenido a la calculadora del samuel\nElige el modo que quieres usar")
print("1 para matemáticas, 2 para física")
modo = int(input())
if modo == 1:
    print("a: Resolver una ecuación de segundo grado")
    print("b: Obtener diámetro y área de un círculo a partir de su radio")
    print("c: Aplicar teorema de pitágoras")
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
        try:
            x = float(input("Introduce el radio de un círculo: "))
            a = Circulo(x)
            a.obtener_diametro()
            a.obtener_area()
        except:
            print("Has puesto un valor un poco extraño. Sólo se admiten decimales")

    elif problema == "c":
        a = int(input("Escribe el cateto a: "))
        b = int(input("Escribe el cateto b: "))
        hipotenusa = sqrt((a ** 2) + (b ** 2))
        print("La hipotenusa es:", hipotenusa)

elif modo == 2:
    """
    Ahora está hecho así porque sólo hay hecha una función, para añadir más se haría como antes
    print("a: Calcular MRU")
    print("b: ???")
    print("c: ???")
    problema = input()
    if problema == "a":
        (Código de abajo sin el print inicial)
    if problema == "b":
        (Código que lo resuelva)
    etc
    """
    print("De momento sólo puedo calcular MRU, así que vamos a saltar a eso")
    x0 = int(input("Introduce la posición inicial: "))
    v = int(input("Introduce la velocidad: "))
    t = int(input("Introduce el tiempo: "))
    MRU = x0 + (v*t)
    print(f"La posición final es {MRU} metros")
    print(f"Distancia recorrida: {MRU - x0}")
