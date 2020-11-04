'''
Created on 4 nov. 2020

@author: migueltoro
'''

from dataclasses import dataclass
from typing import TypeVar,List

Dato = TypeVar('Dato')

@dataclass(frozen=True,order=True)
class Dato:
    anyo:int
    nombre:str
    frecuencia:int
    genero:str
      
    @staticmethod
    def of(anyo, nombre, frecuencia, genero) -> Dato:
        return Dato(anyo, nombre, frecuencia, genero)
    
    @staticmethod
    def parse(linea:List[str]) -> Dato:
        return Dato(int(linea[0]), linea[1], int(linea[2]),linea[3])
    
    def __str__(self) -> str:
        return '{0:5d},{1:>15s},{2:5d},{3:4s}'.format(self.anyo, self.nombre, self.frecuencia, self.genero)
    
if __name__ == '__main__':
    pass