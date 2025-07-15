"""
Saindo de loops com break

Funciona da mesma forma que nas linguagens C e Java.

Utilizamos o break para sair de loops de maneira projetada.
"""

# Example 1
for num in range(1, 11):
    if num == 6:
        break
    else:
        print(num)

# Example 2
while True:
    comand = input(f"Type 'exit' to exit: ")
    if comand == 'exit':
        break
