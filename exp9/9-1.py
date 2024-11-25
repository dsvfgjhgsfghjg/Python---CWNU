class InvalidSalaryException(Exception):
    def __init__(self,message="工资不在有效范围内（0-100000）"):
        super().__init__(message)
def getSalaryInput(salary):
    while True:
        try:
            salary = float(input(salary))
            if salary < 0 or salary > 1e5:
                raise InvalidSalaryException()
            return salary
        except ValueError:
            print("输入的值有误")

def main():
    try:
        name = input("输入你的姓名")
        salary = getSalaryInput(f"输入{name}的工资：")
        annual = salary * 12
        print(f"{name}的年薪是{annual:.2f}")
    except InvalidSalaryException as e:
        print(f"出错了：{e}")
    except Exception as e:
        print(f"未预期的错误：{e}")
main()