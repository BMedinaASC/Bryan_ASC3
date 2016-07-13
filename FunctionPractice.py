def sumAll(x, y):
    i = x
    result = 0
    while i < y + 1:
        result = i + result
        i = i + 1
    return result
    
num1 = sumAll(1, 10)
num2 = sumAll(7, 24)

print ("The first number is:", num1, "The second number is:", num2)      