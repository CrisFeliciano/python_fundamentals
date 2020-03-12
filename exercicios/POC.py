volantes = ["volante esportivo", "volante normal"]
motores = ["v8", "1.0", "1.6", "2.0"]
print("Bem vindo ao monte seu carro!")
print("Escolha seu volante: \n \t1- Volante Esportivo\n \t2- Volante Normal\n")
volante = int(input(">>> "))
try:
    if volante == 1:

        volante = volantes[0]
    elif volante == 2:

        volante = volantes[1]
    else:
        raise ValueError("Valor inexistente")
except ValueError as v:
    print(v)
print(f"Volante selecionado: {volante}")
print("Escolha seu motor: \n \t1- V8\n \t2- 1.0\n \t3- 1.6\n \t4- 2.0")
motor = int(input(">>>"))
try:
    if motor == 1:

        motor = motores[0]
    elif motor == 2:

        motor = motores[1]
    elif motor == 3:

        motor = motores[2]
    elif motor == 4:

        motor = motores[3]
    else:
        raise ValueError("Valor Incorreto!")
except ValueError as v:
    print(v)
print(f"Motor selecionado: {motor}")
portas = int(input("Digite a quantidade de portas: "))
try:
    if portas <= 4:
        print(f"Quantidade de portas: {portas}")
    else:
        raise ValueError("Valor incorreto")
except ValueError as v:
    print(v)





class Carro:
    def __init__(self):
        self.rodas = 4
        self.volante = volante
        self.motor = motor
        self.portas = portas

    def informacaoes(self):    
        self.confCarros = {'Configuracao':{'volante': volante, 'motor':motor, 'portas': portas}} 
        print(self.confCarros)
    
    def ligar(self):
        print("Carro ligado")

    def desligar(self):
        print("Carro desligado")

    def acelerar(self):
        print("Acelerando")

    def frear(self):
        print("freando")







Fiat_147 = Carro()

Fiat_147.informacaoes()
Fiat_147.ligar()








