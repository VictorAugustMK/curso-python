"""
1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando os números maiores que 0.
"""

# Activite 1 make my me
print("# Activite 1")

count: int = 0
indice: int = 1

while count < 5:
    if indice % 3 == 0:
        print(indice)
        count = count + 1
    indice = indice + 1