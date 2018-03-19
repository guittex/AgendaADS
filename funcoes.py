#Mensagem de Bem Vindo e Opcoes ao Usuario
def bemvindo():
	print("Bem Vindo a Agenda")
	print("Selecione uma Opcao")
	print("1  Adicionar um novo contato")
	print("2  Listar os contatos da agenda")
	print("3  Buscar usuario pelo nome")
	print("4  Remover contato")

#Funcoes do processo
def adicionar(nome,telefone):
	verificador=[]
	for i in range (0,len(telefone)):
		verificador.append(telefone[i])
	digitos=len(verificador)
	if (digitos >= 8):
		print("Contato salvo com nome: ",nome," e numero ",telefone)	
		agenda = open("agendatelefonica.csv",'a')
		agenda.write(nome)
		agenda.write(",")
		agenda.write(telefone)
		agenda.write(",")
		agenda.write("\n")
		agenda.close()
		return(True)
	else: 
		print ("Digite um telefone com mais de 8 digitos")
		return(False)	
def listar():
	print("Lista de Contatos")
	agenda = open("agendatelefonica.csv")
	for linha in agenda:
		partes = linha.strip().split(',')
		print("O telefone de %s eh %s " % (partes[0], partes[1]))
	agenda.close()

def busca():
        agenda = open("agendatelefonica.csv")
        contato = str(input("Digite o nome do usuario: \n"));
        for linha in agenda:
                if(linha.startswith(contato)):
                        print("Contato encontrado: ", linha);
        agenda.close();

def remover ():
		print("Remover um contato")
		agenda = open("agendatelefonica.csv", "r")
		lines = agenda.readlines()
		agenda.close()
		agenda = open("agendatelefonica.csv", "w")
		remover = input("Digite o nome do usuario para remover: ")
		for line in lines:
				if line[:(len(remover)+1)] != (remover+","):
					agenda.write(line)

		agenda.close()


def falha():
	falha="opcao incorreta"
	print(falha)
