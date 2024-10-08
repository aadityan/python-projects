import calculator

def get_input():
    operator = input("Enter operation (+, -, *, /): ")
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    return operator, a, b

def main():
    while True:
        try:
            operator, a, b = get_input()
            result = calculator.calc(operator, a, b)
            print(f'Result: {result}')
        except ValueError as err:
            print(f'Error: {err}')

        retry = input("Do you want to perform another calculator? (y/n): ")
        if retry != 'y':
            break

if __name__ == '__main__':
    main()

