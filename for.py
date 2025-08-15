# Atividade 01: Tabuada de um Número: Faça um programa que solicite um número ao usuário e use um laço for para exibir a tabuada desse número (de 1 a 10).
num = int (input('Tabuada do: '))
for i in range(1,11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')

#//
#Atividade 02: Soma de Números de 1 a 100: Crie um programa que use um laço for para somar todos os números de 1 a 100 e exiba o resultado.
num = 0
for i in range(1,101):
    num += i
    print(i, num)
print(f"A soma dos números de 1 a 100 é: {num}")

#//

#Atividade 03: Caractere por Caractere: Escreva um programa que solicite uma palavra ao usuário e use um laço for para exibir cada caractere da palavra em uma linha separada.
nome = str(input('Digite seu nome: '))
for i in nome:
    print(i)
  
  #//
#Atividade 04: Contagem Regressiva de 10 a 1: Desenvolva um programa que use um laço for para fazer uma contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".

for i in range(10,0,-1):
    print(i)
print('Feliz Ano Novo !!')

#Atividade 05: Contagem de Números Positivos e Negativos: Escreva um programa que solicite ao usuário 10 números e use um laço for com uma condicional para contar quantos são positivos e quantos são negativos.
positivos = 0
negativos = 0
for i in range(1, 11):
    numero = float(input(f"Digite o {i}º número: "))   
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"números positivos: {positivos}")
print(f"números negativos: {negativos}")

#///

#Atividade 06:Soma de Números Pares:Escreva um programa que use um laço for para somar todos os números pares de 1 a 50 e exiba o resultado final.
soma = 0
for i in range(1,51):
    if i % 2 == 0:
        soma+= i
        print(i, soma)
    
print(f'soma dos numeros é: {soma}')

