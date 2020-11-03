'''
Created on 3 nov. 2020

@author: migueltoro
'''


from typing import Iterator, TypeVar, Callable

E = TypeVar('E')


def str_iterable(iterable:Iterator[E],sep:str=',',prefix:str='{',suffix:str='}',ts:Callable[[E],str]=str) -> str:
    return '{0}{1}{2}'.format(prefix,sep.join(ts(x) for x in iterable),suffix)

if __name__ == '__main__':
    pass