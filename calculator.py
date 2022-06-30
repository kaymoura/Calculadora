print('\n Calculadora')
print('\n Lembre-se no lugar de {,} use {.}')

# Funcao que retorna operacao de soma
def add(k,y): return float(k+y)
# Operacao de subtracao
def sub(k,y): return float(k-y)

print('\n Selecione a operacao desejada:')
print(' 1 - Soma')
print(' 2 - Subtracao')
escolha = int(input('\n Digite sua opcao {1 ou 2}: '))

number1 = float(input('\n Digite o primeiro numero: '))
number2 = float(input(' Digite o segundo numero: '))

if escolha == 1 : print('\n ' + str(number1) + ' + ' +
     str(number2) + ' = ' + str(add(number1,number2)))

if escolha == 2: print('\n ' + str(number1) + ' - ' +
     str(number2) + ' = ' + str(sub(number1,number2)))