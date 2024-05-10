import sqlite3

def calcular_TMB(idade, peso, altura, sexo):
  if sexo == "M":
      TMB = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
  elif sexo == "F":
      TMB = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)
  else:
    raise ValueError("Sexo inválido. Use 'M' para masculino ou 'F' para feminino.")
  return TMB

idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo M para Masculino e F para Feminino: ")

resultado = calcular_TMB(idade, peso, altura, sexo, )
print("O seu TMB é:", resultado)

# Conectar ao banco de dados (se não existir, será criado)
conn = sqlite3.connect('dados_usuarios.db')
cursor = conn.cursor()

# Criar uma tabela se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY, idade REAL, peso REAL, altura REAL, sexo TEXT, TMB REAL)''')

# Inserir os dados do usuário no banco de dados
def salvar_usuario_no_banco(sexo, idade, peso, altura, TMB):
    cursor.execute('''
    INSERT INTO usuarios (idade, peso, altura, sexo, TMB)
    VALUES (?, ?, ?, ?, ?)
    ''', (idade, peso, altura, sexo, TMB))
    conn.commit()

# Chamar a função para salvar os dados do usuário no banco de dados
salvar_usuario_no_banco(sexo, idade, peso, altura, resultado)

# Fechar a conexão com o banco de dados
conn.close()
