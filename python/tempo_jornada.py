print('Seja bem vindo aventureiro!\n\nGostaria de saber quanto tempo gostou em sua jornada?')
print('Insira abaixo o valor que passou em aventura e descubra o equivalente em vidas humanas.')

tempo = float(input('Tempo de Jornada: '))

humano = tempo // 80

seculo = tempo // 100

resto_seculo = tempo % 100

decada = resto_seculo // 10

anos_quebrados = resto_seculo % 10

print(f'De acordo com os astros, ficastes fora o equivalente a: {humano} vidas humanas\n {decada} décadas\n {seculo} séculos')

if anos_quebrados > 0:
    print(f'{anos_quebrados} anos que sobraram da sua aventura. Quase a idade de uma criança.')