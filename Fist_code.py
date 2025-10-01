# Atividade 02: Crie um programa que peça ao usuário para digitar: 1.Seu nome; 2.Sua idade; 3.Sua altura; 4.Em seguida, imprima esses valores e seus respectivos tipos.

nome = str (input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
print(f"nome: {nome}")
print(f"idade: {idade}")  
print(f"altura: {altura:.2f}")


