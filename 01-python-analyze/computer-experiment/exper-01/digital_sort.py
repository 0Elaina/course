"""
    按照数位之和给数排序，当两个数各个数位之和不同时，
    将数位和较小的排在前面，当数位之和相等时，将数值小的排在前面。
    例如：2022排在409的前面，因为2-22的数位之和是6，小于409的数位之和13；
    又如，6排在2022前面，因为它们的数位之和相同，而6小于2022。
    
    编程实现：给定正整数n，m，请问对1到n采用这种方法排序时，排在第m个的元素是多少？

    【样例输入】：
        13
        5
    【样例输出】：
        3   
    【样例说明】：
        1到13的排序为：1,10,2,11,3,12,4,13,5,6,7,8,9。第5个数为3。
"""
def get_digit_sum(num: int) -> int:
    """计算十进制数位之和"""
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s
    
while True:
    n = int(input("请输入最大的整数 n: "))
    m = int(input("请输入要获取的第 m 个整数: "))
    if m > n or n < 0:
        print("m 不能大于 n 或小于 0")
        continue
    
    num_list = list(range(1, n + 1))
    num_list.sort(key = lambda x: (get_digit_sum(x), x))
    print(f"第 {m} 个数字为: {num_list[m - 1]}")
    break