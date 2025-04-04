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

# Sample Solution

# Define a function named 'test_prime' that checks if a number 'n' is a prime number
def test_prime(n):
    # Check if 'n' is equal to 1
    if (n == 1):
        # If 'n' is 1, return False (1 is not a prime number)
        return False
    # Check if 'n' is equal to 2
    elif (n == 2):
        # If 'n' is 2, return True (2 is a prime number)
        return True
    else:
        # Iterate through numbers from 2 to (n-1) using 'x' as the iterator
        for x in range(2, n):
            # Check if 'n' is divisible by 'x' without any remainder
            if (n % x == 0):
                # If 'n' is divisible by 'x', return False (not a prime number)
                return False
        # If 'n' is not divisible by any number from 2 to (n-1), return True (prime number)
        return True

# Print the result of checking if 9 is a prime number by calling the 'test_prime' function
print(test_prime(9))