from core import user_table, engine

con =  engine.connect()
insert =  user_table.insert()

new = insert.values(idade=25, nome='Caio', senha='cris1621')

con.execute(user_table.insert(),[
    {'nome':'marcio', 'idade':20, 'senha': 'limão'},
    {'nome':'elder', 'idade':18, 'senha': 'limão123'},
    {'nome':'gustavo', 'idade':20, 'senha': 'limãoazedo'}
])

