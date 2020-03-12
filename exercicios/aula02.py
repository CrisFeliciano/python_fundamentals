


#Dado o dicionário

#produtos = dict(produtos=dict(p1=dict(nome="Camiseta Star Wars", preco=99.90), p2=dict(nome='Caneca Ricky&Morty', preco=49.90), p3=dict(nome='Camiseta SpiderMan', preco=69.90)))

#print(produtos)

#A partir do id do produto mostraremos o nome e o preço
#Caso o produto não exista mostraremos a seguinte mensagem;
#Produto Inexistente



#produtos = dict(produtos=dict(p1=dict(nome="Camiseta Star Wars", preco=99.90), p2=dict(nome='Caneca Ricky&Morty', preco=49.90), p3=dict(nome='Camiseta SpiderMan', preco=69.90)))
    # 
# try:  
    # 
    # id_produtos = input('Digite o nome do produto: ')
    # if id_produtos not in produtos['produtos']:
        # raise ValueError ('Produto não existe ')
# 
    # else:
        # print(f'produto'[produtos['produtos'],[id_produto]['nome']])
# 
        # print ('preco:' .format())
# 
# except ValueError as v:
        # print(f'Erro: {v}')
# 


########################################


#with open('novo arquivo', 'w') as f:
#    f.write('meu primeiro arquivo')


#def dobra(valor):
#    return valor * 2

#    print(dobra(122))
# 
#produtos = []
# 
# 
# def cadastraProduto (produto):
    # return produtos.append(produto)
# 
# def ListaProdutos():
        # if produto in produtos:
        # produto.remove(produtos)
# 
    # else:
        # print('produto não existe')
# 
    # print(produtos)
# 
# cadastraProduto('tenis')
# cadastraProduto('sapato')
# cadastraProduto('bolsa')
# 
# 
# ListaProdutos()

######################################
# def teste(var: int) -> float:
    # print (var)
# 
# teste('casa')
# print
######################################

#usuarios = []
# def cadastra_Pessoa (add=None):
    #pessoa = dict(nome='renato' , sobrenome = 'barbosa')
    # if add is None:
            # pass
    # else:
            # usuarios.append(add)
# 
# cadastra_Pessoa('renato')
# print(usuarios)

####################################


# frutas = []
# 
# def inserFrutas(*args):
    # for f in args:
        # frutas.append(f)
# 
#  inserFrutas('abacaxi', 'uva', 'pera')
# 
#  print(frutas)



##################################

# camisetas = []
# 
# def insereCamiseta(**kwargs):
    # global camisetas
    # camisetas = kwargs
    # return camisetas
# 
# insereCamiseta(camiseta1='Star',  camiseta2='Roxo')
# 
# print(camisetas)



##################################

#dobro =  lambda x: x * 2

#print(dobro(10))


#Faça uma função Lambda que receba 3 valores e retorne uma soma

#soma = lambda x , y , z: x + y + z 
#print(soma(10, 15, 10))


#################################

#Map

# #numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# dobro =  list(map(lambda x: x * 2, numeros))

# print(dobro)



# ################################
# AULA FIBONACCI


n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1


if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)