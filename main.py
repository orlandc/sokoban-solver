#Integrantes:
#- Juan Gabriel Rodriguez 201710191
#- Orlando Montenegro     201427277
import sys
import os

root = os.path.dirname(os.path.abspath(__file__))

fold_mapa     = root + "/mapa"
fold_tablero  = root + "/tablero"
fold_busqueda = root + "/busqueda"

sys.path.append(fold_mapa)
sys.path.append(fold_tablero)
sys.path.append(fold_busqueda)

from transformar_mapa import Transformar_Mapa           as TMP
from cargar_mapa      import Cargar_Mapa                as CMP
from bfs              import breadth_first_search       as BFS
from dfs              import depth_first_search         as DFS
from ids              import iterative_deepening_search as IDS

def correr_busqueda(tipo_busqueda=0):
    tablero = CMP(get_mapa_caracteres())
    
    if tipo_busqueda == 1:
        resultados, tablero = BFS(tablero)
    elif tipo_busqueda == 2:
        resultados, tablero = DFS(tablero)
    elif tipo_busqueda == 3:
        resultados, tablero = IDS(tablero)
    elif tipo_busqueda == 0:
        print("No se envio el parametro tipo de busqueda")
        exit()
    else:
        print("No se envio un tipo de busqueda correcto")
        exit()
    
    return resultados, tablero

def get_mapa_caracteres():
    path = 'mapa/map.txt'
    with open(path, 'r') as f:
        mapa_caracteres = f.read()
    return mapa_caracteres

if __name__ == '__main__':
    arguments = len(sys.argv) - 1
    if arguments > 0:
        parametro = sys.argv[1]
    else:
        parametro = 0
    
    TMP()
    resultados, tablero = correr_busqueda(int(parametro))
    print(tablero.movimientos)
    #print(tablero)
