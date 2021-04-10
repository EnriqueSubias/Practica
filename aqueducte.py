
#! /usr/bin/python

#import matplotlib.pyplot as plt
import numpy as np
import math
import sys

def calculateCostMultipleArches(n, h, alpha, beta, posX, posY):

    #-#print(n, h, alpha, beta)
    #-#print(" Y ",posY)
    #-#print(" X ",posX)
    # Sumatorio de alturas de columnas
    result = 0
    for i in range(0, n):
        result = float(result + (h - int(posY[i])))
        #-#print(h - int(posY[i]))
    result = float(alpha * result)
    #print("result1" ,result)
    # Sumatorio de distancias de puntes
    result2 = 0
    for i in range(0, n - 1):
        dist = int(posX[i + 1]) - int(posX[i])
        result2 = float(result2 + ( dist ** 2 ))
        #-#print(int(posX[i + 1]) - int(posX[i]))
        #-#print(dist ** 2)

    result2 = float(beta * result2)
    #print("result2" ,result2)
    result = float(result + result2)
    #print("ResultFinal" ,result)
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

def doesntOverlapMultipleArches(posX, posY): ## Falta por hacer la comprobacion de que el terreno no se solapa con el aqueducto

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
            #-print("Posicion de Y ",int(posY[i]))
            #-print(" Centro ",centerY)
            terrainPoint[0] = int(posX[i])
            terrainPoint[1] = int(posY[i])
            #terrainPoint = [1,9]
            angle = calculateAngle(point1, point2, terrainPoint, max(posX))
            if angle < 90 :
                return False
    return True

def calculateAngle(point1, point2, terrainPoint, distanceHorizontal):
    angle = 0
    
    #point1 = [0,5]
    #point2 = [10,5]
    #terrainPoint = [1,9]

    distance1vector = [0,0]
    distance1vector[0] = float(terrainPoint[0] - point1[0])
    distance1vector[1] = float(terrainPoint[1] - point1[1])
    #-print("Distance1Vector [0]")
    #-print(distance1vector[0])
    #-print("Distance1Vector [1]")
    #-print(distance1vector[1])
    distance2vector = [0,0]
    distance2vector[0] = float(point2[0] - terrainPoint[0])
    distance2vector[1] = float(terrainPoint[1] - point2[1])
    #-print("Distance2Vector [0]")
    #-print(distance2vector[0])
    #-print("Distance2Vector [1]")
    #-print(distance2vector[1])
    #distance1vetor = [1,4]
    distance1 = math.sqrt(distance1vector[0] * distance1vector[0] + distance1vector[1] * distance1vector[1]) 
    distance2 = math.sqrt(distance2vector[0] * distance2vector[0] + distance2vector[1] * distance2vector[1]) 
    #-print(" - Distance1 ")
    #-print(distance1)
    #-print(" - Distance2 ")
    #-print(distance2)
    #-print(" - Distance Horizontal ")
    #-print(distanceHorizontal)
    
    #distance1 = 4
    #distance2 = 6
    #distanceHorizontal = 10

    a = (((distance1 * distance1) + (distance2 * distance2) - (distanceHorizontal * distanceHorizontal)) / ( 2 * distance1 * distance2))
    
    ## arc cos de a
    #-print("Resultadod de a",a)
    #-print("Arcos de A en rediantes ",math.acos(a))
    #-print("****Grados de a**** ",math.degrees(math.acos(a)))
    angle = math.degrees(math.acos(a))
    ## result in radians
    #>>> sin(0)
    #0.0
    #>>> cos(0)
    #1.0
    #>>> math.pi
    #3.141592653589793
    #>>> math.atan(1)
    #0.7853981633974483

    #Valor de la hipotenusa de un triangulo rectangulo dados sus catetos
    #>>> math.hypot(3, 4)
    #5.0

    #print("Angulo")
    #print(angle)
    return angle


def isValid():
    if n < 2 or n > 10000 or h < 1 or h > 100000 or alpha < 1 or alpha > 10000 or beta < 1 or beta > 10000:
        return False
    else:
        return True

def readTerrain(posX, posY):
    for x in f:
        a = x.split(" ")
        posX.append(float(a[0])) # si un punto esta por encima de la altura maxima (if) print impossible
        posY.append(float(a[1]))
    posX.pop(0)
    posY.pop(0)



if __name__ == "__main__":
# Leer arhivo .in
#$./aqueducte <fitxer entrada>
    f = open(sys.argv[1] , "r")
    valores = f.readline().split(" ")

    n = int(valores[0])
    h = int(valores[1])
    alpha = int(valores[2])
    beta = int(valores[3])

    posX = [0] # x primera columna
    posY = [0] # y segunda columna

    if isValid():
        readTerrain(posX, posY)
        if doesntOverlapMultipleArches(posX, posY) or doesntOverlapOneArch(posX, posY): #Calcular el coste solo si es possible
                result = [0,0]
                result[0] = calculateCostMultipleArches(n, h, alpha, beta, posX, posY)
                result[1] = calculateCostOneArch(n, h, alpha, beta, posX, posY)
                result = int(min(result))
                #print("Coste todos los puntos " + (str(result[0])))
                #print("Coste solo un punto " + (str(result[1])))
                print(result[0]))
                print(result[1]))
                ######print(int(min(result)))
                ## Falta crear archivo .ans
                ###return int(min(result))
                ##sys.stdout.write(int(min(result)))

                print(result)
                

        else:
            print("impossible")
    else:
        print("impossible")

    #-print("")
    #-print("")

    f.close

