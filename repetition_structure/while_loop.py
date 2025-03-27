
# Loop While

# Forma geral

# while expressão_booleana:
#     //execução do loop

# O bloco while será repetido enquanto a expressão booleana for verdadeira.

# Expressão booleana é toda expressão onde o reseultado e verdadeiro ou falso.

# Exemplo:

num = 5
num < 5 (False)
num < 10 (True)

# Exemplo 1
num = 1
while num < 10:
    print(num)
    num = num + 1
# OBS: Em um loop while, é importante que cuidamos do critério de parada para não causar loop infinito.

# Exemplo 2
answord = ""
while answord != "yes":
    answord = input(f"It's over?\n")
