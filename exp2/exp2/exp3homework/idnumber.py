def extract_birthdate_from_id(id_number):
    if len(id_number) != 18:
        return "身份证号必须是18位"

    birthdate_str = id_number[6:14]

    try:
        year = birthdate_str[:4]
        month = birthdate_str[4:6]
        day = birthdate_str[6:]
        from datetime import datetime
        datetime(int(year), int(month), int(day))

        return f"{year}年{month}月{day}日"
    except ValueError as e:
        return "身份证号中的出生年月日部分不合法"


if __name__ == "__main__":
    user_input = input("请输入你的18位身份证号码: ")
    result = extract_birthdate_from_id(user_input)
    print("你的出生年月日是:", result)