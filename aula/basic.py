#!/usr/bin/python3
# Isso é comentário

#print ("Esse é um comentário")

#script que peça o nome

#nome = input("Qual seu nome?\n")

#print("Seu nome é:", nome)

###########################
#endereco = "Rua Vergueiro"

#print(endereco.capitalize()) #
#print(endereco.count()) #Conta palavras
#print(endereco.upper()) #Letras maiusculas
#print(endereco.lower()) #Letras minusculas
#print(endereco.split())
###########################

#vdd = True
#fal = False

#print (vdd.numerator)
#print (fal.numerator)
###########################

#n1 = int(input("Digite o primeiro numero: ")) #int é o valor inteiro, para não juntar e sim somar os numeros
#n2 = int(input("Digite o primeiro numero: "))

#print ("O Valor Somado é: ", n1 + n2)

###########################

#lista =  ["A" , "B" , "C" , "TESTE" , "CASA", ["Lista1" , "Lista2"]] #Exibe uma lista

#print(lista)
#print(lista[4]) #Exibe o quinto valor da lista
#print(lista[2])
#print(len(lista))

#lista [0] = "cachorro" # Serve para modificar valor 

#lista.append(145) #Coloca um valor na ultima lista

#print(lista)

###########################

#Tuplas 

#linguagens = ("python" , "java" , "golang")

#linguagens = ("python" , "javascript" , "golang")

#print (linguagens)
#print (linguagens [0])
#print (linguagens [0].upper ())

###########################

#carros = {"modelos" : {"fox" , "Crossfox", "Palio"}, 
#"anos": {2003, 1978, 2002}}

#print(carros["modelo"])
#print(carros["anos"])


#produtos = {'produtos': {'001' : {'nome' : 'camiseta' , 'preco':99,90},
 #   '002 : {'nome' : 'camiseta 1' , 'preco': 10,00}


  #  print(produtos['produtos'] ['002']['preco']
    #print(produtos.get('produtos').get ('002'))

#produtos['produtos']['001']['preco'] = 29,90

#print(produtos.get('produtos').get ["001"])


###########################

dados = {
    'estado' : {
            'sp': {
            'nome': 'São Paulo',
            'municipios': 645,
            'população': 44.404
        
        },
            'rj': {
            'nome': 'Rio de Janeiro',
            'municipios': 450,
            'população': 50.404
        },
            'mg': {
            'nome': 'Minas Gerais',
            'municipios': 31,
            'população': 50.404
    }
}
}
print ("")

print(f"estado: {dados['estado']['sp']['nome']}")
print(f"municipios: {dados['estado']['sp']['municipios']}")
print(f"população: {dados['estado']['sp']['população']}")

print ("")

print(f"estado: {dados['estado']['rj']['nome']}")
print(f"municipios: {dados['estado']['rj']['municipios']}")
print(f"população: {dados['estado']['rj']['população']}")

print ("")

print(f"estado: {dados['estado']['mg']['nome']}")
print(f"municipios: {dados['estado']['mg']['municipios']}")
print(f"população: {dados['estado']['mg']['população']}")




#Estrutura de Condição

idade = int(input ('Digite sua Idade :'))

if idade >= 18:
    print ('voce é maior de idade')

else:
    print ('voce não é maior de idade')


