nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

#formatação de strings com f-strings
#fstrings sempre começa com f na frente das aspas, e dentro das chaves você pode colocar qualquer expressão do Python, e ele vai calcular o valor da expressão e colocar dentro da string

#envolver a variável sempre em chaves 

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,' #2f seria a quantidade de casas decimais que você quer que apareça, nesse caso 2 casas decimais
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987