'''
Created on 3 nov. 2020

@author: migueltoro
'''

from dataclasses import dataclass
from typing import TypeVar,List

Dato = TypeVar('Dato')

@dataclass(frozen=True,order=True)
class Dato:
    nombre_pais:str
    cod_pais:str
    anyo:int
    num_habitantes:int
      
    @staticmethod
    def of(nombre_pais, cod_pais, anyo, num_habitantes) -> Dato:
        return Dato(nombre_pais, cod_pais, anyo, num_habitantes)
    
    @staticmethod
    def parse(linea:List[str]) -> Dato:
        return Dato(linea[0], linea[1], int(linea[2]),int(linea[3]))
    
    def __str__(self) -> str:
        return '{0:>30s},{1:>4s},{2:5d},{3:10d}'.format(self.nombre_pais,self.cod_pais,self.anyo,self.num_habitantes)

if __name__ == '__main__':
    d = Dato