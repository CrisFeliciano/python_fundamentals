# Exercicio 1 
# Imprimir Times com o valor de suas cores


#Dados a Lista

#times = [["Corinthians" , "Palmeiras" , "Sao Paulo"], ["preto" , "verde" , "vermelho" , "branco"]]

#print ("time:", times [0][0] ,", cores:" , times [1][0] ,"e", times [1][3])
#print ("time:", times [0][1] ,", cores:" , times [1][1] ,"e", times [1][3])
#print ("time:", times [0][2] ,", cores:" , times [1][2] ,"e", times [1][0])




#Exercicio

valor_hora = float(input('Digite o valor da hora: '))
quant_hora_trabalhada = float(input('Digite a quantidade de hora: '))
salario_bruto = (valor_hora*quant_hora_trabalhada)


def descontos(salario_bruto):
    desc_sindicato = (salario_bruto/100)*3
    fgts = (salario_bruto/100)*11
    ir = 0
    if salario_bruto <= 900:
        salario_liquido = salario_bruto - desc_sindicato
        
    elif salario_bruto <= 1500:
        ir = (salario_bruto/100)*5
        salario_liquido = salario_bruto - desc_sindicato - ir
        
    elif salario_bruto <= 2500:
        ir = (salario_bruto/100)*1045
        salario_liquido = salario_bruto - desc_sindicato - ir
        
    else:
        ir = (salario_bruto/100)*20
        salario_liquido = salario_bruto - desc_sindicato - ir
        
    imprime_desconto(salario_bruto, desc_sindicato, ir, fgts, salario_liquido)

def imprime_desconto(salario_bruto, desc_sindicato, ir, fgts, salario_liquido):
    print('''
    Salario Bruto: %.2f
    Desconto Sindicato: %.2f
    Desconto IR: %.2f
    FGTS: %.2f
    
    Salario Liquido: %.2f
    '''%(salario_bruto, desc_sindicato, ir, fgts, salario_liquido))

descontos(salario_bruto)

