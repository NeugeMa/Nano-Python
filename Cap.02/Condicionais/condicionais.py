# Tomada de Decisão: if, elif, else

''' 
Durante o desenvolvimento de um código, existem diversas situações em que a resolução dependerá de uma condição para que ela possa 
seguir seu rumo. 

Isso ocorre muito em nosso dia a dia quando planejamos uma tarefa, mas as “variáveis” do nosso cotidiano fazem com que tenhamos que 
optar por mudanças de planos.

- Exemplo: Quando estimamos um tempo para chegarmos a um local e um simples pneu furado do seu veiculo atrapalha todo seu 
planejamento de tempo. 

Para utilizarmos as tomadas de decisões, vamos identificar como **IF**
A forma de utilizar o comando “if” é bem simples:

**if <condição>:** 

<o que você quer que aconteça caso a condição seja verdadeira>

'''

nota = 8
if nota > 6: 
    print('Aprovado')


# Decisão Simples:
# Uma decisão simples é o caso mais comum e corriqueiro que existirá dentro de um código. 
''' 
Exercício: Você precisará coletar o nome dos pacientes que serão atendidos em uma sala de emergência, porém algumas das pessoas 
deverão ter prioridade no atendimento, portanto vamos definir um atendimento preferencial para idosos, que podem ser identificados 
pela idade maior/igual à 65 anos
'''

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade:"))
prioridade = "NÃO" # muda o valor da variável “prioridade” de acordo com o valor da idade.

if idade>=65:
    prioridade = "SIM"
print(f"O paciente {nome} possui atendimento prioritario? {prioridade}")

# Decisão Composta:
# As tomadas de decisões compostas, são formadas para o direcionamento caso a condição seja verdadeira e caso a condição seja falsa, ela deve avaliar as duas hipóteses
# Por isso nossa estrutura irá ganhar mais um nome o ELSE.

'''
Exercício: Utilizando o código anterior, adicione o ELSE para aqueles que não tenham prioridade 
'''
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade:"))

if idade>=65:
        print(f"O paciente {nome} possui atendimento prioritario")
else: 
    print(f"O paciente {nome} não possui atendimento prioritário")

# Conhecendo o ELIF (if + else)
# A outras situações que podemos encontrar uma situação em que o Verdadeiro e o Falso, simplesmente, não sejam suficientes. 

'''
Exercício: Agora se baseando em todos os exercícios anteriores, vamos adicionar mais coisas: Pessoas com idade igual ou superior a 65, 
receberão atendimento prioritário, mas que também pessoas com suspeita de doenças infectocontagiosas deverão ser direcionadas para a 
sala de espera distintas, por motivos óbvios.
'''

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade: "))
doenca = input("Você possui suspeita de doença infectocontagiosa? (Sim/Não): ")

if idade >= 65:
    print(f"O paciente {nome} possui atendimento prioritário")

elif doenca == 'Sim': 
    print(f"O paciente {nome} deve ser direcionado para a sala de espera de doenças infectocontagiosas")    

else: 
    print(f"O paciente {nome} não possui atendimento prioritário")
    
# Operadores:
# Agora vamos utilizar operadores AND ou OR, que nos permitem colocar duas/mais condições dentro de um único “if” ou “elif”. 
'''
- > Operador AND, queremos dizer que a condição que estiver a esquerda e a condição a direita do operador devem ser verdadeiras para 
que o “if” seja considerado Verdadeiro. Se uma condição retornar Falso, o “if” será Falso.

- > Operador OR determina que se uma das condições for verdadeira, o “if” já deverá retornar Verdadeiro.
'''

''' 
Exercício: Vamos imaginar que a seguinte situação, o paciente chega à triagem que o direcionará à sala de espera na consulta. 
O funcionário da triagem poderá direcionar o paciente para uma das duas salas de esperas, são elas: 

- Branca: Para pacientes sem risco de doenças infectocontagiosa, mas com/sem prioridade
- Amarela: Para pacientes com risco de doença infectocontagiosa, mas com/sem prioridade

'''

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade:"))
doenca = input("Você possui suspeita de doença infectocontagiosa? (Sim/Não): ")

if idade >= 65 and doenca == 'Sim':
    print(f"O paciente {nome} deve ser direcionado para a sala AMARELA de doenças infectocontagiosas - Com prioridade")
    
elif idade < 65 and doenca == 'Sim':
    print(f'O paciente {nome} deve ser direcionado para a sala AMARELA de doenças - Sem prioridade')

elif idade >= 65 and doenca == "Nao":
    print(f"O paciente {nome} será direcionado para sala BRANCA - COM prioridade")
    
elif idade < 65 and doenca == "Nao":
    print(f"O paciente {nome} será direcionado para sala BRANCA - SEM prioridade")
    
else:
    print("Responda a suspeita de doença infectocontagiosa com Sim ou Nao")
    
# Decisões Encadeadas: 
'''
Servem para avaliar uma situação, e dependendo da situação, serão tomadas algumas outras decisões. Por isso, servem como uma 
alternativa para estruturas mais “robustas”. 

Podendo pensar em uma string que não tenha apenas os valores “SIM” e “NÃO”, como exemplo estado civil, que pode ter 
(casado, solteiro, divorciado, viúvo, etc..)
'''

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ")

# PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca_infectocontagiosa=="SIM":
    print("Encaminhe o paciente para sala AMARELA")
elif doenca_infectocontagiosa=="NAO":   
    print("Encaminhe o paciente para sala BRANCA")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero=input("Digite o gênero do paciente: ")
    if genero=="FEMININO" and idade>10:
        gravidez=input("A paciente está grávida? ")
        if gravidez=="SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")
