# 2. Sum All Numbers in a List

def soma(lista):
    calculo = 0
    for i in lista:
        calculo += i
    return calculo

print(soma([8, 2, 3, 0, 7]))
