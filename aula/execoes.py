
# 
# while True: #while True serve para o programa rodar sem fim
# 


    # try: #Serve Para exetutar 

        # x = int(input('digite o 1 num : '))

        # y = int(input('digite o 2 num : '))   

        # print ('O valor é:',(x+y))

        # break #Serve para parar 
# 


    # except ValueError: #Caso o programa de cima dê erro ele exibe a msg abaixo
# 


        # print('digite apenas numeros')

        # continue #Serve para continuar o programa sem fim


################################


try

    produto_id = [1111, 1112, 1113, 1114, 1115]
    id_desejado = int(input ('Digite o id do produto'))
        if id_desejado not in   produto_id:
            raise ValueError('Produto não castrado') 
        else:
        print ('produto cadastrado')

    except ValueError as e:

    print(e)     
