import tkinter as tk

def calculate_sum():
    try:
        user_input = entry.get()
        numbers = [int (num.strip()) for num in user_input.split(',')]
        total = sum(numbers)
        result_label1.configure(text=f"整数之和：: {total}")
    except ValueError:
        result_label1.configure(text="请输入有效的整数列表，用半角逗号分割。")

root = tk.Tk()
root.title("整数求和计算器")

prompt_label = tk.Label(root,text="请输入若干整数，用半角逗号分割：")
prompt_label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

calculate_button = tk.Button(root,text='计算',command=calculate_sum)
calculate_button.pack(pady=10)
result_label1 = tk.Label(root,text="0",width=40)
result_label1.pack(pady=5)
root.mainloop()