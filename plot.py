import os
import matplotlib.pyplot as plt

def le(numero_experimento, nome, total_alocacao, total_cobertura):

    idx = 1
    while True:
        file_path = "experimento "+str(numero_experimento)+"/"+nome+"-"+str(idx)+".txt"
        total_cobertura.append([])
        if not(os.path.exists(file_path)):
            break
        proximo = 0
        cluster = 0
        with open(file_path) as f:
            for x in f:
                if(proximo == 1):
                    total_alocacao.append(int(x))
                    proximo = 0
                elif(proximo == 2):
                    if(len(total_cobertura) <= cluster):
                        total_cobertura.append([])
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
        plt.plot(total_alocacao[i], total_cobertura[i][cluster], marker='o', linestyle='--', color=color[i], label=legenda[i])
    plt.xlabel('Number of RSUs')
    plt.ylabel('Vehicle Coverage')
    plt.title(titulo)
    plt.legend()
    plt.show()

if __name__ == '__main__':

    total_alocacao_baseline = []
    total_cobertura_baseline = []
    total_alocacao_baseline.append([])
    total_cobertura_baseline.append([])
    le(4, "baseline", total_alocacao_baseline[0], total_cobertura_baseline[0])
    total_alocacao_baseline.append([])
    total_cobertura_baseline.append([])
    le(4, "grasp", total_alocacao_baseline[1], total_cobertura_baseline[1])
    legenda = ["Baseline", "Grasp"]
    color = ["r", "black"]
    plot(legenda, color, "Cluster 0", total_alocacao_baseline, total_cobertura_baseline, 0)
    