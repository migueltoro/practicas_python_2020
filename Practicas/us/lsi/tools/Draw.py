'''
Created on 3 nov. 2020

@author: migueltoro
'''

from typing import List,Tuple,Callable
import matplotlib.pyplot as plt
import numpy as np

def draw_function(function:Callable[[float],float],a:float,b:float,inc:float)->None: 
    plt.axes()
    n = int((b-a)/inc)
    x = [a+i*inc for i in range(0,n)]
    y = [function(v) for v in x]
    plt.plot(x, y)
    plt.show()
    
def draw_piechar(labels:List[str],sizes:List[int]):
    plt.pie(sizes, labels=labels)
    plt.axis('equal')
    plt.show()

def draw_barchart(labels:List[str],sizes:List[int],title:str,y_label:str):
    y_pos = np.arange(len(sizes))
    plt.bar(y_pos,sizes, align='center', alpha=0.5)
    plt.xticks(y_pos,labels)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()
    
def draw_multiline(points:List[Tuple[float,float]],y_label:str='eje y',x_label:str='eje_x',title:str='Grafico'):
    plt.ylabel(y_label)
    plt.xlabel(x_label) 
    plt.title(title) 
    plt.plot([x[0] for x in points], [x[1] for x in points])
    plt.show()
   

if __name__ == '__main__':
    pass