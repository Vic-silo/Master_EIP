# Simple función para imprimir lista de numeros indicando si es primo o no
def primo(n):
	for i in range(2, n):
		es_primo = True
		for j in range(2, i):
			if(i%j == 0):
				es_primo = False
		if es_primo:
			print(f"{i} SI es primo")
		else:
			print(f"{i} NO es primo")