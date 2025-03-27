def SquareNumberCalculator():
    print("Enter 3 numbers to be summed:")
    a: int = int(input("First number: ")) ** 2
    b: int = int(input("Second number: ")) ** 2
    c: int = int(input("Third number: ")) ** 2

    total_sum = a + b + c
    print(f'The total sum of the squared numbers is "{total_sum}"')

def Calculator():
    print("Enter 3 numbers to be summed:")
    a: int = int(input("First number: "))
    b: int = int(input("Second number: "))
    c: int = int(input("Third number: "))

    total_sum = a + b + c
    print(f'The total sum of the numbers is "{total_sum}"')

def NumericReader():
    a: int = int(input("Enter a number: "))
    print(f'The number entered was "{a}"')

if __name__ == '__main__':

    print("Choose one of the options below:")
    print("[1] - Square Number Calculator")
    print("[2] - Calculator")
    print("[3] - Numeric Reader")

    num = input()

    if num == '1':
        SquareNumberCalculator()
    elif num == '2':
        Calculator()
    elif num == '3':
        NumericReader()
