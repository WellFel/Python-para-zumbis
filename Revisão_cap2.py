#Capítulo 2: Mastigando estruturas de controle

print ('Bem Vindo ao meu Mundo')
print('Volte Sempre')

#Em geral não é necessário executar todas as linhas do
#do programa

#Ler dois valores inteiros e mostrar o maior deles

a=int(input('Primeiro valor: '))
b=int(input('Segundo Valor: '))

if a>b:
    print('O primeiro número é maior.')
if a<b:
    print ('O Segundo valor é maior.')


#Importante o uso de dois pontos e identação:

#I love dois pontos !!

#Verificar se um carro é novo ou velho:
#Maior que 3 anos, o carro é velho, caso contrário
    #o carro será velho

idade=int(input('Informe o ano do carro: '))
if idade >= 2016:
    print ('O carro é novo')
else:
    print ('O carro é velho')

#PErguntar a velocidade de um carro , supondo um valor int

km=int(input('Informe a velocidade do veículo: '))
if km<=110:
    print ('Velocidade dentro do permitido.')
else:
    print('Veículo acima da velocidade permitida, multado em R$', (km-110)*5,)

#empresa tchau de telefonia

minutos=int(input('Informe a quantidade de minutos utilizados: '))
if minutos<=200:
    p1=0.20
    print ('O valor da conta é de %.2f' %(minutos*p1))

else:
    
    if 201<minutos<=400:
        p2=0.18
        print ('O valor da conta é de %.2f' %(minutos*p2))
    else:
        p3=0.15
        print ('O valor da conta é de %.2f' %(minutos*p3))

# Repetições
#incrementação, ex:imprimindo de 1 a 3

x=1 # apartir daqui
while x<=3:
    print (x)
    x+=1 #(x=x+1), contador                             

#Imprima um valor de 1 até um número digitado
#pelo usuário

x=1
y=int(input('Digite um valor: '))
while x<=y:
    print (x)
    x+=1

#Imprima os números pares entre 0 e um número fornecido
    #usando if


y=int(input('Informe um número: '))
x=0
while x<=y:
    if x % 2 == 0:
        print(x)
        x=x+1

#utilizando o mesmo sistema acima, mas sem o a cláusula IF

y=int(input('Digite um valor: '))
x=0
while x<=y:
    print(x)
    x=x+2


# Fazer um programa similar ao anterior, porém utilizando
#apenas os números ímpares:

y=int(input('Digite um valor: '))
x=1
while x<=y:
    print (x)
    x=x+2
#idem programa anterior, com dez primeiros multiplo de trê

y=30
x=0
while x<=y:
    print(x)
    x=x+3

# Acumuladores
#no contador, há uma varredura nos elementos definidos
#no acumulador há acumulo entre os elementos atribuídos

#Cálculo da soma de dez números inteiros:

n=1 #Contador
soma=0
while n<=10: #10 é quantidade máxima de números
    x=int(input('Informe um valor: '))
    soma=soma+x #Acumulador
    n=n+1
print ('A soma é %.2f' %soma)

# fazer a média de 10 números inteiros

n=1 #contador
soma=0 #acumulador
while n<=10:
    nota=float(input('Informe uma nota: '))
    soma=soma+nota
    n+=1
print ('A média das notas é: ', (soma/10))

#Calcule o fatorial de dez, baseado no programa anterior
n=1
fat=1
while n<=10:
    fat=fat*n
    n+=1
print ('O fatorial é %d' %fat)



n=1
fat=1
while n<=10:
    fat=fat*n
    n+=1
print ('O fatorial é %d' %fat)

#Calcule o fatorial de um número inteiro qualquer

n=1
fat=1
y=int(input('Digite um valor para achar seu fatorial:'))
while n<=y:
    
    fat=fat*n
    n+=1
print ('O fatorial do valor é', fat)
    
#Interropendo a repetição, no meio dos comando while
soma=0
while True:
    x=int(input('Digite o número (0 sai):'))
    if x==0:
        break
    soma+=1
print(' A soma é: ', soma)





    
        
        





