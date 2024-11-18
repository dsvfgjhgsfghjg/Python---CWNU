# 定义加密/解密函数（与之前相同）
def encrypt_decrypt_special(input_file, output_file, key, decrypt=False):
    shift = key if not decrypt else -key
    with open(input_file, 'r') as infile:
        content = infile.read()

    encrypted_decrypted_content = []
    for char in content:
        if char.isalpha():
            # 凯撒密码加密/解密字母
            base = ord('a') if char.islower() else ord('A')
            new_char = chr((ord(char) - base + shift) % 26 + base)
        elif char.isdigit():
            # 对数字进行模10加法（处理单个数字字符的位移）
            new_char = str((int(char) + shift) % 10)
        else:
            # 对非字母非数字字符进行特殊处理
            if char == '<':
                new_char = '@' if not decrypt else '<'
            elif char == '>':
                # 假设'>'加密成了'#'
                new_char = '#' if not decrypt else '>'
            else:
                new_char = char  # 其他字符保持不变

        encrypted_decrypted_content.append(new_char)

    encrypted_decrypted_content = ''.join(encrypted_decrypted_content)

    with open(output_file, 'w') as outfile:
        outfile.write(encrypted_decrypted_content)

# 创建输入文件并写入内容
input_filename = 'input.txt'
with open(input_filename, 'w') as infile:
    infile.write('abc123<def>')

# 加密文件
encrypted_filename = 'encrypted.txt'
encrypt_decrypt_special(input_filename, encrypted_filename, key=4)
print(f"文件已加密并保存到 {encrypted_filename}")

# 读取加密后的文件内容（可选，用于验证）
with open(encrypted_filename, 'r') as encrypted_file:
    encrypted_content = encrypted_file.read()
    print(f"加密后的内容: {encrypted_content}")

# 解密文件
decrypted_filename = 'decrypted.txt'
encrypt_decrypt_special(encrypted_filename, decrypted_filename, key=4, decrypt=True)
print(f"文件已解密并保存到 {decrypted_filename}")

# 读取解密后的文件内容（可选，用于验证）
with open(decrypted_filename, 'r') as decrypted_file:
    decrypted_content = decrypted_file.read()
    print(f"解密后的内容: {decrypted_content}")