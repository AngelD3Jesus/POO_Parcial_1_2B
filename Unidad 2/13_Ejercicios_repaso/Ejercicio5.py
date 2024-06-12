#5.- 
#Crear una lista y un diccionario con el contenido de esta tabla: 

#  ACCION              TERROR        DEPORTES
#  MAXIMA VELOCIDAD    LA MONJA       ESPN
#  ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#  RAPIDO Y FURIOSO I  LA MALDICION   ACCION

# Crear una lista con el contenido de la tabla

peliculas = [
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]
]

# Crear un diccionario con el contenido de la tabla
peliculas_dict = {
    "ACCION": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO I"],
    "TERROR": ["LA MONJA", "EL CONJURO", "LA MALDICION"],
    "DEPORTES": ["ESPN", "MAS DEPORTE", "ACCION"]
}

# Imprimir la información de la lista
print("Lista de Películas:")
for fila in peliculas:
    print("\t".join(fila))

# Imprimir la información del diccionario
print("\nDiccionario de Películas:")
for categoria, lista_peliculas in peliculas_dict.items():
    print(f"{categoria}: {', '.join(lista_peliculas)}")

