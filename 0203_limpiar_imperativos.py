import re

archivo_imperativos = open("0202_lista_imperativos.txt","r")
lista_imperativos = archivo_imperativos.readlines()
archivo_imperativos.close()

def filtrar(forma):
    # plurales 1ª persona (cantemos, comamos, arrepintamos)
    if re.search("[ea]mos\n", forma):
        return False
    # plurales 1ª persona con clitico -os (cantémonos, comámonos, arrepintámonos)
    elif re.search("[éá]monos\n", forma):
        return False
    # singulares 2ª persona voseante (cantá, comé, arrepentí)
    elif re.search("[áéí]\n", forma):
        return False
    # singulares 2ª persona con clitico -te (cántate, cómete, arrepiéntete, pero no ate, mete)
    elif re.search(".*[áéíóú].*[aei]te\n", forma):
        return False
    # plurales 2ª persona (cantad, comed, arrepentid, reíd)
    elif re.search("[aeií]d\n", forma):
        return False
    # plurales 2ª persona con clitico -os (cantaos, comeos, arrepentíos)
    elif re.search("[aeí]os\n", forma):
        return False
    # singulares 3ª persona con clitico -se (cántese, cómase, arrepiéntase, pero no case, cese)
    elif re.search(".*[áéíóú].*[ea]se\n", forma):
        return False
    # plurales 3ª persona (canten, coman, arrepientan)
    elif re.search("[ae]n\n", forma):
        return False
    # plurales 3ª persona con clitico -se (cántense, cómanse, arrepiéntanse, pero no amanse)
    elif re.search(".*[áéíóú].*[ea]nse\n", forma):
        return False
    else:
        return True

def desacentuar(forma):
    if re.search('á', forma):
        return forma.replace('á', 'a')
    elif re.search('é', forma):
        return forma.replace('é', 'e')
    elif re.search('í', forma):
        return forma.replace('í', 'i')
    elif re.search('ó', forma):
        return forma.replace('ó', 'o')
    elif re.search('ú', forma):
        return forma.replace('ú', 'u')
    else:
        return forma

def acentuar(letra):
    if letra == 'a':
        return 'á'
    elif letra == 'e':
        return 'é'
    elif letra == 'i':
        return 'í'
    elif letra == 'o':
        return 'ó'
    elif letra == 'u':
        return 'ú'
    else:
        return letra

def arreglar_qu(forma):
    if re.search("qú", forma):
        forma = forma.replace("qú", "qu") # achaqúe -> achaque
        if re.match('[aeiou]', forma[-5]):
            return forma[:-5] + acentuar(forma[-5]) + forma[-4:] # achaque -> acháque
        elif re.match('[aeiou]', forma[-6]):
            return forma[:-6] + acentuar(forma[-6]) + forma[-5:] # refresque -> refrésque
    return forma

def añadir_clitico(forma):
    return forma[:-1] + 'lo\n'
    
def transformar(forma):
    forma = desacentuar(forma)
    if len(forma) > 3 and re.match('[aeiou]', forma[-3]):
        forma = forma[:-3] + acentuar(forma[-3]) + forma[-2:]
    elif len(forma) > 4 and re.match('[aeiou]', forma[-4]):
        forma = forma[:-4] + acentuar(forma[-4]) + forma[-3:]
    elif len(forma) > 5 and re.match('[aeiou]', forma[-5]):
        forma = forma[:-5] + acentuar(forma[-5]) + forma[-4:]
    elif len(forma) > 6 and re.match('[aeiou]', forma[-6]):
        forma = forma[:-6] + acentuar(forma[-6]) + forma[-5:]
    elif len(forma) > 7 and re.match('[aeiou]', forma[-7]):
        forma = forma[:-7] + acentuar(forma[-7]) + forma[-6:]    
    forma = arreglar_qu(forma)
    forma = añadir_clitico(forma)
    return forma

lista_imperativos_limpia = []
for imperativo in lista_imperativos:
    if filtrar(imperativo) == True:
        imperativo = transformar(imperativo)
        lista_imperativos_limpia.append(imperativo)

archivo_imperativos_limpios = open("0204_imperativos_limpios.txt","w")
for imperativo in lista_imperativos_limpia:
    archivo_imperativos_limpios.write(imperativo)
archivo_imperativos_limpios.close()



