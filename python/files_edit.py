# Crie um programa que peça a idade de uma pessoa e se ela possui habilitação (True ou False). O programa deve imprimir True se ela tiver 18 anos ou mais e possuir habilitação, caso contrário False.

idade = int(input('Digite sua idade: '))
CNH = (input('Possui habilitação (True/False): ')).strip().lower()


if idade >= 18 and CNH == 'true':
    print('Possui CNH')
elif idade >= 18 and CNH == 'false':
    print('Rapaz, está na hora de tirar CNH.')
elif idade < 18 and CNH == 'true':
    print('Você é de menor.')
else: 
    print('Você é de menor e não possui CNH.')


