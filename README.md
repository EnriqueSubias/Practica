# Practica

################################################################
##                  Pseudocódigo ITERATIVO                    ##
################################################################

________________________________________________________________

                   Costes Teóricos Iterativo
________________________________________________________________


Para calcular el menor coste del aqueducto, teniendo en cuenta 2 casos:
 - Todos los puntos tienen pilares.
 - Sólo los puntos de los extremos tienen pilares.

Primero, tras obtener los primeros parámetros y las posiciones x e y de los puntos,
comprobamos que los puntos de los pilares de cada arco estén por debajo del centro del semcírculo que forma el arco (que tiene un coste O(n)),
si no interfieren, entonces procedemos a calcular el coste, se puede hacer los sumatorios por separado, pero para optimizar,
podemos usar un mismo bucle de coste O(n) para calcular 3 cosas:
    -  Comprobación de puntos válidos por debajo de los arcos
    -  Sumatorio de alturas de columnas
    -  Sumatorio de distancias al cuadrado de puntes

Ahora, tenemos que comprobar que todos los puntos del terreno no interfieran con el arco.
Los puntos que estén por debajo del centro del arco, está claro que no interfieren, pero los puntos que hay por encima ya no es tan sencillo.
Para ésto, hemos pensado hacerlo mediante trigonometría, siguiendo la teoria de que
El ángulo que forma un triángulo inscrito en una circunferencia,
con dos vértices alineados con el diámetro, con el tercer vértice en cualquier parte de la circunferencia,
éste formará un ángulo rectángulo con los otros vértices, visto de otra manera,
cualquier triángulo rectángulo inscrito en una circunferencia tendrá un lado que pasará por el centro de la circunferencia.
Ya que como hay que calcular el angulo de cada punto del terreno, el coste será de O(n).

Por lo que el coste total sería de O(n) + O(n) = O(n)
Coste Teórico Iterativo: O(n)

________________________________________________________________

          Pseudocódigo y Costes Prácticos Iterativo
________________________________________________________________


input:
    linea ← string
    n_points ← numPuntos
    h_max ← Altura
    alpha ← alpha
    beta ← beta
    pos_x ←
    pos_y ←
output:
    positive integrer / string

## Para múltiples arcos ##

    for i ← lenght(n_points)                                    coste O(n)
        if i < n_points -1
            radio ← pos_x[ i + 1 ] - pos_x[ i ]
            center ← h_max - radio
            if center < pos_y[ i ] OR center < pos_y[ i + 1 ]                   # Comprobación de que los puntos esten por debajo de los arcos
                return "Impossible"
            distancia ← pos_x[ i + 1] - pos_x[ i ]                              # Cálculo de costes de distancias
            distancia ← distancia^2
        columnas ← columnas + (h_max - pos_y[ i ] )                             # Cálculo de costes de alturas
    result ← (beta * distancia) + (alhpa * columnas)                            # Cálculo de los costes totales
    return result

## Para un solo arco ##

    for i ← lenght(n_points - 1)                                coste O(n)
        if center < pos_y[ i ]                                                  # Si los puntos del terreno están por encima del centro del arco
            angulo ← función calculate_angle()                  coste O(1)      # Tenemos que calcular el angulo que hacen para saber si se solapan
            if angulo < 90
                return "Impossible"                                             # El terreno interfiere con el aqueducto

    columans ← h_max - pos_y [ 0 ]                                              # Cálculo de costes de alturas
    columnas ← columnas + h_max - pos_y [ n_points - 1 ]
    distancia ← distancia + (( pos_x [ n_points - 1 ] - pos_x [ 0 ] ) ^ 2 )     # Cálculo de costes de distancias
    result ← ( columnas * alpha ) + ( distancia * beta )                        # Cálculo de los costes totales
    return result

Coste total sería de O(n) + (O(n) * O(1)) = O(n)
Coste Práctico Iterativo: O(n)


################################################################
##                  Pseudocódigo RECURSIVO                    ##
################################################################

________________________________________________________________

                   Costes Teóricos Recursivo
________________________________________________________________


Para calcular el menor coste del aq‰ueducto, teniendo en cuenta 2 casos:
 - Todos los puntos tienen pilares.
 - Sólo los puntos de los extremos tienen pilares.

Primero, tras obtener los primeros parámetros y las posiciones x e y de los puntos, comprobamos, de la misma manera que en el iterativo,
que los puntos de los pilares de cada arco estén por debajo del centro del semcírculo que forma el arco (que tiene un coste O(n)),
si no interfieren, entonces procedemos a calcular el coste usando una llamada recursiva de coste O(n).

Posteriormente, comprobamos que 

Por lo que el coste total sería de O(n) + O(n) = O(n)
Coste Teórico Recursivo: O(n)

________________________________________________________________

          Pseudocódigo y Costes Prácticos Recursivo
________________________________________________________________


input:
    linea ← string
    n_points ← numPuntos
    h_max ← Altura
    alpha ← alpha
    beta ← beta
    pos_x ← array_X
    pos_y ← array_Y
output:
    positive integrer / string

## Para múltiples arcos ##

if doesnt_overlap_multiple(pos_x [poss_arr], pos_y[poss_arr]    coste O(1)      # Comprobación de que los puntos esten por debajo de los arcos
    if poss_arr < len( pos_x ) - 1
        columnas ← (h_max - pos_y[ poss_arr ])                                  # Cálculo de costes de alturas
        total ← alpha * columnas
        distancia ← pox_x [ poss_arr - 1] - pox_x[ poss_arr ]                   # Cálculo de costes de distancias
        total ← total + beta * distancia
        total ← total + recursive(poss_arr +1 )                 coste O(n)      # Cálculo de los costes totales con llamada recursiva
    else:
        columnas ← (h_max - pos_y[ len( pos_x ) - 1])           coste O(1)      # Caso simple, coste de la última altura cuanfo ha llegao al final
        result ← alpha * columnas
    return result
return Impossible

## Para un solo arco ##

if doesnt_overlap_one_arch()                                    coste O(n)      # Comprobación de que los puntos esten por debajo del arco
    columnas ← (h_max - pos_y[ 0 ])                                             # Cálculo de costes de alturas
    columnas ← (h_max - pos_y[ n_points - 1])
    columnas ← alpha * columnas

    distancias ← distancias + ((pos_x[n_points - 1] - pos_x[ 0 ]) ^ 2)          # Cálculo de costes de distancias
    distancias ← beta * distancias

    result ← columnas + distancias                                              # Cálculo de costes totales
    return result
return Imposible

Coste total sería de  (O(1) * O(n)) + (O(1) * O(1)) + O(n) = O(n)
Coste Práctico Recursivo: O(n)

________________________________________________________________

for i ← 0 to length n
        x ← X[ i ]                                                          # posX del terreno
        y ← Y[ i ]                                                          # poxY del terreno
        if Y[ i ] > (h - max( X ))                                          # Comprobación de que los puntos esten por debajo de los arcos
            result ← result + h - Y [ i ]                                   # Cálculo de costes de alturas
            if i != 0
                result2 ← result2 +  (( X [ i ] - X [ i - 1 ] ) ** 2 )      # Cálculo de costes de distancias
    result ← ( result * alpha ) + ( result2 * beta )                        # Cálculo de los costes totales
    return result

Función recursiva( , result)
    Si el primer arco es válido
        Calcular coste del primer arco
    Si hay más arcos
        Llamada recursiva
    Acabar y hacer return del result

Funcion recursiva()
    Calcular el coste de la priera altura y de la primera distancia
    Si no estamos al final
        llamada recursiva
    si estamos al final
        sumamos al result el coste de la última altura
        hacemos return result

Funcion recutsiva()
    Si no estamos al final
        Calcular el coste de la priera altura y de la primera distancia
        llamada recursiva
    si estamos al final
        sumamos al result el coste de la última altura
        hacemos return result
