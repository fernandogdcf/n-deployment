from pymoo.indicators.hv import HV
import matplotlib.pyplot as plt
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
    S = []
    Q = []
    ref_point = np.array([2500, 80000, 80000, 80000])

    tau = 30
    experimentos = 30

    if(len(sys.argv) == 2):
        tau = int(sys.argv[1])

    if(tau == 60):
        numero_baseline = 17
        numero_experimento = 51
    elif(tau == 120):
        numero_baseline = 18
        numero_experimento = 81
    else:
        numero_baseline = 16
        numero_experimento = 21

    le(numero_baseline, "baseline", B)

    hv = HV(ref_point=ref_point)
    result_baseline = hv.do(np.array(B))

    for i in range(numero_experimento,numero_experimento+experimentos):
        F=[]
        le(i, "solucao", F)
        result = hv.do(np.array(F))
        S.append(result)
        Q.append(result_baseline)

    d=[S, Q]

    fig = plt.figure()
    ax = fig.add_subplot(111)

    bp = ax.boxplot(d, patch_artist = True,
                    notch ='True')

    colors = ['#0000FF', '#00FF00', 
            '#FFFF00']

    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    for whisker in bp['whiskers']:
        whisker.set(color ='#8B008B',
                    linewidth = 1.5,
                    linestyle =":")

    # changing color and linewidth of
    for cap in bp['caps']:
        cap.set(color ='#8B008B',
                linewidth = 2)

    for median in bp['medians']:
        median.set(color ='red',
                linewidth = 3)

    # changing style of fliers
    for flier in bp['fliers']:
        flier.set(marker ='D',
                color ='#e7298a',
                alpha = 0.5)

    ax.set_xticklabels(['NSGA-II', 'Baseline'])
    
    #plt.title("Customized box plot")

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 34}

    plt.rc('font', **font)

    plt.xlabel('Method')
    plt.ylabel('Hypervolume')
    plt.show()