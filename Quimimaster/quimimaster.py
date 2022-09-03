# Definir la clase que voy a usar para agregar cada elemento en una variable cada uno
class Elemento:
    def __init__(self, nombre, simbolo, exponente, Z, A, tipo):
        self.nombre = nombre
        self.simbolo = simbolo
        self.exponente = exponente
        self.A = A
        self.Z = Z
        self.tipo = tipo
        self.electrones = Z - exponente
        self.neutrones = A - Z
        self.protones = Z


# La idea de la variable exp es que mÃ¡s adelante la introduzca el usuario junto con el nombre o sÃ­mbolo del elemento que quiere consultar
exp = 0
Hidrogen = Elemento("Hidrógeno", "H", exp, 1, 1, "no metal")
Helium = Elemento("Helio", "He", exp, 2, 4, "gas noble")
Litium = Elemento("Litio", "Li", exp, 3, 7, "metal alcalino")
Berilium = Elemento("Berilio", "Be", exp, 4, 9, "alcalinotÃ©rreo")
Boron = Elemento("Boro", "B", exp, 5, 11, "metaloide")
Carbon = Elemento("Carbono", "C", exp, 6, 12, "no metal")
Nitrogen = Elemento("Nitrógeno", "N", exp, 7, 14, "no metal")
Oxygen = Elemento("Oxígeno", "O", exp, 8, 16, "no metal")
Fluorine = Elemento("Flúor", "F", exp, 9, 19, "halógeno")
Neon = Elemento("Neon", "Ne", exp, 10, 20, "gas noble")
Sodium = Elemento("Sodio", "Na", exp, 11, 23, "metal alcalino")
Magnesium = Elemento("Magnesio", "Mg", exp, 12, 24, "alcalinotérreo")
Aluminum = Elemento("Aluminio", "Al", exp, 13, 27, "otro metal")
Silicon = Elemento("Silicio", "Si", exp, 14, 28, "metaloide")
Phosphorus = Elemento("Fósforo", "P", exp, 15, 31, "no metal")
Sulfur = Elemento("Azufre", "S", exp, 16, 32, "no metal")
Chlorine = Elemento("Cloro", "Cl", exp, 17, 35, "halógeno")
Argon = Elemento("Argón", "Ar", exp, 18, 40, "gas noble")
Potassium = Elemento("Potasio", "K", exp, 19, 39, "metal alcalino")
Calcium = Elemento("Calcio", "Ca", exp, 20, 40, "alcalinotérreo")
Scandium = Elemento("Escandio", "Sc", exp, 21, 45, "metal de transición")
Titanium = Elemento("Titanio", "Ti", exp, 22, 48, "metal de transición")
Vanadium = Elemento("Vanadio", "V", exp, 23, 51, "metal de transición")
Chrome = Elemento("Cromo", "Cr", exp, 24, 52, "metal de transición")