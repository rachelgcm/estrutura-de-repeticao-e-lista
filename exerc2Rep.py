
print("faça seu cadastro:")
usuario=str(input("usuario"))
senha=str(input("senha"))
while usuario==senha:
	print("ERRO: o usuario nao pode ser igual a senha.")
	usuario=str(input("usuariO"))
	senha=str(input("senha"))
else:
	print("cadastrado realizado com sucesso")