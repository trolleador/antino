

import math




juega_otra_vez = "si"


def Area_Rectangulo():
    Altura = float(input("Cuanto mide la altura\n"))

    Base = float(input("Cuanto mide la base\n"))
    
    Calculacion = Altura*Base

    print("Los resultados son", Calculacion)

#funcion para el cuadrado, circulo y triangulos

def Area_Triangulo():
    Altura = float(input("Cuanto mide la altura\n"))
   
    Base = float(input("Cuanto mide la base\n"))

    Respuesta = Altura*Base/2

    print("Los resultados son", Respuesta)

def Area_Cuadrado():
    Lado = float(input("Cuanto mide el lado\n"))

    Area = Lado*Lado

    print("Los resultados son", Area)

def Area_Circulo():
    Radio = float(input("dime el radio\n"))

    Area = math.pi*(Radio**2)

    print("Los resultados son", Area)

while(juega_otra_vez == "si" or juega_otra_vez == "s"):

    #hacer casos para hacer 

    eleccion = input("¿A qué figura le quieres sacar el área?\n")

    match eleccion:
        case "cuadrado":
            Area_Cuadrado()

        case "circulo":
            Area_Circulo()
        
        case "triangulo":
            Area_Triangulo()

        case "rectangulo":
            Area_Rectangulo()

        case _ :
            print("no manejamos esa figura \n")

    juega_otra_vez = input("¿Quieres medir otra vez?\n")


#end)