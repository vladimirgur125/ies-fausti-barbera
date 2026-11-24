print("Hola, bienvenido a nuestro banco")
saldo = float(input("Dime tu saldo actual: "))
accion = input("Que acción quieres hacer? \n 1-Ingresar \n 2-Sacar \n 3-Un prestamo \n:")

if accion == "1" :
    ingr = float(input("Cuánto dinero quieres ingresar? "))
    print (f"Ingresando {ingr} € \n Operación realizada")
    sal = saldo + ingr
    print (f"Saldo actualizado: {sal} €")
elif accion == "2" :
    saca = float(input("Que cantidad quieres sacar? "))
    if saca > saldo :
        print (f"No tienes tanto dinero en la cuenta")
    else :
        sa = saldo - saca
        print (f"Operación aceptada, has sacado {saca} euros \nSaldo actual: {sa} €")
elif accion == "3" :
    prest = float(input("De cuanto dinero quieres el préstamo? "))
    sald = saldo + prest
    print (f"El préstamo se ha pedido con éxito \nSaldo actual: {sald} €")
else :
    print (f"No existe esta opción \nSaldo actual: {saldo} €")
print (f"Gracias por utilizar el cajero, hasta la próxima")