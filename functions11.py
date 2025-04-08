# 11. Check if a Number is Perfect
# Número positivo



def perfection():
    num = int(input('Input a interger number to be checked: '))
    soma = 0    
    divisors = [n for n in range(1, num)
                if num % n == 0
                ]
    for n in divisors:
        soma += n
    return "It is a perfect number." if soma == num else "It is not a perfect number."

print(perfection())
