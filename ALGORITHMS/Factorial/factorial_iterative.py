def factorial(number):
    fact = 1
    count = 1

    while count != number+1:
        fact = fact * count
        count += 1
    
    return fact

print(factorial(5))
print(factorial(4))
print(factorial(8))
print(factorial(0))
print(factorial(1))