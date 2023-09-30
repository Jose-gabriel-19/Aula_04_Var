n1= int(input('digite um numero para obter ao quadrado \n'))
print('O quadrado de',n1, 'é:\n', n1*n1) 

nome = input('digite seu nome')
sobrenome = input('digite seu sobrenome')
print(nome+sobrenome) 

n1 = (input('digite um numero'))
n2 = (input('digite outro numero'))
print(n1+n2)

py = 'Python'
n1= input('digite um numero \n')
print(py+n1)


nome = input('Digite seu nome \n ->')
print('\n')
idade = input('Digite sua idade \n ->')
print()
meu_endereco = input('Digite seu endereço \n ->')
print()
cargo = input('Digite seu cargo \n ->')
print()
# print('Meu nome:', nome, '\n','Minha idade:', idade, '\n','Meu endereço:', meu_endereco,'\n', 'Margo é:', cargo)

print(f'Meu nome é {nome}, Minha idade {idade}, Meu endereço {meu_endereco}, Meu cargo {cargo}')


entradaa= input('complete a frase: hoje está ')
print(f'Hoje está {entradaa}')

h = '11'
m = '55'
s = '09'
print(f'agora é {h}:{m}:{s}')

area = '11'
reg = '+55'
nu = '9483-93677'

print(f' o número é: {reg} ({area}) {nu} ')

i1 = '3 ovos'
i2 = '250 ml de leite'
i3 = '3 colheres de sopa de chocolate'
i4 = '1 colher de chá de fermento' 

print(f'{i1}, {i2}, {i3}, {i4}')

ad = input( 'digite um adjetivo:\n')
ad2 = input( 'digite outro adjetivo:\n')
ad3 = input( 'digite o ultimo adjetivo:\n')
print()

print(f'hoje o dia está {ad}, {ad2}, e {ad3}.')


n = float(input('digite um numero'))

if n == 10:
  print( 'o numero é 10')
else:
  print(f'opa está errado {n}')



show = int(input("digite sua idade para acessar o show: \n"))
print()
if show >= 18:
  print()
  print('aproveite o show')
else:
  print('Você não tem idade para acessar ')



n1 = 18
n2 = 45

if n1 < n2:
  print('é maior')
else: 
  print('é menor')



n1 = int(input("digite sua primera nota entre 0 a 10: \n "))
n2 = int(input("digite sua segunda nota entre 0 a 10:\n"))
n3 = int(input("digite sua terceira nota entre 0 a 10: \n"))

if n1+n2+n3 >=15:
  print('passou')
else:
  print('Reprovado')

n1 = int(input("digite sua primera nota entre 0 a 10:\n "))
n2 = int(input("digite sua segunda nota entre 0 a 10:\n"))
n3 = int(input("digite sua terceira nota entre 0 a 10:\n"))
print()
if n1 >= 5:
  print("nota 01:passou")
  print()
else: 
  print('nota 01:não passou')
  print()
if n2 >= 5:
  print("nota 02:passou")
  print()
else:
  print('nota 02:Não passou')
  print()
if n3 >= 5:
  print("nota 03:passou")
  print()
else: 
  print('nota 03:Não passou')

