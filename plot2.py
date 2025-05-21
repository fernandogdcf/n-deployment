import os
import matplotlib.pyplot as plt
import sys

def le(numero_experimento, nome, total_alocacao, total_cobertura):

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
                    if(int(x) >= 42 and int(x) <= 2094):
                        total_alocacao.append(int(x))
                    proximo = 0
                elif(proximo == 2):
                    if(len(total_cobertura) <= cluster):
                        total_cobertura.append([])
                    if(len(total_alocacao) > len(total_cobertura[cluster])):
                        total_cobertura[cluster].append(int(x))
                    proximo = 0                
                elif("Total" in x):
                    proximo = 1
                elif("cluster" in x):
                    cluster = int(x.split("cluster")[1].split(":")[0])
                    proximo = 2
                elif("Celulas" in x):
                    break
        idx = idx + 1

def plot(legenda, color, titulo, total_alocacao, total_cobertura, cluster):
    for i in range(len(legenda)):
        sorted_indices = sorted(range(len(total_alocacao[i])), key=lambda j: total_alocacao[i][j]) 
        sorted_cobertura = [total_cobertura[i][cluster][j] for j in sorted_indices]    
        plt.plot(sorted(total_alocacao[i]), sorted_cobertura, marker='o', ms=3, color=color[i], label=legenda[i], linestyle='solid')
    plt.xlabel('Number of RSUs')
    plt.ylabel('Vehicle Coverage')
    plt.title(titulo)
    plt.legend()
    plt.show()

def domina(total_alocacao, total_cobertura, i, j):
    domina = False
    if(total_alocacao[i] > total_alocacao[j]):
        return False
    if(total_alocacao[i] < total_alocacao[j]):
        domina = True
    if(total_cobertura[i] < total_cobertura[j]):
        return False
    elif(total_cobertura[i] > total_cobertura[j]):
        domina = True
    return domina

def limpa(total_alocacao, total_cobertura, cluster):
    lista = []
    for i in range(len(total_alocacao)):
        for j in range(len(total_alocacao)):
            if(domina(total_alocacao, total_cobertura[cluster], i, j)):
                if(not(j in lista)):
                    lista.append(j)
    lista = sorted(lista,reverse=True)
    for k in range(len(lista)):
        j = lista[k]
        del total_alocacao[j]
        for l in range(len(total_cobertura)):
            del total_cobertura[l][j]

if __name__ == '__main__':

    n = len(sys.argv)
    numero_experimento = 21
    cluster = 0
    if(n == 3):
        numero_experimento = int(sys.argv[1])
        cluster = int(sys.argv[2])
    total_alocacao_baseline = []
    total_cobertura_baseline = []
    total_alocacao_baseline.append([])
    total_cobertura_baseline.append([])
    le(numero_experimento, "baseline", total_alocacao_baseline[0], total_cobertura_baseline[0])
    total_alocacao_baseline.append([])
    total_cobertura_baseline.append([])
    le(numero_experimento, "solucao", total_alocacao_baseline[1], total_cobertura_baseline[1])
    limpa(total_alocacao_baseline[1], total_cobertura_baseline[1], cluster)
    legenda = ["Baseline", "NSGA-II"]
    color = ["r", "blue"]
    plot(legenda, color, "", total_alocacao_baseline, total_cobertura_baseline, cluster)
    
