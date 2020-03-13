from sqlalchemy import select

from core import user_table

#Select

#selecione =  select([user_table])
#print([x for x in selecione.execute()])

#Filro

filtro =  input('digite usuário : ')
selecione_filtro =  select([user_table]).where(user_table.c.nome == filtro)

print([f for f in selecione_filtro.execute()])





