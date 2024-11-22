#calculadora simples

numero1 = 0
numero2 = 0
resultado = 0
operação = ''

while True: # Loop para continuar pedindo entradas
    numero1 = float (input ('digite o numero 1:')) #ler o primeiro numero em Float
    operação = input('digite a operação:')
    numero2 = float (input ('digite o numero 2:'))

    if operação == "+":
       resultado = numero1 + numero2
    elif operação == "-":
         resultado = numero1 - numero2
    elif operação == "/":
         resultado = numero1 / numero2
    elif operação == "*":
         resultado == numero1 * numero2
    else:
         print = ('operação invalida') 
         
    print('{}{}{}={}'.format(numero1, operação, numero2, resultado))

