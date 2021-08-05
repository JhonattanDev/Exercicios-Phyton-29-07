# Imprimir o cabeçalho do jogo
print("***************************************************************")
print("  Digite dois números para ver o resultado da soma entre eles!")
print("*************************************************************** \n")

# Fazendo com que o programa peça ao usuário os 2 números
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Realizar a soma entre os 2 números ja transoformados em "int"
soma = (numero1 + numero2)

# Para pular uma linha
print("")

# Mostrando ao programa que ele deve imprimir a mensagem, junto com o resultado da soma.
print("O resultado da soma dos dois números é {}.".format(soma))