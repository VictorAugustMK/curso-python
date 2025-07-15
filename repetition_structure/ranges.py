"""
Ranges

- Precisamos conhecer o loop 'for' para usar os ranges.
- Precisamos conher o range para trabalhar melhor com o loops 'for'.

Ranges são utilizado para sequências numéricas, não de forma aleatória, mas sim de maneira especifica.

Formas gerais:

Forma 1
range(stop_value)
"""

# Example Form 1
for num in range(11):
    print(num)

# Form 2
# range(start_value, stop_value)

# Example Form 2
for num in range(1, 11):
    print(num)

# Form 3
# range(start_value, stop_value, pass)
# NOTE: step specified by the user.

# Example Form 3
for num in range(0, 50, 5):
    print(num)

# Example Form 4
# range(start_value, stop_value, pass)
# NOTE: step specified by the user.

for num in range(10, 0, -1):
    print(num)

