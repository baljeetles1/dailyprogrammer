def additive_persistence(n,count):    
    length = 0
    while (n%(10**length) != n):
        length += 1

    if (length == 1):
        return count

    digits = []

    for i in range(length-1,-1,-1):
        digits.append(n//(10**i))
        n -= digits[length-i-1] * 10**i

    n = 0
    for i in range (0, len(digits)):
        n += digits[i]

    count += 1
    return additive_persistence(n,count)

print(additive_persistence(199,0))