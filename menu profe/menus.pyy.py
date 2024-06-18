#Menu bienvenida
import funciones 
while True:
    print("********************************");
    print("Bienvenido al menu empresa duoc");
    print("********************************");
    print("1-.Ingresar el trabajador.");
    print("2-.Listar todos los trabajadores.");
    print("3-.Imprimir planilla de sueldos.");
    print("4-.Salir del programa.");
    try:
        opc=int(input("Ingrese una opcion-->"));
    except ValueError:
        print("Error ingrese un nunero del 1 al 4.");
    else:
        if (opc==1):
            while True:
                try:
                    nombre=print("Ingrese el nombre del trabajador.")
                    input("-->");
                    cargo=print("Ingrese el cargo del trabajador.");
                    input("-->");
                    sueldo_Bruto=print("Ingrese el sueldo bruto del trabajador.");
                    input("-->");
                    descSalud=print("Ingrese el descuento de salud del trabajador.");
                    input("-->");
                    descAfp=print("Ingrese el descuento de la afp del trabajador.");
                    input("-->");
                    liquidoapagar=print("Ingrese el saldo liquido a pagar del trabajador.");
                    input("-->");
                    with open("datostrabajadores.txt",'w') as file:
                        file.write(f"{nombre}");
                        file.write(f"{cargo}");
                        file.write(f"{sueldo_Bruto}");
                        file.write(f"{descSalud}");
                        file.write(f"{descAfp}");
                        file.write(f"{liquidoapagar}");
                except ValueError:
                    print("Error ingrese los datos nuevamente.");
                    break;
                else:
                     if (opc==2):
                         while True:
                                try:
                                    print(f"la lista es {trabajador}:");
                                except ValueError:
                                 print("Error ingrese los datos nuevamente.");
                                else:
                                    if (opc==3):
                                        while True:
                                             try:
                                                 print(f"{trabajador}");
                                             except ValueError:
                                                 print("Error ingrese los datos nuevamente.");
                                                 trabajadores=
                                                 for trabajador in trabajadores:
                                                     print(trabajador)
                                                     #Creamos un diccionario con la información del trabajador
                                                     lista_trabajadores =[]
                                                     while True:
                                                        num_trabajadores = int(input("¿Cuántos trabajadores deseas ingresar? "))
                                                        for i in range (num_trabajadores):
                                                            print(f"\nIngresando datos para el trabajdor {i+1}")
                                                            nombre = input("Nombre:")
                                                            cargo  = input("Cargo:")
                                                            sueldo_Bruto = int(input("sueldo bruto:"))
                                                            descSalud =
                                                            int(input("descSalud:"))
                                                            descAfp =
                                                            int(input("descAfp:"))
                                                            liquidoapagar = sueldo_Bruto
                                                            descSalud - descAfp

                                                            trabajador = {
                                                                "nombre": nombre
                                                                "cargo":
                                                                "sueldo Bruto":
                                                                "Descuento Salud":
                                                                descSalud,
                                                                "descAfp":descAfp,
                                                                "liquidoapagar":
                                                                sueldo_liquido
                                                                    }
                                                        lista_trabajadores.append(trabajador)
                                                        print("\nLista de trabajadores:")
                                                        for trabajador in lista_trabajadores:
                                                            print(trabajador)
                                                                


                                                            



                                                        

                                            
                                        