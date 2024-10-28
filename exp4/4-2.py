
dict_data = {
    "数学": "L04",
    "语文": "W01",
    "英语": "W02",
    "物理": "L02",
    "地理": "Q03"
}

dict_data["化学"] = "L03"
dict_data["数学"] = "L01"

dict_data.pop("地理", None)

print("字典内容为:", dict_data)
