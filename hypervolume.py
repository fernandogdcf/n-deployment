from pymoo.indicators.hv import HV
import numpy as np
import sys
import os

def le(numero_experimento, nome, L):

    idx = 1
    while True:
        file_path = "experimento "+str(numero_experimento)+"/"+nome+"-"+str(idx)+".txt"
        if not(os.path.exists(file_path)):
            break
        proximo = 0
        cluster = 0
        with open(file_path) as f:
            for x in f:
                if(proximo == 1):
                    elemento.append(int(x))
                    proximo = 0
                elif(proximo == 2):
                    elemento.append(80000-int(x))
                    proximo = 0                
                elif("Total" in x):
                    elemento = []
                    proximo = 1
                elif("cluster" in x):
                    proximo = 2
                elif("Celulas" in x):
                    L.append(elemento)
                    break
        idx = idx + 1


if __name__ == '__main__':

    F = []
    B = []
    G = []
    ref_point = np.array([2500, 80000, 80000, 80000])

    numero_experimento = 16
    if(len(sys.argv) == 2):
        numero_experimento = int(sys.argv[1])
    le(numero_experimento, "baseline", B)
    le(numero_experimento, "solucao", F)
    le(numero_experimento, "grasp", G)

    hv = HV(ref_point=ref_point)
    result = hv.do(np.array(F))
    result_baseline = hv.do(np.array(B))
    result_grasp = hv.do(np.array(G))

    print("Hypervolume do nsga2:", result)
    print("Hypervolume do baseline:", result_baseline)
    print("Hypervolume do grasp:", result_grasp)