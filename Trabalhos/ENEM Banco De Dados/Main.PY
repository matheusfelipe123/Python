import sqlite3


  def calcular_media(notas):
    total = sum(notas)
    return total / len(notas)

  
  def calcular_media_enem():
        notas = []
        areas_conhecimento = ["Linguagens", "Humanas", "Natureza", "Matematica", "Redacao"]
        for area in areas_conhecimento:
            nota = float(input(f"Insira a nota de {area}: "))
            if nota < 0 or nota > 1000:
                print(f"Por favor, insira uma nota válida para {area}")
                return
          notas.append(nota)
  
      if notas[4] == 0:
          print("A nota da redação não pode ser zero. O aluno está reprovado.")
          return
  
      media = calcular_media(notas)
      status = "Aprovado" if media >= 450 else "Reprovado"
      mensagem = f"Sua média final no ENEM é: {media:.2f}\nStatus: {status}"
      print(mensagem)
      # Conectar ao banco de dados (se não existir, será criado)
      conn = sqlite3.connect('dados_usuarios.db')
      cursor = conn.cursor()
  
      # Criar uma tabela se não existir
      cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, Linguagens   REAL, Humanas REAL, Natureza REAL, Matematica REAL, Redacao REAL, Media REAL, Status TEXT)''')
  
        # Inserir os dados do usuário no banco de dados
      cursor.execute("INSERT INTO usuarios ( Linguagens , Humanas , Natureza , Matematica , Redacao , Media , Status ) VALUES (?, ?, ?,?,?,?,?)", (notas[0], notas[1], notas[2], notas[3], notas[4], media, status))
  
      conn.commit()
      # Fechar a conexão com o banco de dados
      conn.close()
      
      
  calcular_media_enem()




