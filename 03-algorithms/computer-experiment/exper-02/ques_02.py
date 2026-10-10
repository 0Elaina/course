"""
实验2：写函数，接受n个数字，求这些参数数字的和。
"""

def num_sum(*args):
    return sum(args)

if __name__ == '__main__':
    length = int(input("请输入数字个数："))
    nums = [int(input(f"请输入第{i+1}个数字: ")) for i in range(length)]
    print(f"这些数字的和为：{num_sum(*nums)}")