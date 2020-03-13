from sqlalchemy import delete
from core import user_table, engine

con =  engine.connect()

nome =  input('Digite nome que vai deletar : ')

apaga =  delete(user_table).where(user_table.c.nome == nome)

resultado = con.execute(apaga)
print(resultado.rowcount)