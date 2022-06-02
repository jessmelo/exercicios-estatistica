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

def ex1():
    import numpy as np

    # simulação de sorteios com gerador de distribuição multinomial
    n_simulations = 1000000 # número de simulações
    rng = np.random.default_rng()
    simulation = rng.multinomial(2, [2/7, 1/7, 1/7, 1/7, 1/7, 1/7], size=n_simulations)
    
    # contando o número de vezes que foi sorteado pelo menos um aluno da turma 3 (posição 3 do array)
    sorteados_turma3 = 0
    for i in range(n_simulations):
        if(int(simulation[i][2]) >= 1):
            sorteados_turma3 += 1

    prob = sorteados_turma3 / n_simulations
    print("A probabilidade de um dos alunos sorteados ser da turma 3 é ")
    print(prob)

ex1()