numero1 = int(input('Digite seu primeiro Numero: '))
numero2 = int(input('Digite seu segundo Numero: '))
numero3 = int(input('Digite seu Terceiro Numero: '))

if (numero1 >= numero2) and (numero1 >= numero3):
   maior = numero1
elif (numero2 >= numero1) and (numero2 >= numero3):
    maior = numero2
else:
    maior = numero3

print("O maior numero é:",maior)
