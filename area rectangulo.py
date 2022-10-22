# Hacer un programa que te calcule el área de un rectángulo, de un cuadrado y de un círculo
# esto tiene que ser usando funciones como en el ejemplo de abajo 

#ejemplo:

def area_rectangulo(altura, base):
    print("el área del rectángulo con altura =", altura,"y con base =",base,"tiene un área:",altura*base)


base = int(input("¿Cuanto mide la base?\n"))
altura = int(input("¿Cuanto mide la altura?\n"))

area_rectangulo(altura, base)


