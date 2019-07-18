#Exercício 1
n1=int(input('Digite um número inteiro: '))
n2=int(input('Digite um número inteiro: '))
print('A soma de de n1+n2 é: ' ,n1+n2)

#Exercício 2
m=int(input('Digite um valor em metros '))
mm= m*1000
print('O valor em milímetros é: ', mm)

#Exercício 3
d=int(input('Digite a quantidade de dias: '))
h=int(input('Digite a quantidadde de horas: '))
m=int(input('Digite a quantidade de minutos: '))
s=int(input('Digite a quantidade de segundos: '))

x=d*24*60*60
y=h*60*60
z=m*60

T=x+y+z+s #onde s é o tempo em segunodos fornecido pelo usuário, será somado
print('O tempo total é de %d' %T)

#Exercício 4

sal=float(input('Digite o valor do salário atual: '))
perc=float(input('Informe o percentual de aumento: '))
aumento= (sal*(perc/100))
novo_salario=sal+aumento
print('O aumento foi de %.2f' %aumento)
print('O novo salário é %.2f' %novo_salario)

#Exercício 5
preço_atual=float(input('Digite o valor atual do produto: '))
desconto=float(input('Digite o percentual do desconto a ser dado no produto: '))
valor_de_desconto=(preço_atual*(desconto/100))
novo_preço = (preço_atual - valor_de_desconto)
print ('O valor de desconto é %.2f' %valor_de_desconto)
print('O novo preço do produto é %.2f' %novo_preço)

#Exercício 6, cinemática básica (vm=d/t), considerando o S.I
d=int(input('Informe a distância a ser percorrida: '))
vm=int(input('Informe a velocidade média a ser atingida: '))
t= d/vm
print ('O tempo percorrido foi %d' %t)

#Exercício 7
C=int(input('Informe uma temperatura em Celsius: '))
F=9*(C/5)+32
print ('A temperatura em Farenheit é %d' %F)

#Exercício 8
F=int(input('Informe uma temperatura em Farenheit: '))
C=(5*(F-32))/9
print('A temperatura em Celsius é: ')

#Exercício 9
km=float(input('Informe a quantidade de quilômetros rodados: '))
d=float(input('Informe  a quantidade de dias utilizados: '))
preço=0.15*km + 60*d
print ('O custo total é de %.2f' %preço)

#Exercício 10
d=int(input('Informe a quantidade de cigarros fumados por dia: '))
a=int(input('Informe quantos fumou: '))
T=(d*365)*a #Total de cigarros fumados
t=T*10 #tempo de vida a menos (em minutos)
print('Ao todo foram fumados %d cigarros' %T)
print ('O indivíduo terá %d minutos a menos de vida' %t)

#Exercício 11
print (len(str(2**1000000))) #o comando len mostra o tamanho da string, por isso a necessidade de converter a classe para string



