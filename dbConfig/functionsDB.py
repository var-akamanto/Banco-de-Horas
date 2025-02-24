import sqlite3
from dbConfig.Entities import Employee 

def InsertDB(Nome_Banco : str, Pessoa : Employee ):
     db = sqlite3.connect(Nome_Banco)
     cursor = db.Cursor()
    
     query = f"""
          INSERT INTO {Nome_Banco} 
          (MATRICULA,NOME,CARGO,JORNADA,CONTATO,EMAIL,SITUACAO,OBSERVACOES)
          VALUES(?,?,?,?,?,?,?,?)
          """
     
     cursor.execute(query,(
          Pessoa.matricula,
          Pessoa.nome,
          Pessoa.cargo,
          Pessoa.jornada,
          Pessoa.contato,
          Pessoa.email,
          Pessoa.situacao,
          str(Pessoa.observacoes)
     ))

     db.commit()
     db.close()

