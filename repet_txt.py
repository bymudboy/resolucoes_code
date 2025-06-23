# código que solicita uma string e um número inteiro como entrada, depois retorna a string repetida o número de vezes especificado pelo inteiro.

string = input('Digite uma string: ')
numero = int(input('Digite um número inteiro: '))

print('String repetida: ' + (string + ' ') * numero)  