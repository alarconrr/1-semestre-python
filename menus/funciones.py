###Funciones Planilla
import csv
trabajadores=[];

def registrarTrabajador():
    while True:
        try:
            nombre=input("Ingrese el nombre y el apellido del trabajador:  ");
        except ValueError:
            print("error ingrese nuevamente el nombre y apellido.");
        else:
            try:
                while True:
                    cargo=input("Ingrese el cargo del trabajador (CEO), (Desarrollador) o (Analista):  ");
                    if (cargo == "CEO") or (cargo == "Desarrollador") or (cargo == "Analista"):
                        break;
                    else:
                        print ("Ingrese un cargo válido.");
            except TypeError:
                print("Error ingrese nuevamente el cargo.");
            else:
                try: 
                    sueldoBruto=int(input("Ingrese el sueldo del trabajador:  "));
                except ValueError:
                    print("Error ingrese nuevamente el sueldo :<");
                else:
                    break;

    if(cargo=='CEO'):
        descSalud=sueldoBruto*0.07;
        descAfp=sueldoBruto*0.12;
    elif(cargo=='Desarrollador'):   
        descSalud=sueldoBruto*0.05;
        descAfp=sueldoBruto*0.10;
    elif(cargo=='Analista'):
        descSalud=sueldoBruto*0.06;
        descAfp=sueldoBruto*0.11;

    liquidoPagar=(sueldoBruto-descSalud-descAfp);

    trabajador = {
    'nombre': nombre,
    'cargo': cargo,
    'sueldoBruto': sueldoBruto,
    'descSalud': descSalud,
    'descAfp': descAfp,
    'liquidoPagar': liquidoPagar
    }
    trabajadores.append(trabajador);
    print("Trabajador registrado exitosamente.\n");
    return;
    
def mostrarlista():
    if not trabajadores:
        print("no se encuentran trabajadores registrados 0-0");
    else:
        print("Listado de trabajadores:");
        for trabajador in trabajadores:
            print(f"Nombre: {trabajador['nombre']}, Cargo: {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldoBruto']},Descuento AFP: {trabajador['descAfp']}, Descuento salud: {trabajador['descSalud']} Líquido a Pagar: {trabajador['liquidoPagar']}");

def imprimirPlanilla():
    if not trabajadores:
        print("No se encuentran trabajadores registrados.");
        return;
    
    print("\n¿De quién desea imprimir la planilla?");
    try:
        decisionPlanilla = input("\n1.- CEO\n2.- Desarrollador\n3.- Analista\nIngrese su decisión: ");
    except ValueError:
        print ("Ingrese una opción válida");
    else:
        if decisionPlanilla == '1':
            cargo = 'CEO';
        elif decisionPlanilla == '2':
            cargo = 'Desarrollador';
        elif decisionPlanilla == '3':
            cargo = 'Analista';
        else:
            print("Opción no válida");
            return;

        with open(f"Planilla_Trabajadores_{cargo}.txt", 'w') as planilla_trabajadores:
            for trabajador in trabajadores:
                if trabajador['cargo'] == cargo:
                    planilla_trabajadores.write(f"Nombre: {trabajador['nombre']}, Cargo: {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldoBruto']}, Desc. Salud: {trabajador['descSalud']}, Desc. AFP: {trabajador['descAfp']}, Líquido a Pagar: {trabajador['liquidoPagar']}\n");
                    print(f"Planilla de sueldos para el cargo {cargo} generada exitosamente.");
        
        print(f"\nContenido de la planilla para el cargo {cargo}:\n");
        try:
            with open(f"Planilla_Trabajadores_{cargo}.txt", 'r') as planilla_trabajadores:
                contenido = planilla_trabajadores.read();
                print(contenido);
        except FileNotFoundError:
            print(f"No se encontró la planilla para el cargo {cargo}. Verifique que haya sido generada previamente.");
