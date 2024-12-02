import tkinter as tk
from tkinter import messagebox
from math import gcd

def calculate_lcm(a,b):
    if a<=0 or b<=0 :
        return "输入正整数！"
    return abs(a*b)

def on_calculate():
    try:
        num1 = int(txt.get())
        num2 = int(txt2.get())
        lcm = calculate_lcm(num1,num2)
        if isinstance(lcm,str) and "请输入整数！" in lcm:
            result_var.set(lcm)
        else:
            result_var.set(f"{num1}和{num2}的最小公倍数是{lcm}")
    except ValueError:
        result_var.set("请输入有效整数。")

root = tk.Tk()
label0 = tk.Label(root,text="第一个整数：")
label0.grid(row=0,column=0,padx=10,pady=10)
txt = tk.Entry(root,width=10)
txt.grid(row=0,column=1,padx=10,pady=10)
label1 = tk.Label(root,text="第二个整数：")
label1.grid(row=1,column=0,padx=10,pady=10)
txt2 = tk.Entry(root,width=10)
txt2.grid(row=1,column=1,padx=10,pady=10)

calculate_button= tk.Button(root,text="计算",command=on_calculate)
calculate_button.grid(row=2,column=0,padx=10,pady=10)

result_var = tk.StringVar()

label3 = tk.Label(root,textvariable=result_var,width=30)
label3.grid(row=3,column=0,padx=10,pady=10)
root.mainloop()