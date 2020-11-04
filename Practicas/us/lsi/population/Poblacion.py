'''
Created on 3 nov. 2020

@author: migueltoro
'''

from dataclasses import dataclass
from typing import TypeVar,List
from us.lsi.population.DatoPoblacion import Dato
from us.lsi.tools.Files import lineas_de_csv
from us.lsi.tools.Iterables import str_iterable
from us.lsi.tools.Draw import draw_multiline, draw_barchart

Poblacion = TypeVar('Poblacion')

@dataclass(frozen=True)
class Poblacion:
    datos:List[Dato]
    
    @staticmethod
    def lee_de_fichero(file:str) -> Poblacion:
        lineas = lineas_de_csv(file)
        return Poblacion([Dato.parse(linea) for linea in lineas])
    
    def __str__(self) -> str:
        return str_iterable(self.datos[50:70],sep='\n',prefix='',suffix='')
    
    @property
    def paises(self) ->List[str]:
        s = {d.nombre_pais for d in self.datos}
        return sorted(s)
    
    def datos_de_pais(self,pais:str) ->List[Dato]:
        return [d for d in self.datos if d.nombre_pais == pais] 
    
    def datos_de_paises_en_anyo(self,paises:List[str],anyo:int) ->List[Dato]:
        return [d for d in self.datos if d.nombre_pais in paises and d.anyo == anyo]
    
    def muestra_evolucion_poblacion_de_pais(self, pais:str) -> None:
        datos = sorted(self.datos_de_pais(pais), key=lambda x:x.anyo)
        puntos = [(d.anyo,d.num_habitantes) for d in datos]
        draw_multiline(puntos)
        
    def muestra_comparativa_paises_anyo(self,anyo:int, paises:List[str])->None:
        datos = self.datos_de_paises_en_anyo(paises,anyo)       
        draw_barchart([d.nombre_pais for d in datos],[d.num_habitantes for d in datos],'Poblacion','Poblacion de los paises en el anyo {}'.format(anyo))
    
if __name__ == '__main__':
    p = Poblacion.lee_de_fichero('../../../data/population.csv')
#    print(p)
    print(p.paises)
#    print(str_iterable(p.datos_de_pais('Uzbekistan'),sep='\n',prefix='',suffix=''))
#    print(str_iterable(p.datos_de_paises_en_anyo(['Tajikistan','Uzbekistan'],1970),sep='\n',prefix='',suffix=''))
#    p.muestra_evolucion_poblacion_de_pais('Uzbekistan')
    p.muestra_comparativa_paises_anyo(1970,['Afghanistan', 'Albania', 'Algeria', 'Angola']);