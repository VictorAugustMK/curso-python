
# Loop for

# Loop -> Estrutura de repetição.
# For -> Uma das estruturas de repetição

#C ou Java

# for(int i = 0; i < limit; i++) {
#     //execução do loop
# }

#Python

# for i in interavel:
#     //execução do loop

# Utilizamos loops para iterar sobre sequências ou sobre valores interáveis

# Exemplos de interáveis:
# - String
#     nanme = "Curso Python"
# - List
#     list = [1, 3, 5, 7, 9]
# - Range
#     num = range(1, 10)

# Exemplos iterando em uma String
for i in name:
    print(i)

# Exemplos iterando em uma Lista
for number in list:
    print(number)

# Exemplos iterando em uma Range
for number in num:
    print(number)

# Exemplos for
name = "Curso Python"
list = [1, 3, 5, 7, 9]
num = range(1, 10) # Transformar em lista

for i, v in enumerate(name):
    print(name[i])

for i, v in enumerate(name):
    print(v)

for _, v in enumerate(name):
    print(v)

qnt = int(input("Quantas vezes esse loop deve rodar? "))

soma = 0

for n in range(1, qnt + 1):
    num = int(input(f"Informe o {n}/{qnt} valor: "))
    soma = soma + num
print(f"A soma é {soma}")

name = "Curso Python"
for i in name:
    print(i, end=" ")
