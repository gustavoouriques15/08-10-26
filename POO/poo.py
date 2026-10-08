class Estudante:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.nota1} e {self.nota2}."
    def media(self):
        return (self.nota1 + self.nota2) / 2
    def situação(self):
        media = self.media()
        if media >= 6:
            return "Aprovado"
        elif media >= 4:
            return "Recuperação"
        else:
            return "Reprovado"
    def descrever(self):
        return f"{self.nome:<16}{self.nota1:<7.2f}{self.nota2:<7.2f}{self.media():<8.2f} {self.situação():<14}"   
    estudantes = [] 
    def cadastrar ():
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))   

        Estudante.append(Estudante(nome, nota1, nota2))
        print(f"Aluno {nome} cadastrado com sucesso!")
    def listar():
        if len(Estudante.estudantes) == 0:
            print("Nenhum aluno cadastrado.")
            return
        print(f"\n{'Nome':<16} {'Nota 1':<7} {'Nota 2':<7} {'Média':<8} {'Situação':<14}")
        for estudante in Estudante.estudantes:
            print(f"\n{'NOME':<16} {'NOTA 1':<7} {'NOTA 2':<7} {'MÉDIA':<8} {'SITUAÇÃO':<14}")
            for estudante in Estudante.estudantes:
                print(estudante.descrever())
    def menu():
        while True:
            print("\nMenu:")
            print("1. Cadastrar aluno")
            print("2. Listar alunos")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                cadastrar()
            elif opcao == "2":
                listar()
            elif opcao == "3":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")


    menu()            
