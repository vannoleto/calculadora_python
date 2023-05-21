from calculation import Calculation
import math

class Calculator:
    def __init__(self):
        self.history = []
        self.previous_result = 0

    def run(self):
        while True:
            print("\n=== CALCULADORA ===")
            print("1 - SOMA")
            print("2 - SUBTRAÇÃO")
            print("3 - MULTIPLICAÇÃO")
            print("4 - DIVISÃO")
            print("5 - ELEVAR NÚMERO AO QUADRADO")
            print("6 - ELEVAR NÚMERO AO CUBO")
            print("7 - RAIZ QUADRADA")
            print("8 - RAIZ CÚBICA")
            print("9 - VISUALIZAR HISTÓRICO")
            print("0 - SAIR")
            choice = int(input("Escolha a operação: "))

            if choice == 9:  
                self.display_history()
            elif choice == 0: 
                break
            else:
                if choice == 1 and self.previous_result != 0:
                    print("Utilizar resultado anterior.")
                    choice = int(input())

                self.calculate(choice)

    def calculate(self, operation):
        result = 0

        if 1 <= operation <= 4:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operation == 1: 
                result = num1 + num2
            elif operation == 2:
                result = num1 - num2
            elif operation == 3: 
                result = num1 * num2
            elif operation == 4:
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Erro: divisão por zero.")
                    return
        elif 5 <= operation <= 8:
            num = float(input("Digite o número: "))

            if operation == 5:  
                result = num ** 2
            elif operation == 6: 
                result = num ** 3
            elif operation == 7:
                if num >= 0:
                    result = math.sqrt(num)
                else:
                    print("Erro: não é possível calcular a raiz quadrada de um número negativo.")
                    return
            elif operation == 8: 
                result = num ** (1 / 3)

        print("Resultado:", result)
        self.add_to_history(operation, result)
        self.previous_result = result

    def add_to_history(self, operation, result):
        calculation = Calculation(operation, result)
        self.history.insert(0, calculation)

    def display_history(self):
        print("\n=== HISTÓRICO ===")

        if len(self.history) == 0:
            print("Nenhuma operação realizada.")
        else:
            for calculation in self.history:
                print(f"Operação: {calculation.operation}, Resultado: {calculation.result}")
