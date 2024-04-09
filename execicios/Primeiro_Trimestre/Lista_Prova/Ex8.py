lado1 = float(input("Insira o comprimento do primeiro lado:"))
lado2 = float(input("Insira o comprimento do segundo lado:"))
lado3 = float(input("Insira o comprimento do terceiro lado:"))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os comprimentos dos lados dados não podem formar um triângulo.")
