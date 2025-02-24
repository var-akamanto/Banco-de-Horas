def CreateDB(dbName):
    import sqlite3 as sql
    import os
    if not os.path.exists(dbName):  
        db = sql.connect(f"{dbName}")
        cursor = db.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS FUNCIONARIOS (
                MATRICULA INTEGER PRIMARY KEY,
                NOME TEXT NOT NULL,
                CARGO TEXT,
                JORNADA INTEGER,
                DATA_ADMISSAO TEXT,
                CONTATO TEXT,
                EMAIL TEXT,
                SITUACAO TEXT,
                OBSERVACOES TEXT
            )
        ''')

        db.commit()
        db.close()

        print("Transaçao realizada.")
    else:
        print(f"Banco de dados {dbName} ja existe.")