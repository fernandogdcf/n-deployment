#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#define N 500 // tamanho da populaçao
#define G 200 // quantidade de geraçoes

std::vector<std::vector<bool>> alocacao(2*N);
std::vector<int> totalAlocacao(2*N);
std::vector<int> totalCobertura(2*N);

void leParametros()
{
}

void inicializa()
{
}

void geraPopulacaoInicial()
{
}

void avalia(int formulacao)
{
}

void cruzamento()
{
}

void mutacao()
{
}

void selecao()
{
}

void imprimeSolucoes(int numeroExperimento)
{
}

int main(int argc, char **argv)
{
    int formulacao = 2;
    int numeroExperimento = 1;
    leParametros();
    inicializa();
    geraPopulacaoInicial();
    avalia(formulacao);
    std::copy(alocacao.begin(), alocacao.begin()+N, alocacao.begin()+N);
    std::copy(totalAlocacao.begin(), totalAlocacao.begin()+N, totalAlocacao.begin()+N);
    std::copy(totalCobertura.begin(), totalCobertura.begin()+N, totalCobertura.begin()+N);
    for(int i=0; i<G; i++)
    {
        cruzamento();
        mutacao();
        avalia(formulacao);
        selecao();
    }
    imprimeSolucoes(numeroExperimento);
    return 0;
}