"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco) # a letra s é o string e o f é o float, o .2 é para limitar a quantidade de casas decimais, se faz isso ao em vez de escrever "Luiz o preço é R$1000.95897643" por extenso, e sim escrever "Luiz o preço é R$1000.96"

print(variavel)

