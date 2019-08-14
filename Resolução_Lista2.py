#Lista 2

# 1)

a=int(input('Informe um dos lados do triângulo: '))
b=int(input('Informe um dos lados do triângulo: '))
c=int(input('Informe um dos lados do triângulo: '))

if not (a<b+c) and (b<a+c) and (c<a+b):
    print ('A figura não é um triângulo.')
else:
    if a==b and b==c and c==a:
        t='Equilátero'
    else:
        if (a==b!=c) and (b==c!=a) and (c==a!=b):
            t='Isósceles'
        else:
            t='Escaleno'
    print(t)

#2)

year=int(input('Informe o ano: '))
if (year%4)==0 and (year%100)!= 0:
    print ('O ano é Bissexto')
else:
    print('O ano NÃO É Bissexto')

#3)
kg=float(input('Informe a quantidade pescada (em Kg): '))
if kg<=50:
    print('Pesca dentro do limite estabelecido, NÃO HÁ MULTA')
else:
    print ('Pesca acima do limite estabelecido, multa de %.2f' %((kg-50)*4))
    
#4)
a=int(input('Informe um número inteiro: '))
b=int(input('Informe um número inteiro: '))
c=int(input('Informe um número inteiro: '))
if (a>b) and (a>c):
    t='O maior é o valor a'
else:
    if (b>a) and (b>c):
        t= ' O maior é o valor b'
    else:
        t='O maior é o valor c'
print (t)

#5)
a=int(input('Informe um número inteiro: '))
b=int(input('Informe um número inteiro: '))
c=int(input('Informe um número inteiro: '))
if (a>b) and (a>c):
    t='O maior é o valor a'
else:
    if (b>a) and (b>c):
        t= ' O maior é o valor b'
    else:
        t='O maior é o valor c'
print (t)
#

if (a<b) and (a<c):
    t='O menor é o valor a'
else:
    if (b<a) and (b<c):
        t= ' O menor é o valor b'
    else:
        t='O menor é o valor c'
print (t)

#6
sal=float(input('Informe o salário por hora'))
h=float(input('Informe o número de horas trabalhadas: '))
IR=(11*(sal*h))/100
INSS=(8*(sal*h))/100
Sind=(5*(sal*h))/100
d=IR+INSS+Sind
SL=(sal*h)-d
print('O salário bruto é de %.2f' %(sal*h))
print('Tributos ao IR foi de %.2f' %IR)
print('Tributos ao INSS foi de %.2f' %INSS)
print('Tributos ao Sindicato foi de %.2f' %Sind)
print('O salário líquido é de %.2f' %SL)

#7
m2=int(input('Informe a quantidade de metros quadrado irá ser pintado: '))
if m2%54 !=0: #Considerando que 1 lata de 18L pinta 54 metros quadrado de ambiente
    latas= int(m2/54)+1
else:
    latas= m2/54

valor=latas*80
print('É necessário %d' %latas ' ao custo de R$ %d' %valor)



