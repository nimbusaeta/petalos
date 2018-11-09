import re # Importamos re, una librería que nos va a permitir trabajar con regex

archivo_sustantivos = open("0101_raw_rae.txt", "r") # Abrimos el archivo en que hemos guardado la lista de sustantivos
lista_sustantivos = archivo_sustantivos.readlines() # Guardamos cada línea en la lista lista_sustantivos
archivo_sustantivos.close() # Cerramos el archivo

lista_sustantivos_limpia = [] # Declaramos la lista en la que guardaremos los sustantivos una ves limpitos
for linea in lista_sustantivos:
	linea = re.sub("    ", "", linea) # Porque salen 4 espacios al principio cuando copipegas desde la web de la RAE
	linea = re.sub(", la", "", linea) # Quitamos la marca de género femenino
	linea = re.sub(".*?-.*?\n", "", linea) # No nos interesan sufijos ni prefijos, así que eliminamos toda línea que contenga un guion
	linea = re.sub("1;.*?\n", "\n", linea) # Nos quedamos con solo una de las entradas con varias etimologías
	lista_sustantivos_limpia.append(linea) # Metemos cada línea, que ahora ya contiene un sustantivo limpio, en la lista lista_sustantivos_limpia

archivo_sustantivos_limpios = open("0103_sustantivos_limpios.txt", "w") # Abrimos el archivo en el que guardaremos los sustantivos limpios; no hace falta que exista previamente
for sustantivo in lista_sustantivos_limpia:
	archivo_sustantivos_limpios.write(sustantivo) # Escribimos cada sustantivo como una línea nueva en el archivo
archivo_sustantivos_limpios.close() # Cerramos el archivo
