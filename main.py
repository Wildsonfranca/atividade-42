class Usuario:
    def __init__(self, nome, idade, documento):
        self.nome = nome
        self.idade = idade
        self.documento = documento

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Documento: {self.documento}"

class Veiculo:
    def __init__(self, modelo, placa, ano):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

    def __str__(self):
        return f"Modelo: {self.modelo}, Placa: {self.placa}, Ano: {self.ano}"

class SistemaLocacao:
    def __init__(self):
        self.veiculos = []
        self.cadastrar_veiculos()

    def cadastrar_veiculos(self):
        # Cadastrando 5 veículos
        self.veiculos.append(Veiculo("Fusca", "ABC-1234", 1975))
        self.veiculos.append(Veiculo("Civic", "XYZ-5678", 2020))
        self.veiculos.append(Veiculo("Corolla", "LMN-9101", 2021))
        self.veiculos.append(Veiculo("Forte", "JKL-3456", 2018))
        self.veiculos.append(Veiculo("Sandero", "OPQ-7890", 2019))

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
