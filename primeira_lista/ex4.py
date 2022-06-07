# Exercício 4 (adaptado do exercício 3.8.2 do DeGroot):
# Suponha que uma variável aleatória X possui uma distribuição uniforme discreta sobre os
# valores −3, −2, −1,0,1,2,3. Plote um gráfico de pontos com a função de probabilidade da
# variável aleatória 𝑌 = 𝑋(2 − 𝑋), onde no eixo horizontal será exibido cada valor possível 𝑦
# de 𝑌, e no eixo vertical será exibida a probabilidade Pr (𝑌 = 𝑦), estimada via simulação.

def ex4():
    import matplotlib.pyplot as plt
    import random
    n_simulations = 1000000 # número de simulações
    x = [-3, -2, -1, 0, 1, 2, 3] # valores de x
    y = [-15, -8, -3, 0, 1] # valores de y
    pr_y = [0, 0, 0, 0, 0] # probabilidades de y

    for i in range(n_simulations):
        random_x = random.choice(x)
        random_y = random_x * (2 - random_x)
        for i in range(5):
            if(y[i-1] == random_y):
                pr_y[i-1]+=1
            
    for i in range(5):
        pr_y[i-1] = pr_y[i-1] / n_simulations

    plt.scatter(pr_y, y)
    plt.xticks(pr_y)
    plt.yticks(y)
    plt.xlabel('Pr (Y = y)')
    plt.ylabel('y')
    plt.show()

ex4()