"""
输入一个整数，判断它是否水仙花数。
所谓水仙花数，是指这样的一些三位整数：各位数字的立方和等于该数本身
例如：153=1^3+5^3+3^3，因此153是水仙花数。
"""

while True:
    num = input("请输入一个三位整数: ")
    if len(num) != 3 or not num.isdigit():
        print("输入错误，请输入一个三位整数。")
        continue
    num_list: list[str] = list(num)
    result = sum(int(digit) ** 3 for digit in num_list)
    if result == int(num):
        print(f"{num} 是水仙花数。")
        break
    else:
        print(f"{num} 不是水仙花数。")
        continue
