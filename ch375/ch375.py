def add_to_digits(n):    
    length = 0
    while (n%(10**length) != n):
        length += 1

    digits = []

    for i in range(length-1,-1,-1):
        digits.append(n//(10**i))
        n -= digits[length-i-1] * 10**i

    n = 0
    for i in range(0,len(digits)):
        digits[i] += 1
    
    print(digits)

    for i in range(length-1,-1,-1):
        n += digits.pop(0)*(10**i)

    return n   

print(add_to_digits(989))