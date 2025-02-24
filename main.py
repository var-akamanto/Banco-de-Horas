from dbConfig.CreateDataBase import CreateDB 
from dbConfig.functionsDB import InsertDB
import os

dbName = "Banco_de_Horas.db"

if(os.path.exists(dbName)):
     CreateDB(dbName)
