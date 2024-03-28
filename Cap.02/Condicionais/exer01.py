'''
Escreva um programa para ler o ano de nascimento de uma pessoa e escrever uma mensagem que diga se ela poderá ou não votar esse ano 
(não é necessário considerar o mês em que ela nasceu)
'''

ano = int(input("Digite seu ano de nascimento: "))
idade = 2024 - ano 

if idade >= 18:
    print("É obrigatorio votar!")
    
elif idade >= 16: 
    print("Voto é opcional")
    
else: 
    print("Você não pode votar!")