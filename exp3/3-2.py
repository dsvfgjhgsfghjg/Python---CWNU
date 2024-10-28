# 输入一个字符串，计算其中小写字符、大写字符、数字字符、其他字符的个数。

def characters():
    sentence = input("Enter a sentence: ")
    num_lower = 0
    num_upper = 0
    num_digit = 0
    other = 0

    for n in sentence:
        if(n.islower()):
            num_lower = num_lower + 1
        elif(n.isupper()):
            num_upper = num_upper + 1
        elif(n.isdigit()):
            num_digit = num_digit + 1
        else:
            other += 1
    print("Lower:" + str(num_lower))
    print("Upper:" + str(num_upper))
    print("Digit:" + str(num_digit))
    print("Other:" + str(other))
characters()