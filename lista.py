#Execercios sobre lista
#atividade 1 Faça a definição de uma lista contendo os números de 1 até 5. Finalmente, utilize o print() para exibir os valores da lista.
numeros = [1, 2, 3, 4, 5]
print (numeros)

#Atividade 2 Faça a definição de uma lista contendo as vogais. Finalmente, utilize o print() para exibir os valores da lista.
vogais = ['a', 'e', 'i', 'o', 'u']
print (vogais)

#Atividade 3 Defina uma lista com 5 itens que tenha, pelo menos, 3 classes diferentes. Utilize o print() para exibir o terceiro elemento dessa lista.
minhas_classes = [42, "Python", 3.14, True, [1, 2, 3]]
print(minhas_classes[2])

#Atividade 4 Crie uma tupla para representar as informações de três palestrantes, cada uma contendo o nome, o tema da palestra e a instituição à qual estão vinculados. Exiba na tela as informações do terceiro palestrante, incluindo nome tema da palestra e instituição.
# Definindo a tupla com informações dos palestrantes
palestrantes = (
    ("Liu kang", "Pasteleiro", "USP"),
    ("Raiden", "Eletricista", "Senai"),
    ("Kabal", "Corredor olimpico", "COB")
)

# Exibindo as informações do terceiro palestrante
nome, tema, instituicao = palestrantes[1]
print("Nome:", nome)
print("Função:", tema)
print("Instituição:", instituicao)

#Atividade 5 Crie uma lista contendo seis frutas de sua escolha. Depois de ter a lista pronta, converta essa lista em uma tupla. Por fim, exiba o conteúdo da tupla resultante para verificar as frutas que foram armazenadas.

frutas = ['maça', 'pera', 'banana', 'laranja', 'uva', 'limão']

frutas_tupla = tuple(frutas)

print(frutas_tupla)
