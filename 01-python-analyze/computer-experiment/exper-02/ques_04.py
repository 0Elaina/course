"""
实验4：编写函数，计算形式如a+aa+aaa+aaaa+...+aaa...aaa的表达式的值，其中a为小于10的自然数。
"""


def calc_sum(a: int) -> str:
    if a < 1 or a >= 10:
        return "输入的数不是小于10的自然数"
    total = sum(int(str(a) * i) for i in range(1, a + 1))
    result = ""
    for i in range(a - 1):
        result += f"{str(a) * (i + 1)} + "
    result += f"{str(a) * a} = {total}"
    return result


if __name__ == "__main__":
    a = int(input("请输入一个小于10的自然数："))
    print(calc_sum(a))
