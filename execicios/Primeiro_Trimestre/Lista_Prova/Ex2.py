numero = int(input("Digite um valor menor que 100"))

if numero >=100:
  print("o numero inserido não e menor que 100")
else:
    
  dezena = numero //10 
  unidade = numero % 10
  
  soma_digitos = dezena+unidade
  print(soma_digitos)
  
