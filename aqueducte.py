#! /usr/bin/env python3

"""Programa para calcular el coste de un aqueducto en modo Iterativo."""

import math
import sys

def check_overlap_and_calculate_cost_multiple_arches():
    """Comprueba que todos los arcos posibles no interfieran con el terreno,
    funciona comprobando que los puntos no esten por encima del inicio de los arcos,
    ya que nunca habra puntos sin pilar, es suficiente con esta comprobacion.
    Y si no se solapan los putnos con el aqueducto,
    calcula el coste del aquaducto con todos los arcos posibles"""

    result_columns = 0
    result_distances = 0
    for i in range(0, n_points):
        if i < n_points - 1:
            radio = (float(pos_x[i + 1]) - float(pos_x[i])) / 2
            center_y = h_max - radio
            if center_y < int(pos_y[i]) or center_y < int(pos_y[i + 1]) or center_y < 0:
                return "impossible"
            dist = int(pos_x[i + 1]) - int(pos_x[i])
            result_distances = float(result_distances + (dist ** 2))
        result_columns = float(result_columns + (h_max - int(pos_y[i])))
    result_columns = float(alpha * result_columns)
    result_distances = float(beta * result_distances)
    result_total = float(result_columns + result_distances)
    ## Sumatorio de alturas de columnas
    ## Sumatorio de distancias al cuadrado de puntes
    #result_distances = 0
    #for i in range(0, n_points - 1):
    #    dist = int(pos_x[i + 1]) - int(pos_x[i])
    #    result_distances = float(result_distances + (dist ** 2))
    #result_distances = float(beta * result_distances)
    #result_total = float(result_columns + result_distances)
    return result_total

def calculate_cost_one_arch():
    """Calcularel coste del aqueducto con un solo arco,
       sabiendo si no se solapa el terreno con el aqueducto"""
    if doesnt_overlap_one_arch():
        result_columns = 0
        result_columns = float(result_columns + (h_max - int(pos_y[0])))
        result_columns = float(result_columns + (h_max - int(pos_y[n_points - 1])))
        result_columns = alpha * result_columns

        result_distances = 0
        result_distances = result_distances + \
            ((int(pos_x[n_points-1]) - int(pos_x[0])) * (int(pos_x[n_points-1]) - int(pos_x[0])))
        result_distances = float(beta * result_distances)
        result_total= float(result_columns + result_distances)
        return result_total
    return "impossible"

#def doesnt_overlap_multiple_arches():
    #for i in range(0, n_points - 1):
     #   radio = (float(pos_x[i + 1]) - float(pos_x[i])) / 2
      #  center_y = h_max - radio

       # if center_y < int(pos_y[i]) or center_y < int(pos_y[i + 1]):
        #    return False
    #return True


def doesnt_overlap_one_arch():
    """Comprueba que ningun punto del terreno interfiera con la semicircunferencia de cada arco,
       si el angulo es mayor de 90 grados, el punto del terreno no se solapa con el
       aqueducto, pero si es menor de 90 grados, significa que si que interfiere."""
    terrain_point = [0, 0]
    center_y = h_max - float(max(pos_x)) / 2

    if center_y < 0:
        return False

    d_horizontal = pos_x[n_points - 1] - pos_x[0]  # Fallo 1 #

    point1 = [0, 0]
    point1[0] = float(pos_x[0])
    point1[1] = center_y

    point2 = [0, 0]
    point2[0] = float(pos_x[n_points - 1])
    point2[1] = center_y

    for i in range(0, n_points - 1):
        if center_y < int(pos_y[i]):
            terrain_point[0] = int(pos_x[i])
            terrain_point[1] = int(pos_y[i])
            # Fallo 1 # Estabamos dando por hecho que el primer punto salia de [0,0]
            angle = calculate_angle(point1, point2, terrain_point, d_horizontal) # max(pos_x)
            # Fallo 2 # Hemos cambiado la condicion para que si esta tocando, no sea valido el arco
            if angle <= 90:
                return False
    return True


def calculate_angle(point1, point2, terrain_point, distance_horizontal):
    """Calcula el angulo de incidencia entre un punto del terreno y dos puntos
       en los pilares a la altura del centro de la semicircunferencia"""

    angle = 0

    distance1vector = [0, 0]
    distance1vector[0] = float(terrain_point[0] - point1[0])
    distance1vector[1] = float(terrain_point[1] - point1[1])

    distance2vector = [0, 0]
    distance2vector[0] = float(point2[0] - terrain_point[0])
    distance2vector[1] = float(terrain_point[1] - point2[1])

    distance1 = math.sqrt(
        distance1vector[0] * distance1vector[0] + distance1vector[1] * distance1vector[1])
    distance2 = math.sqrt(
        distance2vector[0] * distance2vector[0] + distance2vector[1] * distance2vector[1])

    cos_result = (((distance1 * distance1) + (distance2 * distance2) -
         (distance_horizontal * distance_horizontal)) / (2 * distance1 * distance2))
    angle = math.degrees(math.acos(cos_result))

    return angle


def is_valid():
    """Comprueba que los parametros de la primera linea son correctos segun el enunciado."""
    if n_points < 2 or n_points > 10000 or h_max < 1 or h_max > 100000:
        return False
    if alpha < 1 or alpha > 10000 or beta < 1 or beta > 10000:
        return False
    return True


def read_terrain():
    """Lee los puntos del terreno y comprueba que esten por debajo de la altura maxima"""
    for i in f:
        string_doc = i.split(" ")
        if float(string_doc[1]) > h_max:
            return False
        pos_x.append(float(string_doc[0]))
        pos_y.append(float(string_doc[1]))
    pos_x.pop(0)
    pos_y.pop(0)
    return True


if __name__ == "__main__":

    f = open(sys.argv[1], "r")
    valores = f.readline().split(" ")

    n_points = int(valores[0])
    h_max = int(valores[1])
    alpha = int(valores[2])
    beta = int(valores[3])

    if is_valid():
        pos_x = [0]              # X primera columna
        pos_y = [0]              # Y segunda columna
        if read_terrain():
            #f.close # pylint dice que es innecesario ponerlo
            result = [0, 0]
            result[0] = check_overlap_and_calculate_cost_multiple_arches()
            result[1] = calculate_cost_one_arch()
            # Fallo 2 # Hemos a??adido este for para hacer el minimo correctamente
            if result[0] == "impossible" and result[1] == "impossible":
                print("impossible")
            elif result[0] == "impossible":
                print(int(result[1]))
            elif result[1] == "impossible":
                print(int(result[0]))
            else:
                print(int(min(result)))
        else:
            print("impossible")
    else:
        print("impossible")
