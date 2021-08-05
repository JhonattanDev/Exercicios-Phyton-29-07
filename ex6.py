# Pra explicar o programa
print("Digite dois valores abaixo para ver a soma entre eles, e o antecessor e sucessor do resultado! \n")

# Fazendo com que o programa peça ao usuário os 2 números
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))



# Realizar a soma entre os 2 números ja transoformados em "int"
soma = (numero1 + numero2)
# Realizar o calcúlo para o antecessor e sucessor do resultado da soma
antecessor = soma - 1
sucessor = soma + 1

# Para pular uma linha
print("")

# Mostrar/imprimir o resultado
print("A soma de {} + {} resulta em {}.".format(numero1, numero2, soma))
print("O antecessor de {} é {}, e o sucessor de {} é {}.".format(soma, antecessor, soma, sucessor))
