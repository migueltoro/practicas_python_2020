'''
Created on 3 nov. 2020

@author: migueltoro
'''

from typing import List
import csv

def lineas_de_fichero(file:str,encoding:str='utf-8') -> List[str]:
    with open(file, encoding=encoding) as f:
        lineas_de_fichero =  [linea.rstrip('\n') for linea in f]
        return lineas_de_fichero
    
def lineas_de_csv(file:str, delimiter:str=",")-> List[List[str]]:
    with open(file) as f:
        lector = csv.reader(f, delimiter = delimiter)
        lineas_de_fichero =  [linea for linea in lector]
        return lineas_de_fichero

if __name__ == '__main__':
    pass