'''
Created on 4 nov. 2020

@author: migueltoro
'''

from dataclasses import dataclass
from typing import TypeVar,List,Set,Tuple,Dict
from us.lsi.nombres.DatoNombres import Dato
from us.lsi.tools.Files import lineas_de_csv
from us.lsi.tools.Iterables import str_iterable
from us.lsi.tools.Draw import draw_multiline, draw_barchart
from us.lsi.tools.Iterables import counting

Nacidos = TypeVar('Nacidos')

@dataclass(frozen=True)
class Nacidos:
    datos:List[Dato]
    
    @staticmethod
    def lee_de_fichero(file:str) -> Nacidos:
        lineas = lineas_de_csv(file)
        return Nacidos([Dato.parse(linea) for linea in lineas[1:]])
    
    def __str__(self) -> str:
        return str_iterable(self.datos[:10],sep='\n',prefix='',suffix='')
    
    def de_genero(self,genero:str)->List[Dato]:
        return [d for d in self.datos if d.genero == genero]
    
    def nombres(self,genero:str=None)->Set[str]:
        p = lambda _:True
        if genero is not None:
            p = lambda d: d.genero==genero
        return {d.nombre for d in self.datos if p(d)}
    
    def nombres_mas_fecuentes_en_anyo(self, anyo, limite=10, genero=None)->List[Tuple[int,str,int]]:
        p = lambda _:True
        if genero is not None:
            p = lambda d: d.genero==genero
        r = [(anyo,d.nombre, d.frecuencia) for d in self.datos if p(d) and d.anyo == anyo]
        r.sort(key=lambda x:x[2], reverse=True)
        return r[:limite]
    
    def nombre_mas_frecuente_en_anyo(self, anyo, genero=None)->Tuple[int,str,int]:
        p = lambda _:True
        if genero is not None:
            p = lambda d: d.genero==genero
        r = ((anyo,d.nombre, d.frecuencia) for d in self.datos if p(d) and d.anyo == anyo)
        return max(r,key=lambda e:[2])
    
    @property
    def nombres_en_ambos_generos(self)->Set[str]:
        nombres_hombres = self.nombres('Hombre')
        nombres_mujeres = self.nombres('Mujer')
        return nombres_hombres.intersection(nombres_mujeres)
    
    def nombres_compuestos(self, genero=None)->Set[str]:
        p = lambda _:True
        if genero is not None:
            p = lambda d: d.genero==genero
        return {d.nombre for d in self.datos if p(d) and ' ' in d.nombre}
    
    def anyos(self,genero:str=None)->Set[int]:
        p = lambda _:True
        if genero is not None:
            p = lambda d: d.genero==genero
        return {d.anyo for d in self.datos if p(d)}
    
    def nombre_mas_frecuente_por_anyo(self, genero:str=None)->List[Tuple[int,str,int]]:
        return [self.nombre_mas_frecuente_en_anyo(a,genero) for a in self.anyos(genero)]
        
    def frecuencia_por_anyo_de_nombre(self, nombre:str,genero=None)->List[Tuple[int,int]]:
        return [(a,sum(d.frecuencia for d in self.datos if d.anyo==a and d.nombre==nombre)) for a in self.anyos(genero=genero)]
    
    def mostrar_evolucion_por_anyo(self, nombre:str)->None:
        f = self.frecuencia_por_anyo_de_nombre(nombre)
        f.sort(key=lambda d:d[0])
        draw_multiline(f)
    
    def frecuencia_acumulada(self, nombre:str)->int:  
        return sum(d.frecuencia for d in self.datos if d.nombre==nombre) 
    
    @property
    def frecuencias_por_nombre(self)->Dict[str,int]:
        return counting(self.datos,fkey=lambda d:d.nombre,fsum=lambda d:d.frecuencia)
    
    def mostrar_frecuencias_nombres(self, limite:int=10)->None:
        fn = sorted([(n,f) for n,f in self.frecuencias_por_nombre.items()], key=lambda d:d[1], reverse=True)
        fn = fn[:limite]
        draw_barchart([d[0] for d in fn], [d[1] for d in fn],'Frecuencias de nombres', 'Frecuencias')
           
if __name__ == '__main__':
    p = Nacidos.lee_de_fichero('../../../data/frecuencias_nombres.csv')
#    print(p)
#    g = p.de_genero('Mujer')
#   print(str_iterable(g,sep='\n',prefix='',suffix=''))
#    print(str_iterable(p.nombres()))
#    print(str_iterable(p.nombres_top_en_anyo(2007,genero='Mujer')))
#    print(p.nombres_compuestos())
#    print(p.anyos())
#    genero = None
#    print(p.nombre_mas_frecuente_por_anyo(genero=genero))
#    print(sorted(p.frecuencia_por_anyo_de_nombre('LUCAS')))
#    p.mostrar_evolucion_por_anyo('LUCAS')
#    print(p.frecuencias_por_nombre)
    p.mostrar_frecuencias_nombres(limite=5)
    