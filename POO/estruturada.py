nomes = []
notas1 = []
notas2 = [] 

def cadastrar ():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    nomes.append(nome)
    notas1.append(nota1)
    notas2.append(nota2)
    
    print(f"Aluno {nome} cadastrado com sucesso!")
def calcular_media(indice):
    media = (notas1[indice] + notas2[indice]) / 2
    return media   
def situação(indice):
    media = calcular_media(indice)
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado" 
def listar():
    if len(nomes) == 0: #len() retorna o tamanho da lista/ array
        print("Nenhum aluno cadastrado.")
        return    
    print(f"\n{'Nome':<16} {'Nota 1':<7} {'Nota 2':<7} {'Média':<8} {'Situação':<14}")
  
    for i in range(len(nomes)):
        print(f"{nomes[i]:<16}{notas1[i]:<7.2f}{notas2[i]:<7.2f}{calcular_media(i):<8.2f} {situação(i):<14} {calcular_media(i):<8.2f} {situação(i):<14}")

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
