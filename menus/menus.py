###Empresa DUOC
import funciones as func
import time
trabajadores=[];


while True:
    print("\nBienvenido a DUOC Empresa\n\nElija una opción:  ");
    print("1.- Registrar Trabajador");
    print("2.- Lista de trabajadores");
    print("3.- Imprimir planilla de sueldos");
    print("4.- Salir del programa");

    try:
        menuDecision = int(input("\nIngrese una opción: "));
    except ValueError:
        print("Error ingrese nuevamente. :(");
    else:
        if (menuDecision == 1):
            func.registrarTrabajador();
            trabajadores.append(trabajadores);
        elif (menuDecision == 2):
            func.mostrarlista();
        elif (menuDecision == 3):       
            func.imprimirPlanilla();
        elif (menuDecision == 4):
            print ("Saliendo...");
            time.sleep(2);
            break;
        else:
            print("Error ingrese nuevamente :<");