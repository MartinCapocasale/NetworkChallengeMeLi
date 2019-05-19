import scriptDiario
import scriptSemanal
import scriptMensual

def menu():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(raw_input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

salir = False
opcion = 0
while not salir:
    print ("1. Realizar backup diario de 5 archivos")
    print ("2. Realizar backup semanal de 1 archivo los dias Domingos")
    print ("3. Realizar backup mensual de 1 archivo el primer dia del mes")
    print ("4. Salir")
    print ("Seleccione una opcion")
    opcion = menu()
    if opcion == 1:
        print ("Opcion 1")
        scriptDiario.diario()
        break
    elif opcion == 2:
        print ("Opcion 2")
        scriptSemanal.semanal()
        break
    elif opcion == 3:
        print("Opcion 3")
        scriptMensual.mensual()
        break
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
print ("Fin")
