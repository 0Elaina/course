"""
设计一个程序，实现一个智能计算器，
能够处理各种数学运算（支持加、减、乘、除运算），并对用户输入进行严格的数据验证和异常处理。
要求：
    对用户的输入进行验证，并能够捕获各种异常情况，
    如输入非数字值(ValueError),除以零（ZeroDivisionError），操作数类型不匹配（TypeError）。
"""


def get_number(prompt):
    while True:
        try:
            val_str = input(prompt).strip()
            val = float(val_str)
            return int(val) if val.is_integer() else val
        except ValueError:
            print("错误: 输入值必须是数字")


def calculate(num1, num2, op):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("操作数类型不匹配, 必须为数值类型")

    match op:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                raise ZeroDivisionError("除零错误! 不能除以 0")
            res = num1 / num2
            return int(res) if res.is_integer() else res
        case "**":
            return num1**num2
        case _:
            raise ValueError(f"不支持的操作符: {op}")


def main():
    print("欢迎使用智能计算器! \n")

    while True:
        num1 = get_number("请输入第一个数字: ")
        num2 = get_number("请输入第二个数字: ")
        op = input("请选择操作 (+, -, *, /, **): ").strip()
        flag = True

        try:
            result = calculate(num1, num2, op)
            print(f"\n结果: {num1} {op} {num2} = {result}\n")

        except ZeroDivisionError as e:
            print(f"\n错误: {e}")
            flag = False
        except TypeError as e:
            print(f"\n错误: 类型错误! {e}")
            flag = False
        except ValueError as e:
            print(f"\n错误: {e}")
            flag = False
        
        tip = "是否继续？(y/n): " if flag else "是否重试？(y/n): "
        choice = input(tip).strip().lower()
        if choice != "y":
            print("感谢使用!")
            break
        print()


if __name__ == "__main__":
    main()
