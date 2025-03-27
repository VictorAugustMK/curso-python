
# Ranges

# - Precisamos conhecer o loop 'for' para usar os ranges.
# - Precisamos conher o range para trabalhar melhor com o loops 'for'.

# Ranges são utilizado para sequências numéricas, não de forma aleatória, mas sim de maneira especifica.

# Formas gerais:

# Forma 1
# range(stop_value)

# Exemplo Forma 1
for num in range(11):
    print(num)

# Forma 2
# range(start_value, stop_value)

# Exemplo Forma 2
for num in range(1, 11):
    print(num)

# Forma 3
# range(start_value, stop_value, pass)
# OBS: passo específicado pelo usuário.

# Exemplo Forma 3
for num in range(0, 50, 5):
    print(num)

# Exemplo Forma 4
# range(start_value, stop_value, pass)
# OBS: passo específicado pelo usuário.

for num in range(10, 0, -1):
    print(num)

