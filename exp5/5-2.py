def avgScore(score, n=10, absent_score=0):
    if len(score) < n:
        score = score + [absent_score] * (n - len(score))
    total_score = sum(score[:n])
    return total_score / n

# 主程序
score = [100, 85, 99, 95, 85, 96, 89, 100, 99]
print("按照班级人数计算平均值:", avgScore(score))
print("按照考试人数计算平均值:", avgScore(score, len(score)))
