#Agenda Telefonica
import funcoes
n = str(input("Digite 9 para sair ou qualquer tecla para continuar: "))
while n != '9':
        funcoes.bemvindo()

        # Opcoes do Usuario
        opcao = int(input())
        print("Seleccionaste", opcao)


        # Estrutura de controle
        if opcao == 1:
                print("Adicionar um registro")
                nome=str(input("Nome do Contato: "))
                telefone=str(input("Digite o telefone: "))
                funcoes.adicionar(nome,telefone)
               
                
        elif opcao == 2:
                funcoes.listar()
        elif opcao == 3:
                funcoes.busca()
        elif opcao == 4:
                funcoes.remover()
        else:
                funcoes.falha()
        n = str(input("Digite 9 para sair ou qualquer tecla para continuar: "))
