def calcula(valor):
    lista = [100,50,20,10,5,2,1]
    notas = [0,0,0,0,0,0,0]

    notas[0] = valor//lista[0]
    resto = valor%lista[0]
    for i in range(1,len(lista)):
        notas[i] = resto//lista[i]
        resto = resto%lista[i]
    return notas

print("Seja bem-vindo(a) ao nosso caixa! \n Qual valor você quer sacar?")
valor = int(input("Digite o valor: "))
notas = calcula(valor)

print("Você precisa de: ", notas[0], " notas de 100")
print("Você precisa de: ", notas[1], " notas de 50")
print("Você precisa de: ", notas[2], " notas de 20")
print("Você precisa de: ", notas[3], " notas de 10")
print("Você precisa de: ", notas[4], " notas de 5")
print("Você precisa de: ", notas[5], " notas de 2")
print("Você precisa de: ", notas[6], " notas de 1")
