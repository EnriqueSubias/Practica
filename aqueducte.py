#! /usr/bin/python

#import matplotlib.pyplot as plt
import numpy as np
import math
import sys

def calculateCostMultipleArches(n, h, alpha, beta, posX, posY):
    
    # Sumatorio de alturas de columnas
    result = 0
    for i in range(0, n):
        result = float(result + (h - int(posY[i])))
    result = float(alpha * result)
    
    # Sumatorio de distancias al cuadrado de puntes
    result2 = 0
    for i in range(0, n - 1):
        dist = int(posX[i + 1]) - int(posX[i])
        result2 = float(result2 + ( dist ** 2 ))

    result2 = float(beta * result2)
    result = float(result + result2)
    return result

def calculateCostOneArch(n, h, alpha, beta, posX, posY):
    result = 0
    result = float(result + (h - int(posY[0])))
    result = float(result + (h - int(posY[n-1])))
    result = alpha * result
    result2 = 0
    result2 = result2 + ( (int(posX[n - 1]) - int(posX[0])) * (int(posX[n - 1]) - int(posX[0])) )
    result2 = float(beta * result2)
    result = float(result + result2)
    return result

def doesntOverlapMultipleArches(posX, posY):

    for i in range(0, n - 1, n):
        radio = (float(posX[i + 1]) - float(posX[i])) / 2
        centerY = h - radio

        if centerY < int(posY[i]) or centerY < int(posY[i + 1]):
            return False
    return True

def doesntOverlapOneArch(posX, posY):

    terrainPoint = [0,0]
    centerY = h - float(max(posX)) / 2

    point1 = [0,0]
    point1[0] = float(posX[0])
    point1[1] = centerY

    point2 = [0,0]
    point2[0] = float(posX[n - 1])
    point2[1] = centerY

    for i in range(0, n - 1):
        if centerY < int(posY[i]):# or centerY < int(posY[i + 1]):
            terrainPoint[0] = int(posX[i])
            terrainPoint[1] = int(posY[i])
            angle = calculateAngle(point1, point2, terrainPoint, max(posX))
            if angle < 90 :
                return False
    return True

def calculateAngle(point1, point2, terrainPoint, distanceHorizontal):
    angle = 0

    distance1vector = [0,0]
    distance1vector[0] = float(terrainPoint[0] - point1[0])
    distance1vector[1] = float(terrainPoint[1] - point1[1])

    distance2vector = [0,0]
    distance2vector[0] = float(point2[0] - terrainPoint[0])
    distance2vector[1] = float(terrainPoint[1] - point2[1])

    distance1 = math.sqrt(distance1vector[0] * distance1vector[0] + distance1vector[1] * distance1vector[1])
    distance2 = math.sqrt(distance2vector[0] * distance2vector[0] + distance2vector[1] * distance2vector[1])

    a = (((distance1 * distance1) + (distance2 * distance2) - (distanceHorizontal * distanceHorizontal)) / ( 2 * distance1 * distance2))
    angle = math.degrees(math.acos(a))

    return angle


def isValid(): # Comprobamos que los parametros de la primera linea son correctos segun el enunciado
    if n < 2 or n > 10000 or h < 1 or h > 100000 or alpha < 1 or alpha > 10000 or beta < 1 or beta > 10000:
        return False
    else:
        return True

def readTerrain(posX, posY):
    for i in f:
        a = i.split(" ")
        if float(a[1]) > h:    # Comprobamos que los puntos esten por debajo de la altura maxima
            return False
        posX.append(float(a[0]))
        posY.append(float(a[1]))
    posX.pop(0)
    posY.pop(0)
    return True

if __name__ == "__main__":
    
    f = open(sys.argv[1], "r")
    valores = f.readline().split(" ")
    
    n = int(valores[0])
    h = int(valores[1])
    alpha = int(valores[2])
    beta = int(valores[3])
    
    if isValid():
        posX = [0]            # X primera columna
        posY = [0]              # Y segunda columna
        if readTerrain(posX, posY):
            result = [0,0]
            if doesntOverlapMultipleArches(posX, posY):
                result[0] = calculateCostMultipleArches(n, h, alpha, beta, posX, posY)
            else:
                result[0]="impossible"

            if doesntOverlapOneArch(posX, posY):
                result[1] = calculateCostOneArch(n, h, alpha, beta, posX, posY)
            else:
                result[1]="impossible"
            
            result = int(min(result))
        else:
           result = "impossible"       
    else:
        result = "impossible"
    
    f.close
    
    print(result)
    #return result
