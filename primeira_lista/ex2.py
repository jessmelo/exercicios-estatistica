# Suponha que 𝑛 cartas são colocadas aleatoriamente em 𝑛 envelopes. Consideremos duas
# probabilidades de interesse:
# a) 𝑝0𝑛: probabilidade de que nenhuma carta seja colocada no envelope correto;
# b) 𝑝10𝑛: probabilidade de que pelo menos ⌊𝑛/10⌋ cartas sejam colocadas nos envelopes
# corretos.
# Calcule, via simulação, o valor de 𝑝0𝑛 e de 𝑝10𝑛, para 𝑛 = 10, 𝑛 = 20, 𝑛 = 50, 𝑛 = 100.
# Em cada caso, apresente um gráfico de linha da probabilidade 𝑝0𝑛 e 𝑝10𝑛 em função dos
# valores de 𝑛 indicados acima. Os gráficos podem ser separados ou em uma única figura,
# como no exemplo abaixo.
# Observações:
# Para o item (a), há uma versão dual discutida na Seção 1.10 do livro do DeGroot, subseção
# “The Matching Problem”. Ali, é demonstrado que a probabilidade de pelo menos uma carta
# ser colocada no envelope correto converge para aproximadamente 0,632, com 𝑛 → ∞. Logo,
# a probabilidade de nenhuma correspondência é aproximadamente 0,368.
# Já o item (b) ilustra uma situação em que o cálculo exato (analítico) da probabilidade se torna
# consideravelmente mais difícil, e a estimação via simulação mostra-se muito mais simples.

def ex2():
    