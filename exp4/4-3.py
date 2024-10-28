
ls_score = ["A", "B", "A", "C", "B", "A", "C", "A", "B", "D", "C", "B", "A", "B", "C"]

d = {}

for score in ls_score:
    d[score] = d.get(score, 0) + 1

sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)

print("各等级人数统计：")
for level, count in sorted_d:
    print(f"{level}等级的人数: {count}")
