import math

# Pra explicar o programa
print("Digite um valor abaixo para ver seu dobro, triplo, e raíz quadrada dele! \n")

# Input para o usuário inserir o valor
valor = int(input("Digite o valor: "))

# Aqui será realizados os cálculos que definirão as variáveis
dobro = valor * 2
triplo = valor * 3
raizQuadrada = math.sqrt(valor)

# Para pular uma linha
print("")

# Imprimir/mostrar o resultado do programa
print("O valor digitado foi {}, sendo o seu dobro {}, seu triplo {},"
      " e sua raíz quadrada {}.".format(valor, dobro, triplo, raizQuadrada))
