# Para explicar o programa
print("Insira o valor em metros para ver a conversão em centímetros e milímetros! \n")

# Input para o usuário inserir o valor em metros
valorMetros = int(input("Digite o valor em metros: "))

# Cálculo dos cm e mm
valorCentimetros = valorMetros * 100
valorMilimetros = valorMetros * 1000

# Para pular uma linha
print("")

# Imprimir/mostrar resultado do programa
print("- {} m é equivalente a {} cm e também a {} mm.".format(valorMetros, valorCentimetros, valorMilimetros))