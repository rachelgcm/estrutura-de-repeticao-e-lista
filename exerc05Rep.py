a = int(input("População A 80000 = "))
taxa_A = float(input("Taxa de crescimento da população A ="))
resultado1 = taxa_A * 1.5

b = int(input("População B 200000 = "))
taxa_B = float(input("Taxa de crescimento da população B ="))
resultado2 = taxa_B * 1.5 
ano = 0

while a <= b:
	a += a * resultado1
	b += b * resultado2
	ano += 1

print ( "A ultrapassa ou iguala a B em %. em anos" )