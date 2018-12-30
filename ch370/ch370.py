def final_digit(code):
    digit_list = get_list(code)
    result = 0
    
    for i in range(len(digit_list)):
        if (i % 2 == 0):
            result += digit_list[i]
    print(result)
    result *= 3
    print(result)
    for i in range(len(digit_list)):
        if (i % 2 != 0):
            result += digit_list[i]
    print(result)
    result = result % 10
    print(result)
    if (result != 0):
        result = 10 - result
 
    return result

def get_list(code):
    digit_list = []
    code_str = str(code)
    
    while(len(code_str) != 11):
        code_str = "0" + code_str

    for i in code_str:
        digit_list.append(int(i))
    
    return digit_list

print("Enter incomplete upc code")
code = int(input())
print(final_digit(code))
