# Algoritmos:
''' Termo utilizado na área de TI para definir um conjunto básico de regras, variáveis, instruções e condicionantes que definem o 
funcionamento de um software. Eles funcionam como uma receita de bolo, guiando o computador de acordo com as interações do usuário. 
- Nesse sentido, a estrutura de um algoritmo é moldada da seguinte maneira:T

'''
#  Variáveis:
''' Utilizado para definir um ou mais valores que são manipulados pelos programas durante a sua operação. O nome “variável” 
é utilizado por ser um tipo de conteúdo que pode apresentar diferentes valores enquanto o sistema está em execução.

'''

# Tipos de Dados 
# INT (inteiro)
''' As variáveis int são utilizadas para definirem números inteiros. Eles podem ser positivos ou negativos. Porém, não podem incluir 
números com duas casas decimais.'''

# Float
''' Utilizadas para armazenar números reais. '''

# Double 
''' Semelhantes às variáveis float. Elas permitem o armazenamento de números reais, ou seja, com ponto flutuante, mas 
com precisão dupla. 
'''

# Char 
''' Utilizado para armazenar um único caractere (como uma letra). Nesse caso, as variáveis desse tipo não podem ser utilizadas em 
operações de soma, subtração, divisão ou multiplicação. Afinal, o software interpretará o conteúdo como se ele fosse uma letra.
'''

# String 
''' 
Utilizadas para o armazenamento de faixas de texto.
'''

# Boolean 
'''
Implementadas com um único objetivo: adotar valores de verdadeiro ou falso. Isso permite ao software validar registros, definir quais 
passos tomar após uma ação do usuário, ou automatizar processos. 
'''

# Exemplos em Códigos:
nome="Mariana"                  # Variável tipo: String
empresa="Jython"                # Variável tipo: String
qtde_funcionarios=500           # Variável tipo: int
mediaMensalidade=856.50         # Variável tipo: float

print(nome + 'trabalha na empresa ' + empresa)                      # Exibimos o valor das variáveis nome e empresa
print("Possui: ", qtde_funcionarios, " funcionarios.")              
print("A média da mensalidade é de: " + str(mediaMensalidade))

