# 计算偶数和
def even ():
    summary =0
    for i in range (1,101):
        if i % 2 == 0:
            summary+=i
        else:
            pass

    print(summary)
even()