'''
Escreva um código que solicitará o nível de acesso de uma pessoa que pode ser, ADM, USR ou GUEST e o gênero dessa pessoa, em 
exemplo: caso seja ADM, deverá exibir “Olá administrador (para homens)/ Olá administradora (para mulheres) 

USR - usuário 
GUEST - visitante
'''

cargo = input("Digite seu cargo (ADM, USER, GUEST): ")
if cargo == 'ADM' or cargo == 'USER': 
    genero = int(jnput("Digite seu gênero | 1. Feminino 2. Masculino: "))
    if cargo == 'ADM': 
        if genero == 1: 
            print("Olá administradora")
        else: 
            print('Olá administrador')
            
    else: 
        if genero == "FEMININO":
            print("Olá usuárioa!")
        else:
            print("Olá usuário!")

elif cargo == "GUEST":
    print("Olá visitante!")
else: 
    print("Olá desconhecido(a)!")
        
    