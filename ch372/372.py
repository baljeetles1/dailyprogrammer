def perfectly_balanced(arr):
    x = 0
    y = 0
    
    for i in arr:
        if i == 'x':
            x += 1
        if i == 'y':
            y += 1

    if x==y:
        return True
    else:
        return False

print(perfectly_balanced("yyxyxxyxxyyyyxxxyxyx"))
