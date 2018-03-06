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
                funcoes.adicionar()
        elif opcao == 2:
                funcoes.listar()
        elif opcao == 3:
                funcoes.busca()
        else:
                funcoes.falha()
        n = str(input("Digite 9 para sair ou qualquer tecla para continuar: "))
