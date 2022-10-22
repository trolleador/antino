import random
import time

valor_minimo = 1
valor_maximo = 16

juega_otra_vez = "si"

while(juega_otra_vez == "si" or juega_otra_vez == "s"):
    lados = int(input("Cuantos lados quieres que tenga el dado? Del 1 al 16\n"))
    if(valor_maximo>=lados and valor_minimo<=lados):
        print("Tirando dado...")
        time.sleep(1.5)
        resultado = range(1,lados+1)
        print(random.choice(resultado))
    juega_otra_vez = input("¿Quieres jugar otra vez?\n")

#end