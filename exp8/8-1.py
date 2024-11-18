# 读取文件数据
with open('numbers.txt', 'r') as file:
    data = file.readlines()

# 数据预处理
numbers = []
for line in data:
    try:
        num = float(line.strip())
        numbers.append(num)
    except ValueError:
        continue

n = len(numbers)
arithmetic_mean = sum(numbers) / n

sorted_numbers = sorted(numbers)
if n % 2 == 1:
    median = sorted_numbers[n // 2]
else:
    median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

print("算术平均数：", arithmetic_mean)
print("中位数：", median)