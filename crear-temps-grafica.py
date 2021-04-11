
import matplotlib.pyplot as plt

def sorting(seq):
    pass

def random_list(length):
    """ Random integer list generator """
    import random
    new_list = list(range(length))
    random.shuffle(new_list)
    return new_list

def calcular_temps():
    import timeit
    temps = []
    for x in range(0, 1000, 20):
        temps.append( (x, timeit.timeit("sorting(random_list("+str(x)+"))", setup="from __main__ import sorting, random_list", number=20)) )
    return temps

def crear_grafica( x_list, y_list ):
    import matplotlib.pyplot as plt
    plt.scatter(x_list, y_list)
    plt.show()

if __name__ == '__main__':
    temps = calcular_temps()
    crear_grafica(*map(list, zip(*temps)))
