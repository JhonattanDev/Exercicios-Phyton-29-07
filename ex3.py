# Fazendo com que o programa peça ao usuário o seu nome, dia e mês de aniversário,
# que após digitado, irão definir as variáveis nome, diaDoAniversario e mesDoAniversario.
nome = input("Digite o seu nome: ")
diaDoAniversario = input("Digite em que dia você faz seu aniversário: ")
mesDoAniversario = input("Digite em que mês você faz seu aniversário: ")

# Mostrando ao programa que ele deve imprimir a mensagem,
# junto com o nome e data de aniversário que foi inserido anteriormente.
print("Olá {}, você faz aniversário no dia {} de {}!".format(nome, diaDoAniversario, mesDoAniversario))