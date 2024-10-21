


def contar_palabras(fichero,palabra):
    with open(fichero,'r',encoding='utf-8') as f:
        contenido= f.read().lower()
        palabras=contenido.split()
        contar=palabras.count(palabra.lower())
    return contar


print(contar_palabras('lin_quijote.txt', 'quijote'))


def buscar_lineas(fichero,cad):
    cad=cad.lower()
    lineas_encontradas=[]
    
    with open(fichero,'r',encoding='utf-8') as file:
        for linea in file:
            linea_minuscula = linea.lower()
            if cad in linea_minuscula:
                lineas_encontradas.append(linea.strip())
    return lineas_encontradas
print(buscar_lineas('lin_quijote.txt','quijote'))


def palabras_unicas(fichero):
    palabras=set()
    
    with open(fichero,'r',encoding='utf-8') as file:
        for linea in file:
            for palabra in linea.split():
                palabras.add(palabra.lower())
    return list(palabras)

print(palabras_unicas('archivo_palabras.txt'))


import csv
from typing import Optional
def longitud_promedio_lineas(file_path: str,sep: str=',') -> Optional[float] :
    total_longitud = 0
    num_lineas = 0
    
    with open(file_path,'r',encoding='utf-8') as file:
        reader = csv.reader(file,delimiter=sep)
        for linea in reader:
            total_longitud +=len(linea)
            num_lineas +=1
            
    if num_lineas > 0:
        return total_longitud / num_lineas
    else:
        return None
    
    
print(longitud_promedio_lineas('palabras_random.csv',','))
print(longitud_promedio_lineas('vacio.csv', ','))