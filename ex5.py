# Pra explicar o programa
print("Digite abaixo o valor para verificar se é isalpha, isalnum, isnumeric, isupper, islower! \n")

# Input para o usuário inserir o valor que ele deseja conferir
valor = input("Digite o que você deseja verificar: ")

# Para pular uma linha após onde o usuário irá inserir o valor
print("")

# Aqui, depois do igual, confere se o valor é o não isalpha, isalnum, isnumeric, etc.
# Após a conferência , ele retorna a variável true ou false, transforando em uma variável boolean
letras = valor.isalpha()
alfanumerico = valor.isalnum()
numerico = valor.isnumeric()
letrasMaiusculas = valor.isupper()
letrasMinusculas = valor.islower()

# Parte que vai imprimir as informações ao usuário

# Mostrar se é isalpha ou não
if(letras == True):
    print("- Esse valor digitado é apenas constituído por letras do alfabeto (isalpha = True).")
elif(letras == False):
    print("- Esse valor digitado não é constituído por letras do alfabeto (isalpha = False).")

# Mostrar se é isalnum ou não
if(alfanumerico == True):
    print("- Esse valor digitado é Alfanumérico (isalnum = True).")
elif(alfanumerico == False):
    print("- Esse valor digitado não é Alfanumérico (isalnum = False).")

# Mostrar se é isnumeric ou não
if(numerico == True):
    print("- Esse valor digitado é numérico (isnumeric = True).")
elif(numerico == False):
    print("- Esse valor digitado não é numérico (isnumeric = False).")

# Mostrar se é isupper ou não
if(letrasMaiusculas == True):
    print("- Esse valor digitado é constituído apenas por letras maiúsculas (isupper = True).")
elif(letrasMaiusculas == False):
    print("- Esse valor digitado não é constituído por letras maiúsculas (isupper = False).")

# Mostrar se é islower ou não
if(letrasMinusculas == True):
    print("- Esse valor digitado é constituído apenas por letras minúsuclas (islower = True).")
elif(letrasMinusculas == False):
    print("- Esse valor digitado não é constituído por letras minúsuclas (islower = False).")
