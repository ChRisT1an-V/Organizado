#Atividade 1 Crie um conjunto vazio chamado frutas e adicione as seguintes frutas a ele: "maçã", "banana", "uva", "laranja" e "morango". Em seguida, imprima o conjunto.
frutas = set()

frutas.add("maçã")
frutas.add("banana")
frutas.add("uva")
frutas.add("laranja")
frutas.add("morango")

print(frutas)

#Atividade 2 Crie um conjunto de frutas, Verifique se a fruta  "banana " está presente no conjunto frutas e imprima o resultado.
frutas = {"maçã", "banana", "uva", "laranja", "morango"}
if "banana" in frutas:
    print("banana")
  
#Atividade 3 Crie um conjunto chamado frutas_vermelhas e adicione as seguintes frutas a ele: "morango", "cereja" e "framboesa". Em seguida, imprima o conjunto.

frutas_vermelhas = {"maça", "melancia", "tomate", "acerola"}
frutas_vermelhas.add("morango")
frutas_vermelhas.add("cereja")
frutas_vermelhas.add("framboesa")
print(frutas_vermelhas)

#atividade 4 Remova a fruta "cereja" do conjunto frutas_vermelhas e imprima o conjunto atualizado.
frutas = {"cereja", "melancia", "tomate", "acerola"}
frutas.remove("cereja")
print(frutas)

#atividade 5 Crie dois conjuntos, A e B, e realize a união dos dois conjuntos.
a = {1, 2, 3}
b = {4, 5, 6}
uniao = a.union(b)
print(uniao)

#atividade 6 Crie dois conjuntos, A e B, e realize a interseção dos dois conjuntos.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
intersecao = a.intersection(b)
print(intersecao)

#atividade 7 Escreva um programa que EXIBA um dicionário contendo informações de pessoas (nome, idade) e exiba essas informações.

pessoa = {
    'nome': 'Chris',
    'idade': 23
}
print(pessoa)

#atividade 8 Adicione uma nova chave "cidade" ao dicionário pessoa com o valor "São Paulo" e imprima o dicionário atualizado.
pessoa = { 
    'nome': 'Chris',
    'idade': 23
}
pessoa['cidade'] = 'São Paulo'
print(pessoa)

#atividade 9 Remova a chave "idade" do dicionário pessoa e imprima o dicionário atualizado.
pessoa = {
    'nome': 'Chris',
    'idade': 23,
    'cidade': 'São Paulo'
}
del pessoa['idade']
print(pessoa)

# atividade 10 Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email. Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, o número de telefone e o endereço de email. Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.
contato = {}
contato['nome'] = input('Digita o seu nome: ')
contato['telefone'] = input('Digita o seu telefone: ')
contato['email'] = input('Digita o seu e-mail: ')
print('Suas informações')
print(contato)


#atividade 11 Crie um dicionário que relacione nomes de alunos às suas notas em uma disciplina. Calcule a média das notas e exiba-a.

alunos = {
    "Kitana": [8.5, 9.0, 7.5],
    "Kung Lao": [7.0, 6.5, 8.0],
    "Liu kang": [9.5, 9.0, 8.5],
    "Jonny Cage": [6.0, 7.0, 5.5]
}

print("NOTAS DOS ALUNOS (Múltiplas Avaliações):")
print("=" * 50)

soma_geral = 0
total_notas = 0

for aluno, notas in alunos.items():
    media_aluno = sum(notas) / len(notas)
    soma_geral += sum(notas)
    total_notas += len(notas)
    
    print(f"{aluno}: {notas} → Média: {media_aluno:.1f}")

media_geral = soma_geral / total_notas

print("\n" + "=" * 50)
print(f"MÉDIA GERAL DA TURMA: {media_geral:.1f}")

#atividade 12 Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.

produtos = {
    "notebook": 2500.00,
    "mouse": 50.00,
    "teclado": 120.00,
    "monitor": 800.00,
    "headset": 150.00
}
print("CHAVES (Produtos):")
print("-" * 25)
for chave in produtos:
    print(f"• {chave}")

print("\nVALORES (Preços):")
print("-" * 25)
for valor in produtos.values():
    print(f"• R$ {valor:.2f}")

print("\nRESUMO COMPLETO:")
print("-" * 25)
for chave, valor in produtos.items():
    print(f"{chave.capitalize()}: R$ {valor:.2f}")
    
# Atividade 13 Crie um programa que simule um sistema de votação. O programa deve permitir que os eleitores escolham entre opções de eleitores e conte os votos para cada opção. Use um dicionário para armazenar os resultados da votação, onde as chaves são as opções e os valores são o número de votos para cada opção. O programa deve permitir que os eleitores votem, encerre a votação e exiba os resultados finais. Use While True e pare o programa somente se o usuário digitar o número 0 e exiba os resultados finais.

votos = {
    "Candidato A": 0,
    "Candidato B": 0,
    "Candidato C": 0,
    "Voto Nulo": 0,
    "Voto em Branco": 0
}

print("SISTEMA DE VOTAÇÃO SIMPLES")
print("1 - Candidato A | 2 - Candidato B | 3 - Candidato C")
print("4 - Nulo | 5 - Branco | 0 - Encerrar")

while True:
    try:
        voto = int(input("\nSeu voto: "))
        
        if voto == 0:
            break
        elif voto == 1:
            votos["Candidato A"] += 1
        elif voto == 2:
            votos["Candidato B"] += 1
        elif voto == 3:
            votos["Candidato C"] += 1
        elif voto == 4:
            votos["Voto Nulo"] += 1
        elif voto == 5:
            votos["Voto em Branco"] += 1
        else:
            print("Opção inválida! Use 1-5 ou 0 para sair.")
            continue
            
        print("Voto computado!")
        
    except ValueError:
        print("Digite apenas números!")

# Resultados finais
print("\n" + "=" * 30)
print("RESULTADOS FINAIS:")
for candidato, votos in votos.items():
    print(f"{candidato}: {votos} votos")

total = sum(votos.values())
vencedor = max(votos, key=votos.get)
print(f"\nTotal de votos: {total}")
print(f"Vencedor: {vencedor}")
