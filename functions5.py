# 5. Factorial of a Number

def fatora(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

print(fatora(10))
