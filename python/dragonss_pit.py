# Treinando condicionais

print(
    "\nBem vindo ao Fosso dos Dragões!\n\nPreencha os dados sobre a sua besta e veja se há espaço para ela no fosso.\n"
)

infracoes = 0

nome = str(input("Nome do Dragão: "))

altura = float(input("Altura do dragão: "))

comprimento = float(input("Comprimento do dragão: "))

largura = float(input("Largura (envergadura) do dragão: "))

if altura >= 30:
    print("Dragão muito alto.")
    infracoes += 1

if comprimento >= 100:
    print("Comprimento grande demais.")
    infracoes += 1

if largura >= 150:
    print("Dragão largo demais.")
    infracoes += 1

if infracoes >= 1:
    print(
        f"Dragão {nome}, não coube no fosso ({infracoes} infração(ões) encontrada(as). Terá que ficar na floresta, algum campo aberto.)"
    )


else:
    print("Māzīs, aoñho zaldrīzo kostōba rhaenāmmis")
