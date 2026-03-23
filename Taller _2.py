# Semana 2: Anidaciones
import datetime

usuario_invitado = "invitado"
contraseña_invitado = "12345"
usuario_administrador = "administrador"
contraseña_administrador = "67890"

intentos = 0
rol = None
tiene_acceso = False

while intentos < 3 and not tiene_acceso:
    usuario = input("ingresa tu usuario: ").strip().lower()
    contraseña = input("ingresa tu contraseña: ").strip().lower()

    if usuario == usuario_administrador and contraseña == contraseña_administrador:
        rol = "administrador"
        print("inicio exitoso bienvenido")
        print(f"tu rol es: {rol}")
        tiene_acceso = True
        break

    elif usuario == usuario_invitado and contraseña == contraseña_invitado:
        rol = "invitado"
        print("inicio exitoso bienvenido")
        print(f"tu rol es: {rol}")
        tiene_acceso = True
        break

    else:
        intentos += 1
        print("datos incorrectos")

if rol is None:
    print("alerta usuario bloqueado. cerrando sistema")
    exit()

if tiene_acceso:
    print("Acceso concedido al menú principal.")
    historial_chat = [
        {
            "timestamp": "2026-03-23 17:22:09",
            "comando": "ping",
            "rol": "administrador",
            "descripcion": "se ha solicitado el comando ping",
        },
        {
            "timestamp": "2026-03-23 17:22:11",
            "comando": "pong",
            "rol": "administrador",
            "descripcion": "se ha solicitado el comando pong",
        },
        {
            "timestamp": "2026-03-23 17:22:15",
            "comando": "contar",
            "rol": "administrador",
            "descripcion": "Se ha solicitado contar las vocales y consonantes de la palabra soledad, el resultado fue 3 vocales y 4 consonantes",
        },
        {
            "timestamp": "2026-03-23 17:22:22",
            "comando": "fecha",
            "rol": "administrador",
            "descripcion": "[pseudoAgente] La fecha actual es: 2026-03-23 17:22:22",
        },
        {
            "timestamp": "2026-03-23 17:22:42",
            "comando": "validarcontraseña",
            "rol": "administrador",
            "descripcion": "La contraseña debe contener al menos 8 caracteres",
        }
    ]

    while True:
        print("Home de entrada")
        print(
            """
        Aqui se imprime el menu
        ping o pong
        contar
        fecha
        validarcontraseña
        calculadora
        historial
        salir
        """
        )

        mensaje = "se ha solicitado terminar la sesión"
        comando = input(
            "ingresar la solicitud que deseas realizar: "
        ).strip().lower()

        if comando == "ping":
            print("pong")
            mensaje = "se ha solicitado el comando ping"

        elif comando == "pong":
            print("ping!")
            mensaje = "se ha solicitado el comando pong"

        elif comando == "contar":
            palabra = input("ingresa una palabra: ").strip().lower()
            totalvocales = 0
            totalconsonantes = 0
            vocales = "aeiouAEIOU"

            for letra in palabra:
                if letra.isalpha():
                    if letra in vocales:
                        totalvocales += 1
                    else:
                        totalconsonantes += 1

            print(
                f"su palabra: {palabra} contiene {totalvocales} Vocales y tiene {totalconsonantes} consonantes"
            )
            mensaje = f"Se ha solicitado contar las vocales y consonantes de la palabra {palabra}, el resultado fue {totalvocales} vocales y {totalconsonantes} consonantes"

        elif comando == "fecha":
            if rol == "administrador":
                hoy = datetime.datetime.now()
                mensaje = f"[pseudoAgente] La fecha actual es: {hoy.strftime('%Y-%m-%d %H:%M:%S')}"
                print(mensaje)
            else:
                mensaje = "[Acceso negado] Este comando necesita permisos de administrador."
                print(mensaje)

        elif comando == "validarcontraseña":
            nuevacontraseña = input("Ingrese una nueva contraseña: ")
            if len(nuevacontraseña) < 8:
                mensaje = "La contraseña debe contener al menos 8 caracteres"
                print(mensaje)
            elif nuevacontraseña == usuario:
                mensaje = "La contraseña no puede ser igual al nombre de usuario"
                print(mensaje)
            else:
                mensaje = "contraseña valida"
                print(mensaje)

        elif comando == "calculadora":
            num1 = float(input("ingrese el primer numero: ").strip())
            operador = input("Ingresa el operador (+,-,*,/): ").strip()
            num2 = float(input("ingrese el segundo numero: "))

            if operador == "+":
                print("Resultado:", num1 + num2)
            elif operador == "-":
                print("Resultado:", num1 - num2)
            elif operador == "*":
                print("Resultado:", num1 * num2)
            elif operador == "/":
                if num2 == 0:
                    print("Error, no se puede dividir por cero")
                else:
                    print("Resultado:", num1 / num2)
            else:
                print("operador no valido")

            mensaje = "se ha realizado una operacion en la calculadora"

        elif comando == "historial":
            historial_all = input("¿Desea ver todo el historial? (s/n): ").strip().lower()

            if historial_all == "s":
                print(f"\n--- Historial completo ({len(historial_chat)} registros) ---")
                for registro in historial_chat:
                    print(
                        f"Timestamp: {registro['timestamp']}, Comando: {registro['comando']}, Rol: {registro['rol']}, Descripción: {registro['descripcion']}"
                    )

            elif historial_all == "n":
                limpiar = input("¿Desea limpiar el historial actual? (s/n): ").strip().lower()
                if limpiar == "s":
                    historial_chat.clear()
                    print("Historial actual limpiado.")

                elif limpiar == "n":
                    palabra = input("Ingresa la palabra clave a buscar: ").strip().lower()
                    if palabra:
                        resultados_busqueda = [
                            registro
                            for registro in historial_chat
                            if palabra in registro["descripcion"].lower()
                        ]
                        if resultados_busqueda:
                            print(f"\n--- Se encontraron {len(resultados_busqueda)} resultado(s) ---")
                            for registro in resultados_busqueda:
                                print(f"Rol: {registro['rol']}, Descripción: {registro['descripcion']}")
                        else:
                            print("[PseudoAgente] No encontré registros que coincidan con esa palabra.")
                    else:
                        print("[PseudoAgente] Debe ingresar una palabra para buscar.")
                else:
                    print("Comando no reconocido. Por favor, ingrese 's' o 'n'.")
            else:
                print("Comando no reconocido para historial. Por favor, ingrese 's' o 'n'.")

            mensaje = "se ha consultado el historial"

        elif comando == "salir":
            print("Apagando agente....")
            break

        else:
            mensaje = "Comando no reconocido"
            print("Comando no reconocido. Por favor, intente de nuevo.")

        d_log = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "comando": comando,
            "rol": rol,
            "descripcion": mensaje,
        }
        historial_chat.append(d_log)
else:
    print("Acceso denegado.")