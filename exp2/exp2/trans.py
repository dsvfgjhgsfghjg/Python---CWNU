
if __name__ == "__main__":
    sentence = input("请输入一个只包括字符和空格的句子: ")

    words = sentence.split()

    reversed_words = words[::-1]

    reversed_sentence = " ".join(reversed_words)

    print("反转后的句子是:", reversed_sentence)