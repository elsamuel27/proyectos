repetir = "s"
while repetir == "s":
    elementi = input("Nombre del elemento en inglés: ")
    element = elementi.replace("\"", "")
    elemento = input("Nombre del elemento en español: ")
    simbolo = input("Símbolo: ")
    Z = int(input("Z: "))
    A = int(input("A: "))
    tipo = input("Tipo: ")
    resultado = f"\n{element} = Elemento(\"{elemento}\", \"{simbolo}\", exp, {Z}, {A}, \"{tipo}\")"
    # ("Hidrógeno", "H", exp, 1, 1, "no metal")

    # prueba = open("prueba.txt", "a")
    # prueba.write(resultado)
    quimimaster = open("quimimaster.py", "a", encoding="utf-8")
    quimimaster.write(resultado)
    print("Hecho")
    repetir = input("¿Añadir otro? [s/n]: ")