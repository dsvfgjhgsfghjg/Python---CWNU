def maxnum(*nums):
    # 计算最大值
    if not nums:
        return None
    return max(nums)

# 主程序
print(maxnum(-1, 33, 44, -99, 100))
print(maxnum(1, 4, 95, 3, 78))
