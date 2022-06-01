from os import system

def rtres ():
	print ("Regra de tres\n\nA está para B\nC está para X\n\n")
	a=float(input("Digite o valor de A: "))
	b=float(input("Digite o valor de B: "))
	c=float(input("Digite o valor de C: "))
	x = (b*c)/a
	print("{} está para {}\n{} está para {}".format(a,b,c,x))

def rtresi ():
	print ("Regra de tres inversamente proporcional\n\nA está para B\nC está para X\n\n")
	a=float(input("Digite o valor de A: "))
	b=float(input("Digite o valor de B: "))
	c=float(input("Digite o valor de C: "))
	x= (a*b)/c

def Bahskara ():
	print ("Calculadora de Bahskara\n")
	a = int(input("Digite o valor de a: "))
	b = int(input("Digite o valor de b: "))
	c = int(input("Digite o valor de c: "))
	delta = (b**2) - 4*a*c
	xp =  (-b + delta**(1/2))/2*a
	xn =  (-b - delta**(1/2))/2*a
	print ("Delta = {}\nX = {}\nX' = {}".format(delta,xp,xn))


def lucro():
	valor = float(input('digite o valor inicial: '))
	taxa = float(input('digite a taxa: '))
	periodo = int(input('digite o periodo: '))
	taxaP = (taxa/100)+1
	for i in range(0, periodo, 1):
		valor = valor * taxaP
	diferenca = valor - vIni
	print('Obteve um ganho de: $', diferenca)
	print('Valor final: ', valor)
	ganhoP = (diferenca*100)/vIni
	print('Obteve lucro de', ganhoP,'%')

while(True):
	print("\n\nCalculadoras\n\n")
	print("Escolha o tipo de calculadora que deseja utilizar:\n  1. Regra de três\n  2. Regra de três inversamente proporcional\n  3. Bahskara\n  4. Lucro\n  qualquer outro numero. Sair")
	ncalc = int(input("Digite o numero da calculadora:	"))
	system('cls')
	if ncalc == 1:
		rtres()
	elif ncalc == 2:
		rtresi()
	elif ncalc == 3:
		Bahskara()
	elif ncalc == 4:
		lucro()
	else:
		exit()
