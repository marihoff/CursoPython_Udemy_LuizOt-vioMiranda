#Precedencia de operadores são a ordem que eles serão executados, ou seja, qual operador será executado primeiro, segundo, terceiro e assim por diante.

# 1. (n + n) #primeiro executa os parenteses, sempre executa os parenteses de dentro para fora, ou seja, primeiro executa os parenteses mais internos e depois os mais externos

# 2. ** #em segundo, executa a exponenciação, ou seja, o operador de potência

# 3. * / // % #depois, executa a multiplicação, divisão, divisão inteira e módulo, nessa ordem, ou seja, primeiro executa a multiplicação, depois a divisão, depois a divisão inteira e por último o módulo

# 4. + - #por último, executa a adição e subtração, nessa ordem, ou seja, primeiro executa a adição e depois a subtração

#executa sempre da esquerda para a direita 

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)