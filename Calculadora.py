def add(x, y):
    """Função para adicionar dois números"""
    return x + y

def subtract(x, y):
    """Função para subtrair dois números"""
    return x - y

def multiply(x, y):
    """Função para multiplicar dois números"""
    return x * y

def divide(x, y):
    """Função para dividir dois números"""
    if y == 0:
        return "Erro: Divisão por zero!"
    else:
        return x / y

print("Selecione a operação desejada:")
print("1. Adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

while True:
    # Solicita ao usuário para selecionar uma operação
    escolha = input("Digite sua escolha (1/2/3/4): ")

    # Verifica se a entrada é válida
    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif escolha == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Escolha inválida!")
