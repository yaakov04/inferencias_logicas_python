import random

#Definiendo las las variables de las inferencias
MP = "P -> Q\nP\n______\nQ"
MT = "P -> Q\n-Q\n______\n-P"
SD = "P v Q\n-Q\n______\nP"
SH = "P -> Q\nQ -> R\n______\nP -> R"
CONJ = "P\nQ\n______\nP & Q"
SIMP = "P & Q\n______\nP"
AD = "P \n______\nP v Q"
DC = "(P -> Q) & (R -> S)\nP v R\n_______________\nQ v S"
DD ="(P -> Q) & (R -> S)\n-Q v -S\n_______________\n-P v -R"

#Texto de Bienvenida e instrucciones
print("Bienvenido a:")
print
print("Que inferencia es")
print
print("=============================================")
print("Instrucciones:")
print("Para cada uno de los argumentos escriba el nombre de la regla de inferencia (MP, MT, SD, etc.) que le corresponda.")
print
print("Escribe tus respuestas solo en mayusculas.")
print
print("==============================================")
print("Conectores logicos:")
print("< Negacion(-), Conjuncion(&), Disyuncion(v), Condicional(->) >")
print
print("==============================================")
print("Reglas de inferencia:")
print("< Modus ponens(MP), Modus tolens(MT), Silogismo disyuntivo(SD), Silogismo hipotetico(SH), Conjuncion(CONJ), Simplificacion(SIMP), Adicion(AD), Dilema constructivo(DC), Dilema destructivo(DD) >")

aciertos = 0
desaciertos = 0
continuar = int(input("Entendido? < 1=si, 0=no >"))
while  continuar == 1:
	r_inf = ((MP,"MP"), (MT, "MT"), (SD, "SD"), (SH, "SH"), (CONJ, "CONJ"), (SIMP, "SIMP"), (AD, "AD"), (DC,"DC"), (DD,"DD"))

	inf = random.choice(r_inf)
	print("========================================")
	print
	print(inf[0])
	print("Que inferencia es?")
	print
	ans = str(input("Cual es tu respuesta:"))
	
	opciones = ("MP", "MT", "SD", "SH", "CONJ", "SIMP", "AD", "DC", "DD")
	
	if ans == inf[1]:
		#print("work")
		answer = ans
	else:
		print("Nowoerk")
	answer = ans
	if inf[1] == answer:
		aciertos = aciertos + 1
		print(" :D Correcto!!! :D ")
		print
		print("Parece que lo tienes ;) ")
	else:
		desaciertos = desaciertos + 1
		print(" u.u Incorrecto u.u ")
		print
		print("Vuelvelo a intentar!!")
		intentos = 1
		print
		print(intentos, "intento(s)")
		reintentar = int(input("Reintentar? < 1=si, 0=no >"))
		
		while reintentar == 1:
			print
			print(inf[0])
			print
			answer = input("Cual es tu nueva respuesta:  ")
			#if answer == opciones:
			#	answer = str(answer)
			print
			if inf[1] == answer:
				aciertos = aciertos + 1
				print("Correcto!! :D ")
				print
				print("Eso es!!")
				reintentar = 0
			else:
				desaciertos = desaciertos + 1
				print("Incorrecto u.u ")
				print
				print("Te hace falta repasar mas el Copi")
				intentos = intentos + 1
				print
				print(intentos, "intento(s)")
				reintentar = int(input("Reintentar? < 1=si, 0=no >"))
			
			
		
		
	continuar = int(input("Deseas continuar? < 1=si, 0=no >"))
		
print
print("Su total de aciertos fue:(" ,aciertos, ") :D ")
if desaciertos >= 1:
	print("Su total de desaciertos fue:(", desaciertos, ") u.u ")
print
	
print("Exit")



		
