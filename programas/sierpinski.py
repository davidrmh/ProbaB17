import numpy as np
import pylab
import math
from random import randint
from numpy.random import triangular, uniform


def puntoMedio(p1, p2):
    ''' Calcula el punto medio entre dos puntos

    Input:
    p1,p2: Lista [x,y]

    Output:
    Lista [xmedio,ymedio]
    '''
    return [(p1[0] + p2[0])/2, (p1[1] + p2[1])/2]

def creaVertices(numPuntos=3,radio=1):
    '''Obtiene los vertices de un poligono regular

    Input:
    numPuntos: Numero de lados del poligono regular
    radio: Radio del circulo que contiene el poligono

    Output:
    vertices: Lista de listas con los vertices [x,y]
    '''

    angulo=2*math.pi/numPuntos
    vertices=[]
    for i in range(0,numPuntos):
        x=radio*math.sin(i*angulo)
        y=radio*math.cos(i*angulo)
        vertices.append([x,y])
    return vertices


def sierpinski(nsim=1000,numlados=3,radio=1):
    '''Obtiene el poligono de Sierpinski simulando nsim veces
    Input:
    nsim: Numero de simulaciones
    numlados: Numero de lados del poligono

    Output:
    Imagen con el poligono de Sierpinski
    '''

    #Vertices del poligono
    vertices=creaVertices(numlados,radio)

    #Elige un punto dentro del poligono
    #(De esta parte no estoy muy seguro sobre x=uniform)
    #Hace sentido cambiar por x=0.5
    #Por eso grafico el punto interior inicial
    #Por alguna razon funciona con x=uniform!!
    #puntoInterior = [uniform(0,1),triangular(0,.5,1)]
    puntoInterior = [0,0]
    pylab.plot(puntoInterior[0],puntoInterior[1],'m.',markersize=10)

    # Crea la grafica
    for i in range(nsim):

        dado = randint(0,len(vertices)-1)
        puntoInterior = puntoMedio(puntoInterior, vertices[dado])
        pylab.plot(puntoInterior[0],puntoInterior[1],'r.',markersize=3)

    pylab.show()
