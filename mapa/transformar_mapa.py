
def Transformar_Mapa():
    f        = open ('mapa/map.txt','r')
    fl       = f.readlines()
    mapa_mod = []
    p        = 0
    for x in fl:
        
        if x.find(',') < 0:
            g = x.replace("\n", "")
            h = g.replace("W", "#")
            i = h.replace("X", ".")
            j = i.replace("0", " ")
            if len(j) > 0:
                mapa_mod.append(list(j))
        else:
            if len(x) == 4 and x.find(',') >= 0:
                vector       = list(x)
                fila         = int(vector[0])
                columna      = int(vector[2])
                get_caracter = mapa_mod[fila][columna]
                if p == 0:
                    if get_caracter == ' ':
                        mapa_mod[fila][columna] = '@'
                    else:
                        mapa_mod[fila][columna] = '+'
                    p = p + 1
                else:
                    if get_caracter == ' ':
                        mapa_mod[fila][columna] = '$'
                    else:
                        mapa_mod[fila][columna] = '*'
    
    f.close()

    with open('mapa/map.txt', 'w') as f2:
        for t, item in enumerate(mapa_mod):
            for item2 in item:
                f2.write("%s" % item2)
            f2.write("\n")