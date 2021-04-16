#! /usr/bin/env python

import random
import aqueducte #nombre de tu fichero

def soil_generator(n):
   h = random.randint(150,200)
   alpha = random.randint(1,100)
   beta = random.randint(1,100)

   points_x = sorted(random.sample(range(1,n*10), n))
   print(n, h, alpha, beta)
 
   points = []
   for x in points_x:
      points.append( (x, random.randint(1,100)) )

   return h, alpha, beta, points

def test_aqueducte(n):
    h, alpha, beta, points = soil_generator(n)
    xs, ys = list(zip(*points)) #si a vuestra funcion le pasais como parametros una lista con todas las X y otra lista con todas las Y, haced esto. Si no, ignorad esta linea y en lugar de xs e ys, pasais points.
    aqueducte.pos_x = xs
    aqueducte.pos_y = ys
    aqueducte.alpha = alpha
    aqueducte.beta = beta
    aqueducte.n_points = n #esto lo teneis que hacer si usais variables globales en vuestro programa
    aqueducte.h_max = h
    aqueducte.check_overlap_and_calculate_cost_multiple_arches() #nombre_programa.nombre_funcion, llamais a vuestra funcion que calcula los costes 

def calcular_temps():
    import timeit
    temps = []
    for n in range(1,300,1):
        temps.append( (n, timeit.timeit("test_aqueducte("+str(n)+")",
            setup="from __main__ import test_aqueducte", number=1000)) )
    return temps

import matplotlib.pyplot as plt

def crear_grafica( x_list, y_list ):
    plt.scatter(x_list, y_list)
    plt.show()

if __name__ == '__main__':
    temps = calcular_temps()
    crear_grafica(*map(list, zip(*temps)))
