from main import *
def mostrar_veiculos(self):
        print("Veículos disponíveis:")
        for i, veiculo in enumerate(self.veiculos):
            print(f"{i + 1}: {veiculo}")

def alugar_veiculo(self):
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        documento = input("Digite seu documento: ")

        usuario = Usuario(nome, idade, documento)

        self.mostrar_veiculos()
        escolha = int(input("Escolha o número do veículo que deseja alugar: ")) - 1

if 0 <= escolha < len(self.veiculos):
        veiculo_escolhido = self.veiculos[escolha]
        print("\nDados da locação:")
        print(usuario)
        print(veiculo_escolhido)
else:
   print("Escolha inválida!")

if __name__ == "__main__":
    sistema = SistemaLocacao()
    sistema.alugar_veiculo()
