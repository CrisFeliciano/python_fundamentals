######################### CONECTANDO NO BANCO DE DADOS POSTGRE SUCESSSO ################################


# import psycopg2


# def insert_in_table(nome, conteudo):
#     try:
#      con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")

#      cur = con.cursor()
#      cur.execute("insert into scripts(nome,conteudo) values ('{nome}', 'print{conteudo}')")
#      #cur.execute ("select * from scripts")
#         #print(f"Primeiro registro é {cur.fetchone()}")
#         #print(f"Todos os outros registros: {cur.fetchall()}")
#      con.commit()
    
#      print('registro OK')

#     except Exception as e:
#             print(f'Erro {e}')
#             print('fazendo rollback')

#         #con.rollback

#     finally:
#             print('final de conexão')
#             cur.close()
#             con.close()

# insert_in_table('Cristiano', 'Feliciano')



##########################CONECTANDO NO DB MONGO #######################


from pymongo import MongoClient


client =  MongoClient('localhost')
db = client['dexterops']


def insert_dados():

        db.fila.insert({    
            "_id":10,
            "empresa": "4linux",
            "cursos": [
                {"nome":"InfraAgil",
                "carga horaria":40},
                {"nome": "Continuos monitoring",
                "carga horaria":40}
            ]})

def select_dados():
    for r in db.fila.find():
        print(f"Empresa: {r['empresa']}")
        for c in r['cursos']:
            print('============')
            print(f"Nome: {c['nome']} \nCarga Horaria: \
                {c['carga horaria']}\n")

select_dados()