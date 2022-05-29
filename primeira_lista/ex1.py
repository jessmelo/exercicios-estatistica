# Enunciado:
# Uma escola contém estudantes nas séries 1,2,3,4,5,6. As turmas das séries 2,3,4,5,6 contêm
# as mesmas quantidades de estudantes, mas a turma 1 contêm o dobro de estudantes das
# demais. Calcule, via simulação, a seguinte questão: Se dois estudantes forem sorteados
# através de amostragem simples com reposição (ou seja, um estudante pode ser sorteado duas
# vezes), qual a probabilidade de pelo menos um deles ser da série 3? Imprima a probabilidade
# estimada.
# Dica: O sorteio pode ser feito usando-se o gerador da distribuição multinomial, sendo que o
# único cuidado a tomar é que você precisará calcular corretamente as probabilidades de um
# estudante ser sorteado em cada uma das seis séries.

import pandas as pd

def ex1():
    escola = pd.read_csv("primeira_lista\escola.csv", sep=";", index_col=False)

    iterable = 10**6
    sorteado_turma3 = 0
    for i in range(iterable):
        amostra = escola.sample(2, replace=True)
        if(amostra.iat[0,0] == "turma3" or amostra.iat[1,0] == "turma3"):
            sorteado_turma3 += 1

    probabilidade = sorteado_turma3 / 10**6
    print("A probabilidade de um dos sorteados ser da turma 3 (com simulação) é de : ")
    print(probabilidade)

ex1()

def teste_com_pmf():
    from scipy.stats import multinomial
    prob = multinomial.pmf(x=[1,1], n=2, p=[1/7, 6/7])
    print("A probabilidade com distribuição multinomial de apenas um dos sorteados ser da turma 3 é de : ")
    print(prob)
    print("A probabilidade com distribuição multinomial de os dois sorteados ser da turma 3 é de : ")
    prob2 = multinomial.pmf(x=[2,0], n=2, p=[1/7, 6/7])
    print(prob2)
    print("Probabilidade total com distribuição multinomial: ")
    print(prob + prob2)

teste_com_pmf()

def teste_com_gerador():
    import numpy as np
    rng = np.random.default_rng()
    simulation = rng.multinomial(100000, [2/7, 1/7, 1/7, 1/7, 1/7, 1/7], size=2)
    prob = (simulation[0][2] + simulation[1][2]) / 100000
    print(simulation)
    print(prob)

teste_com_gerador()