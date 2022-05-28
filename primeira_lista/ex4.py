# Exercício 4 (adaptado do exercício 3.8.2 do DeGroot):
# Suponha que uma variável aleatória X possui uma distribuição uniforme discreta sobre os
# valores −3, −2, −1,0,1,2,3. Plote um gráfico de pontos com a função de probabilidade da
# variável aleatória 𝑌 = 𝑋(2 − 𝑋), onde no eixo horizontal será exibido cada valor possível 𝑦
# de 𝑌, e no eixo vertical será exibida a probabilidade Pr (𝑌 = 𝑦), estimada via simulação.

import matplotlib.pyplot as plt
import numpy as np
def ex4():
    x = [-3, -2, -1, 0, 1, 2, 3]
    y = []
    x_axis = []
    y_axis = []
    for i in x:
        y_result = x[i] * (2 - x[i])
        x_axis.append(x[i])
        y_axis.append(y_result)
        print(x[i])
        print(y_result)
    plt.scatter(x_axis, y_axis)
    plt.xticks(x_axis)
    plt.yticks(y_axis)
    plt.xlabel('variável aleatória x')
    plt.ylabel('funcao de probabilidade')
    plt.show()

ex4()