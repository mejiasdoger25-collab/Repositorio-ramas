print("Este programa es un test")

resultado = True

while resultado:

    x = int(input("Indique que número el número a revisar:"))

    if (1 <= x <= 10): 
        resultado = True
        print('La variable se encuentra entre 0 y 10')

    # Code solucionado
    else: 
        # Sample code:
        resultado = False
        print('La variable no se encuentra en 0 y 10')

print ("Se termina el test.")
