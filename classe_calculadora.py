class Calculadora:
    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        try:
            resultado = a/ b
            return resultado
        except ZeroDivisionError:
            return "Erro: divisão por zero"
        
calc = Calculadora()

while True:

    print ("\n===CALCULADORA===")
    print ("1 - realizar uma operação matematica")
    print ("0 - Sair do programa")
    opcao = input ("escolha uma opção: ")

    if opcao == "0":
        print("Encerrado o programa.")
        break
    if opcao == "1":
        try:
            #entrada do usuario para calcular
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            #realizando a operação
            if operacao == "+":
                resultado = calc.somar(num1, num2)
            elif operacao == "-":
                resultado = calc.subtrair(num1, num2)
            elif operacao == "*":
                resultado = calc.multiplicar(num1, num2)
            elif operacao == "/":
                resultado = calc.subtrair(num1, num2)
            else:
                resultado = "Operação inválida."

            print (f"Operação '{num1} {operacao} {num2}' é: ", resultado)

        except ValueError:
            print ("Erro: Você deve digitar apenas números válidos.")
            continue
    else:
        print("Opação invalida! tente novamente ou digite (0) para sair")