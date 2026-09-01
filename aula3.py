"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""
print(1234)

# Aspas simples
print('Luiz Otávio')
print(1, 'Luiz "Otávio"') #essa seria a forma mais simples de escrever uma string com aspas duplas dentro dela, sem precisar usar o escape ou o r antes das aspas

# Aspas duplas 
print("Luiz Otávio")
print(2, "Luiz 'Otávio'")

# Escape seria a barra invertida, que serve para escapar caracteres que tem uma função especial no Python
print("Luiz \"Otávio\"")

# r antes das aspas, serve para ignorar os caracteres de escape, ou seja, ele vai imprimir exatamente o que estiver dentro das aspas
print(r"Luiz \"Otávio\"")