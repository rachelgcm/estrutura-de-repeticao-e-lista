aluno1 =[4,7,9,10]
aluno2 =[2,2,3,7] 
aluno3 =[6,8,4,9] 
aluno4 =[6,6,3,8] 
aluno5 =[9,4,10,8] 
aluno6 =[6,8,4,9] 
aluno7 =[3,5,7,3] 
aluno8 =[10,10,10,10] 
aluno9 =[9,9,8,9] 
aluno10 =[4,6,9,10] 
alunos = [aluno1,aluno2,aluno3,aluno4,aluno5,aluno6,aluno7,aluno8,aluno9,aluno10] 
contagem = 0
final= ""
media = 0
for i in alunos:
    for nota in alunos[contagem]:
        media = media + nota 
        media = media / len (alunos[contagem])
        if media >=7:
            final = f"{final} aluno {contagem+1} (aprovado) - {media} |"
        contagem +=1
        media = 0
        print("media", final)