'''
Created on 3 nov. 2020

@author: migueltoro
'''


from typing import Iterator, Iterable, TypeVar, Dict, Callable, List, Set

K = TypeVar('K')
V = TypeVar('V')
E = TypeVar('E')
R = TypeVar('R')


def str_iterable(iterable:Iterator[E],sep:str=',',prefix:str='{',suffix:str='}',ts:Callable[[E],str]=str) -> str:
    return '{0}{1}{2}'.format(prefix,sep.join(ts(x) for x in iterable),suffix)

def grouping(iterable:Iterator[E],fkey:Callable[[E],K],op:Callable[[V],E],a0:E=None) -> Dict[K, V]:
    a = {}
    for e in iterable:
        k = fkey(e)
        if not (a0 is None):
            a[k] = op(a.get(k,a0),e)
        elif k in a:
            a[k] = op(a[k],e)
        else:
            a[k] = e
    return a

identity = lambda x:x

def grouping_list(iterable:Iterator[E],fkey:Callable[[E],K],fvalue:Callable[[E],V]=identity) -> Dict[K,List[V]]:
    return grouping(iterable,fkey,lambda x,y:x+[fvalue(y)],a0=[])

def grouping_set(iterable:Iterator[E],fkey:Callable[[E],K],fvalue:Callable[[E],V]=identity) -> Dict[K,Set[V]]:
    return grouping(iterable,fkey,lambda x,y:x|{fvalue(y)},a0=set()) 

def counting(iterable:Iterator[E],fkey:Callable[[E],K],fsum:Callable[[E],int]=lambda e:1) -> Dict[K,int]:
    return grouping(iterable,fkey,lambda x,y:x+fsum(y),a0=0)     

if __name__ == '__main__':
    pass