import os
from divice import Divice
from radio import Radio
from tv import TV
from smartTv import SmartTv
from remote import Remote
from advanceremote import AdvanceRemote


aceptado: bool = True
controlTipo: bool = True
dispositivo: Divice = TV()
control: Remote = AdvanceRemote(dispositivo)


def opciones():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
    print("Selecciona un dispositivo ")
    print("\t1 - Radio")
    print("\t2 - Television")
    print("\t3 - Smart Tv")
    print("\t0 - salir")


def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
    print("Selecciona una opcion ")
    print("\t1 - Toogle power")
    print("\t2 - Volume Up")
    print("\t3 - Volume Down")
    print("\t4 - Channel Up")
    print("\t5 - Channel Down")
    print("\t0 - salir")

def menu_control():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
    print("Selecciona una opcion ")
    print("\t1 - Control normal")
    print("\t2 - Control avanzado")
    print("\t0 - salir")


# menu para crear pedido
while aceptado:
    # Mostramos el menu
    opciones()

    # solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >> ")

    if opcionMenu == "1":
        dispositivo: Divice = Radio()
        break

    elif opcionMenu == "2":
        dispositivo: Divice = TV()
        break

    elif opcionMenu == "3":
        dispositivo: Divice = SmartTv()
        break

    elif opcionMenu == "0":
        aceptado = False
        break

    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


menu_control()

opcionMenu = input("elegir opcion")

if opcionMenu == "1":
    control: Remote = Remote(dispositivo)
    controlTipo = False
        
elif opcionMenu == "2":
    control: Remote = AdvanceRemote(dispositivo)
       
# menu para crear pedido
while aceptado == True:
    # Mostramos el menu
    menu()

    # solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >> ")

    if opcionMenu == "1":
        print("TOGGLEPOWER")
        control.togglepower()

    elif opcionMenu == "2":
        print("VOLUME UP")
        control.volume_up()

    elif opcionMenu == "3":
        print("VOLUME DOWN")
        control.volume_down()

    elif opcionMenu == "4":
        print("CHANNEL UP")
        control.channel_up()
        
    elif opcionMenu == "5":
        print("CHANNEL DOWN")
        control.channel_down()
        
    elif opcionMenu == "6":
        print("MUTE")
        if controlTipo==True:
            control.mute()
        else:
            print("Este control no tiene esa opcion")

    elif opcionMenu == "0":
        break

    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

    

