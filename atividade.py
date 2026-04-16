            atividade 1
nome = input("qual seu nome: ")
idade = int(input("Qual sua idade: "))
cidade = input("Qual sua cidade: ")
print(f"Olá,meu nome é {nome}) tenho{idade}anos e moro em {cidade}

                atividade 2
n1 = float(input("digite um numero: "))
n2 = float(input("digite outro: "))

print(float(n1 + n2))
print(float(n1*n2))
print(float(n1/n2))
print(float(n1-n2))

                atividade 3
n1=int(input("digite um numero: "))

for i  in range (n1,n1*10,n1):
    print(i)

                atividade 4
numero = ""


while numero != "23":
    numero=input("digite o numero: ")
print("acerto")

            atividade 5
compras=[]

c1=(input("digite uma compra: "))
c2=(input("digite uma compra: "))
c3=(input("digite uma compra: "))
c4=(input("digite uma compra: "))
c5=(input("digite uma compra: "))

compras=compras(enumerate[c1,c2,c3,c4,c5])
print(compras)

c6=(input("alguma nova compra?:"))

compras.append(["6 " + c6])
print(compras)

        atividade 7


def par_ou_impar():
    n1=int(input("qual seu numero: "))
    n2=int(input("qual seu numero: "))
    n3=int(input("qual seu numero: "))
    if int (n1)%2==0:
        print("par")
    else:
        print("impar")
    if int (n2)%2==0:
        print("par")
    else:
        print("impar")
    if int (n3)%2==0:
        print("par")
    else:
        print("impar")

par_ou_impar()

            atividade 8 
            def calcular_imc(peso,altura):
    peso=int(input("qual seu peso: "))
    altura=float(input("qual sua altura: "))
    imc=peso/(altura**2)
    
calcular_imc()

            atividade 9

def calcular_imc():
    peso=int(input("qual seu peso: "))
    altura=float(input("qual sua altura: "))
    imc=peso/(altura**2)
    print(imc)

calcular_imc()

def
