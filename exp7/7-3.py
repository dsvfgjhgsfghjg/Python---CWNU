import jieba
import re
from collections import Counter

def is_chinese(word):
    return re.match(r'[\u4e00-\u9fff]+', word) is not None

with open('wind.txt', 'r', encoding='utf-8') as file:
    txt = file.read()

ls = jieba.lcut(txt)

filtered_ls = [word for word in ls if is_chinese(word)]

word_counts = Counter(filtered_ls)

freq_word = word_counts.most_common(10)


print("词频前10位的中文词及出现次数：")
for word, count in freq_word:
    print(f"{word}: {count}")