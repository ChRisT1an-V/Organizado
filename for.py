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

#// 

#Atividade 07: Contagem de Vogais em uma Palavra: Crie um programa que solicite uma palavra ao usuário e use um laço for com uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.

palavra = str (input('Digite a palavra: '))
vogais = 'aeiouAEIOU'
contador = 0
for i in palavra:
    if i in vogais:
        contador += 1
print(f'Na palavra {palavra} tem total  {contador} vogais')

#// 

#Atividade 08: Cálculo de Média de Notas: Escreva um programa que solicite 5 notas de alunos. Use um laço for para somar as notas e uma condicional para exibir a média e a classificação ("Aprovado" para média >= 6, "Reprovado" para média < 6).
soma = 0
for i in range(1, 6):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma += nota

media = soma / 5
print(f"Média: {media:.2f}")

if media >= 6:
    print("Aprovado")
else:
    print(" Reprovado")
#//

#Atividade 09: Verificar Números Pares e Impares com Interrupção: Crie um programa que use um laço for para contar de 1 a 20. Use condicionais para identificar números pares e ímpares. Pare o loop ao encontrar o número 15, usando break.

for i in range(1, 21):
    if i %2 == 0:
        print('Par:', i)
    else:
        print('Impar:', i)

    if i == 15:
        print('O Numero 15 foi encontrado, fim.')
        break
#//

#Atividade 10: Peça ao usuário para inserir 10 números. Use um laço for com condicionais para contar quantos são positivos e quantos são negativos. Pare o loop se o número 0 for inserido, usando break.
positivo = 0
negativo = 0
tentativa = 0
for i in range(10):
    numero = int(input('Digite o numero: '))
    tentativa += 1
    if numero == 0:
        print(' Você acertou o numero 0, fim.')
        break
    elif numero > 0:
        positivo += 1
        print('Numero positivo:', numero)
    else:
        negativo += 1
        print('Numero negativo:', numero)
    print(f'Tentativa {tentativa} de 10')
