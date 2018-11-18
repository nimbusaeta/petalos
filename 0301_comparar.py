import re

archivo_imperativos = open("0204_imperativos_limpios.txt","r")
lista_imperativos_limpia = archivo_imperativos.readlines()
archivo_imperativos.close()

archivo_sustantivos = open("0103_sustantivos_limpios.txt","r")
lista_sustantivos_limpia = archivo_sustantivos.readlines()
archivo_sustantivos.close()

archivo_impsus = open("0302_imperativos_sustantivos.txt","w")
for imperativo in lista_imperativos_limpia:
    for sustantivo in lista_sustantivos_limpia:
        if re.match(imperativo, sustantivo):
            archivo_impsus.write(imperativo)
archivo_impsus.close()
