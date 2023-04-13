idade = [65,78,34,56,22]
altura = [1.65, 1.56, 1,53, 1.47, 1.70]
alturaVazia = []
idadeVazia = []
print(idade)
print(altura)

for i in range(5):
    idadeVazia.append (idade.pop())
    alturaVazia.append(altura.pop())

    print(idadeVazia)
    print(alturaVazia)

