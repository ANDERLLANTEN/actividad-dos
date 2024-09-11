

# 1. Conversión de tipos de datos (Enteros, Decimales y Cadenas)
def conversion_de_tipos():
    # Enteros
    entero = 10
    print("Entero:", entero)

    # Decimales
    decimal = 10.5
    print("Decimal:", decimal)

    # Cadenas
    cadena = "Hola, mundo!"
    print("Cadena:", cadena)

    # Conversión de Entero a Cadena
    entero_a_cadena = str(entero)
    print("Entero a Cadena:", entero_a_cadena)

    # Conversión de Cadena a Entero
    cadena_a_entero = int(entero_a_cadena)
    print("Cadena a Entero:", cadena_a_entero)

    # Conversión de Decimal a Entero
    decimal_a_entero = int(decimal)
    print("Decimal a Entero:", decimal_a_entero)

    # Conversión de Entero a Decimal
    entero_a_decimal = float(entero)
    print("Entero a Decimal:", entero_a_decimal)


# 2. Multilíneas de cadenas
def cadenas_multilinea():
    multilinea = """Esta es una cadena de texto
que abarca varias líneas.
Puedes escribir lo que quieras aquí,
y se conservará el formato original."""
    print("\nCadena Multilínea:\n", multilinea)


# 3. Función len()
def longitud_cadena():
    cadena = "Hola, mundo!"
    longitud = len(cadena)
    print("\nLongitud de la cadena '{}':".format(cadena), longitud)


# 4. Sub cadenas
def sub_cadenas():
    cadena = "Hola, mundo!"

    # Obtener los primeros n caracteres de una cadena
    n = 5
    primeros_n = cadena[:n]
    print("\nPrimeros {} caracteres:".format(n), primeros_n)

    # Obtener los caracteres de en medio de una cadena
    inicio = 6
    fin = 11
    en_medio = cadena[inicio:fin]
    print("Caracteres del medio (de {} a {}):".format(inicio, fin), en_medio)

    # Obtener los últimos n caracteres de una cadena
    n = 6
    ultimos_n = cadena[-n:]
    print("Últimos {} caracteres:".format(n), ultimos_n)


# 5. Función upper() y lower()
def manipular_cadenas():
    cadena = "Hola, Mundo!"

    # Convertir a mayúsculas
    mayusculas = cadena.upper()
    print("\nCadena en mayúsculas:", mayusculas)

    # Convertir a minúsculas
    minusculas = cadena.lower()
    print("Cadena en minúsculas:", minusculas)


# 6. Función strip()
def funcion_strip():
    cadena_con_espacios = "   Hola, mundo!   "
    # Eliminar espacios al inicio y al final
    cadena_sin_espacios = cadena_con_espacios.strip()
    print("\nCadena con espacios eliminados:", cadena_sin_espacios)


# 7. Función replace()
def funcion_replace():
    cadena = "Hola, mundo!"
    # Reemplazar 'mundo' por 'Python'
    cadena_reemplazada = cadena.replace("mundo", "Python")
    print("\nCadena después de reemplazar 'mundo' por 'Python':", cadena_reemplazada)


# 8. Función split()
def funcion_split():
    cadena = "Hola, mundo, Python"
    # Dividir la cadena en una lista de subcadenas usando la coma como delimitador
    partes = cadena.split(", ")
    print("\nCadena dividida en partes:", partes)


# 9. Formato de cadenas F-String
def formato_fstring():
    nombre = "Mundo"
    lenguaje = "Python"
    # Usar F-Strings para formatear la cadena
    mensaje = f"Hola, {nombre}! Estás aprendiendo {lenguaje}."
    print("\nMensaje formateado con F-String:", mensaje)


# Ejecutar ejemplos
if __name__ == "__main__":
    conversion_de_tipos()
    cadenas_multilinea()
    longitud_cadena()
    sub_cadenas()
    manipular_cadenas()
    funcion_strip()
    funcion_replace()
    funcion_split()
    formato_fstring()
