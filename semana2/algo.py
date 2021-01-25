from Lectura import lee_archivo
import os

def main():
    folder = lee_directorio(".")
    print(folder)
    textos = []
    for f in folder:
        t = lee_archivo(f)
        textos.append(t)
    #Limpiamos los textos y obtenemos una lista de palabras por cada texto
    lista_textos = []
    for t in textos:
        texto_limpio = limpia_textos(t)
        lista_textos.append(texto_limpio)
    #Obtenemos una lista unica de palabras
    lista_palabras_completa = []
    for lista in lista_textos:
        lista_palabras_completa.extend(lista)
    #Obtener el diccionario de palabras
    diccionario_palabras = crea_diccionario_palabras(lista_palabras_completa)
    despliega_diccionario(diccionario_palabras)

def getkey(x):
    return (x[0],x[1])

def despliega_diccionario(diccionario):
    lista = []
    for key,value in diccionario.items():
        lista.append( (value,key))

    acomodada = sorted(lista,key=getkey)
    for palabra in acomodada[::-1]:
        print(palabra[0], " ", palabra[1])
    
        

def crea_diccionario_palabras(lista):
    diccionario = dict()
    for palabra in lista:
        if (palabra not in diccionario):
            diccionario[palabra] = 1  #iniciamos en 1
        else:
            diccionario[palabra] += 1 #incrementamos en 1
    return diccionario


def limpia_textos(texto_original):
    lista_texto = texto_original.split("\n")
    lista_cadena = []
    for cadena in lista_texto:
        c = cadena.lower()
        c = c.replace(".","")
        c = c.replace("¡","")
        c = c.replace("!","")
        c = c.replace(",","")
        c = c.replace(";","")
        c = c.replace("¿","")
        c = c.replace("?","")
        lista_cadena.append(c)
    lista_palabras = []
    for lista in lista_cadena:
        palabras = lista.split(" ")
        for palabra in palabras:
            lista_palabras.append(palabra)
    return lista_palabras

def lee_directorio(directorio):
    lista_dir = os.listdir(directorio)
    lista = []
    for archivo in lista_dir:
        a = archivo.split(".")
        if(len(a)>1):
            if(a[1] == "txt"):
                lista.append(archivo)
    return lista


if __name__ == "__main__":
    main()