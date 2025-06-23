# código que solicita dois números como entrada e deposi realiza uma operação simples entre eles

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

operacao = input('Digite a operação desejada (+, -, *, /): ')

if operacao == '+': 
    resultado = (num1 + num2)
elif operacao == '-':
    resultado = abs(num1 - num2)
elif operacao == '*':
    resultado = (num1 * num2)
elif operacao == '/':
    if num2 != 0:
        resultado = (num1 / num2)
    else:
        resultado = 'Erro: Divisão por zero não é permitida.'

print(f'Resultado: {resultado}')

