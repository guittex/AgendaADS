#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opção")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")
	print("3  Buscar usuário pelo nome");

#Funcoes do processo
def adicionar():
	print("Adicionar um registro")
	agenda = open("agendatelefonica.csv",'a')
	nome = str(input("Nome do Contato:"))
	telefone = str(input("Digite o telefone:"))
	print("Contato salvo com nome:",nome," e número",telefone)
	agenda.write(nome)
	agenda.write(",")
	agenda.write(telefone)
	agenda.write(",")
	agenda.write("\n")
	agenda.close()

def listar():
	print("Lista de Contatos")
	agenda = open("agendatelefonica.csv")
	for linha in agenda:
		partes = linha.strip().split(',')
		print("O telefone de %s eh %s " % (partes[0], partes[1]))
	agenda.close()

def busca():
        agenda = open("agendatelefonica.csv")
        contato = str(input("Digite o nome do usuário: \n"));
        for linha in agenda:
                if(linha.startswith(contato)):
                        print("Contato encontrado: ", linha);
        agenda.close();
        

def falha():
	print("Opção Incorreta")
