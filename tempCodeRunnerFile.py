# 9. Check Whether a Number is Prime

def prime(n):
    divisors = [2, 3, 5, 7]
    if n in divisors:
        return 'Prime'
    else:
        check = [n % i for i in divisors]
        if 0 in check:
            return "Not prime"
        else:
            return "Prime"
            
print(prime(53))