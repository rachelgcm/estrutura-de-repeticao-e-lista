nome=str(input("adicione um nome maior que 3 caracteres"))
while ( len(nome) <=  3 ):
	nome=str(input("nome invalido. adicione novamente o nome"))
	
idade=int(input("adicione a idade"))
while ( idade > 150 or idade < 0 ):
	idade=int(input("invalido. adicione uma idade entre 150 e < 0"))
	
	
salario=float(input("informe um salário"))
while ( salario < 0 ):
	salario=float(input("invalido. informe um salário > 0 "))
	

sexo=str(input("informe a inicial do seu genero"))
while  sexo !="f" and sexo!="m" :
	sexo=str(input("informe a inicial do seu genero"))
	

estadoCivil=str(input("informe a inicial do seu estado civil"))
while ( estadoCivil != "s" and estadoCivil != "c" and estadoCivil != "v" and estadoCivil != "d" ):
	estadoCivil=str(input("informe a inicial do seu estado civil"))