def calculate_bmi(weight, height):
    # Calcula o IMC
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    # Determina a categoria do IMC
    if bmi < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= bmi < 24.9:
        return "Peso normal"
    elif 25 <= bmi < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    print("Calculadora de IMC")
    weight = float(input("Digite seu peso em kg: "))
    height = float(input("Digite sua altura em metros: "))

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print(f"Seu IMC é: {bmi:.2f}")
    print(f"Categoria: {category}")

if __name__ == "__main__":
    main()
