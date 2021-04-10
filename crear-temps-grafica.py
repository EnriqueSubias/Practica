
def multiplicacio(x,y):
   result = 0
   return result

def calcular_temps():
    import timeit
    temps = []
    for x in range(0,200,10):
        temps.append( (x, timeit.timeit("multiplicacio("+str(x)+",100)",
            setup="from __main__ import multiplicacio")) )
    return temps

import matplotlib.pyplot as plt

def crear_grafica( x_list, y_list ):
    plt.scatter(x_list, y_list)
    plt.show()

if __name__ == '__main__':
    temps = calcular_temps()
    crear_grafica(*map(list, zip(*temps)))
