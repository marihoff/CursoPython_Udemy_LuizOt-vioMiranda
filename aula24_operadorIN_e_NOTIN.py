
# Operadores in e not in (in é entre e not in é não está entre)

# Strings são iteráveis, isso quer dizer que navega item por item, no caso de strings, caractere por caractere. Seria como se fosse indices 
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

nome = 'Otávio'
print(nome[2]) # esse seria o indice para acessar a letra "a" do nome otavio
print(nome[-4]) # com negativo, seria de trás para frente 
print('vio' in nome) #esta verificando se a string "vio" está dentro da string "Otávio"
print('zero' in nome) #esta verificando se a string "zero" está dentro da string "Otávio"
print(10 * '-') # imprime 10 hífens
print('vio' not in nome) #esta verificando se a string "vio" não está dentro da string "Otávio"
print('zero' not in nome) #esta verificando se a string "zero" não está dentro da string "Otávio"

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')