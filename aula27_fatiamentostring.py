
"""
Fatiamento de strings
 012345678 #esse numero sao os indices, ou seja, é a contagem das letras
 Olá mundo
-987654321 # para negativo tem que começar do -1
Fatiamento [i:f:p] [::] #pega uma fatia da string, pega o inicio, o fim, etc
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo' 
print(variavel[::-1]) #esse numero vai ser o indice, que seriam a contagem das letras, e o -1 é para inverter a ordem

print(variavel[4:]) # vai pegar a partir do indice 4 até o final

print(variavel[4:8]) # vai pegar a partir do indice 4 até o 8, mas não pega o 8
#se não tiver 02 números, o outro está omitido

