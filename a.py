
import matplotlib.pyplot as plt
import numpy as np
import sys

def openDocument():
    f = open(sys.argv[1], "r")
    return f
    
def readLine(f):    
    coordinates = f.readline().split(" ")
    return coordinates
    
def closeDocument(f):
    f.close


def drawArch(x0, y0, x1, y1, h, axes, plt):
    
    radio = float((x1 - x0) / 2)
    centerX = x0 + radio
    centerY = h - radio
    

    draw_circle1 = plt.Circle((centerX, centerY), radio, fill=False)
    axes.add_artist(draw_circle1)
    pilar = np.random.randn(2, 2)
    pilar[0] = [x1, x1]
    pilar[1] = [y1, h]
    plt.plot(pilar[0], pilar[1], '-g')



def calculateCostMultipleArches(n, h, alpha, beta, posX, posY):

    # Sumatorio de alturas de columnas
    result = 0
    for i in range(0, n):
        result = float(result + (h - int(posY[i])))
        #print("Altura i ")
        #print(i)
        #print("Resultado")
        #print(result)

    result = alpha * result
    #print("Alpha")
    #print(result)
    
    # Sumatorio de distancias de puntes
    result2 = 0
    for i in range(0, n-1):
        result2 = result2 + ( (int(posX[i + 1]) - int(posX[i])) * (int(posX[i + 1]) - int(posX[i])) )
        
    result2 = float(beta * result2)
    result = float(result + result2)
    print(result)

def calculateCostOneArch(n, h, alpha, beta, posX, posY):
    result=0
    result = float(result + (h - int(posY[0])))
    result = float(result + (h - int(posY[n-1])))
    result = alpha * result
    result2=0
    result2 = result2 + ( (int(posX[n-1]) - int(posX[0])) * (int(posX[n-1]) - int(posX[0])) )
    result2 = float(beta * result2)
    result = float(result + result2)
    print(result)


def valid():
    if 1 == 1 :
        return true
    else:
        return false


f = openDocument()
valores = readLine(f)

n = int(valores[0])
h = float(valores[1])
alpha = float(valores[2])
beta = float(valores[3])

print(n)
print(h)
print(alpha)
print(beta)

if n < 2 or n > 10000 or h < 1 or h > 100000 or alpha < 1 or alpha > 10000 or beta < 1 or beta > 10000:
    print("imposible")
else:
    print("ok")


data = np.random.randn(2, n)
posX = [0] # x primera columna
posY = [0] # y segunda columna

for x in f:
    a = x.split(" ")
    print(a)
    posX.append(a[0])
    posY.append(a[1])
    
posX.pop(0)
posY.pop(0)
closeDocument(f)

np.random.seed(19680801)

maxh = np.random.randn(2, 2)

#pilar0 = np.random.randn(2, 2)
#pilar1 = np.random.randn(2, 2)
#pilar2 = np.random.randn(2, 2)
#pilar3 = np.random.randn(2, 2)
#data[0] = (0,0)

maxh[0] = [posX[0], max(posX)]
maxh[1] = [h, h]

#pilar0[0] = [0,00]
#pilar0[1] = [0,60]

#pilar1[0] = [20,20]
#pilar1[1] = [20,60]

#pilar2[0] = [50,50]
#pilar2[1] = [30,60]

#pilar3[0] = [70,70]
#pilar3[1] = [20,60]

#fig, axs = plt.subplots(2, 2, figsize=(10, 10))
#axs[0, 0].hist(data[0])
#axs[1, 0].scatter(data[0], data[1])
#axs[0, 0].plot(data[0], data[1],maxh[0],maxh[1])
#axs[1, 1].hist2d(data[0], data[1])

figure, axes = plt.subplots()
#radio = int(h)/2
#draw_circle1 = plt.Circle( ( int(max(posX))-(int(min(posX))) )/2, h-radio), radio)#, fill=False)

# Numero de arcos posibles, desde 1 hasta n -1
# Numero de posibilidades

#k = 1 # desde 1 hasta n - 1
#for  k in range(1, 4, 1):

# Todos los puntos tienen columnas

for i in range(0, n-1, 1): 
    j= i + 1
    drawArch(float(posX[i]), float(posY[i]), float(posX[j]), float(posY[j]), float(h), axes, plt)


# Solo los extremos tienen columnas

#drawArch(float(posX[0]), float(posY[0]), float(posX[1]), float(posY[1]), float(h), axes, plt)
#drawArch(float(posX[1]), float(posY[1]), float(posX[3]), float(posY[3]), float(h), axes, plt)
#drawArch(float(posX[3]), float(posY[3]), float(posX[4]), float(posY[4]), float(h), axes, plt)

calculateCostOneArch(n, h, alpha, beta, posX, posY)
calculateCostMultipleArches(n, h, alpha, beta, posX, posY)
#main(result)


drawArch(float(posX[0]), float(posY[0]), float(posX[n-1]), float(posY[n-1]), float(h), axes, plt)

    
#for x in range((n-1)/2):
#    drawArch(float(posX[x]), float(posY[x]), float(posX[x+2]), float(posY[x+2]), float(h), axes, plt)

#for i in range(n-1):
#    drawArch(float(posX[i]), float(posY[i]), float(posX[i+1]), float(posY[i+1]), float(h), axes, plt)

#draw_circle1 = plt.Circle(((int(max(posX)) - int(min(posX))) / 2, h-radio), radio, fill=False)

#draw_circle2 = plt.Circle((35, 45), 15,fill=False)
#draw_circle3 = plt.Circle((60, 50), 10,fill=False)
#line1 = plt.axline((0, 0), (1, 1), linewidth=4, color='r')
#axes.set_aspect(1)
#axes.add_artist(draw_circle1)
#axes.add_artist(draw_circle2)
#axes.add_artist(draw_circle3)
#plt.plot(pilar0[0], pilar0[1], '-g')
#plt.plot(pilar1[0], pilar1[1], '-g')
#plt.plot(pilar2[0], pilar2[1], '-g')
#plt.plot(pilar3[0], pilar3[1], '-g')
#plt.scatter(posX[0], max(posX), marker='o',s=100)

fig, axs = plt.plot(posX, posY, maxh[0], maxh[1])

#pilar1[0],pilar1[1],pilar2[0],pilar2[1]

plt.show()