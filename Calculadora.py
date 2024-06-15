def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

def main():
    print("Calculadora Simples")
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        choice = input("Digite a escolha (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if choice == '1':
                print(f"Resultado: {num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"Resultado: {num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"Resultado: {num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                if result == "Erro! Divisão por zero.":
                    print(result)
                else:
                    print(f"Resultado: {num1} / {num2} = {result}")
        else:
            print("Escolha inválida. Por favor, tente novamente.")

        next_calculation = input("Deseja fazer outra operação? (s/n): ")
        if next_calculation.lower() != 's':
            break

if __name__ == "__main__":
    main()
