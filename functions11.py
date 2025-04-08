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


# Sample solution

# Define a function named 'perfect_number' that checks if a number 'n' is a perfect number
def perfect_number(n):
    # Initialize a variable 'sum' to store the sum of factors of 'n'
    sum = 0
    
    # Iterate through numbers from 1 to 'n-1' using 'x' as the iterator
    for x in range(1, n):
        # Check if 'x' is a factor of 'n' (divides 'n' without remainder)
        if n % x == 0:
            # If 'x' is a factor of 'n', add it to the 'sum'
            sum += x
    
    # Check if the 'sum' of factors is equal to the original number 'n'
    return sum == n

# Print the result of checking if 6 is a perfect number by calling the 'perfect_number' function
print(perfect_number(6)) 