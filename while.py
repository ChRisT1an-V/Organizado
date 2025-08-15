#Atividade 01: Contagem de 1 a 10: Crie um programa que use um laço while para contar de 1 a 10 e exibir cada número.
contador = 0
while contador <=10:
    print(contador)
    contador += 1

#//

#Atividade 02: Soma de Números de 1 a 100: Escreva um programa que use um laço while para somar os números de 1 a 100 e exiba o resultado.
numero = 1
soma = 0
while numero <=100:
    soma += numero
    numero += 1
print('A soma é:', soma)

#//

#Atividade 03: Tabuada de um Número: Faça um programa que solicite um número ao usuário e use um laço while para exibir a tabuada desse número (de 1 a 10).
tabuada = 1
num = int (input('Digite um numero:  '))
while tabuada <=10:
    resultado = num * tabuada
    print(f'{num}  x  {tabuada} = {resultado}')
    tabuada += 1

#//
#Atividade 04: Contagem Regressiva: Desenvolva um programa que use um laço while para exibir uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

contador = 10
while contador >=1:
    print(contador)
    contador -=1
print(' Feliz Ano Novo :D !!')

#//

#Atividade 05: Contagem até o Número Inserido: Crie um programa que solicite um número ao usuário e use um laço while para contar de 1 até o número inserido, exibindo apenas os números ímpares.
contador = 1
num = int (input('Digite um numero: '))
while contador <=num:
    if contador % 2 !=0:
        print(contador)
    contador += 1

#//

#Atividade 06: Tabuada com Condicional: Faça um programa que solicite um número ao usuário e use um laço while para exibir a tabuada desse número (de 1 a 10), mas apenas para os resultados que forem múltiplos de 3.
num = int(input('Digite um numero: '))
tabuada = 1
while tabuada <=10:
    resultado = num * tabuada
    if resultado % 3 == 0:
        print(f'{num} x {tabuada} = {resultado}')
    tabuada += 1
  
#//
#Atividade 07: Média de Notas: Desenvolva um programa que solicite as notas dos alunos até que o usuário digite -1. Calcule e exiba a média das notas inseridas.
soma = 0
quantidade = 0

nota = float(input("Digite uma nota (-1 para parar): "))

while nota != -1:
    soma += nota
    quantidade += 1
    nota = float(input("Digite outra nota (-1 para parar): "))

if quantidade > 0:
    media = soma / quantidade
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")

#// 

#Atividade 08: Escreva um programa que use um laço while para somar números consecutivos começando de 1 e termine quando a soma atingir ou ultrapassar 50.
num = 1
soma = 0
while soma <50:
    soma += num
    print(f'adicionado {num}, soma atual: {soma}')
    num +=1
print(f'soma final {soma}')

#//


