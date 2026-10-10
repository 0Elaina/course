"""
实验3：
    编写函数，接收一个正偶数为参数，
    输出两个素数，并且这两个素数之和等于原来的正偶数。
    如果存在多组符合条件的素数，则全部输出。

如：
5 + 61 = 66
7 + 59 = 66
13 + 53 = 66
19 + 47 = 66
23 + 43 = 66
29 + 37 = 66
"""
def get_prime_pair(num: int) -> str:
    if num % 2 != 0 or num <= 1:
        return "输入的数不是正偶数"
    
    prime_set: set = set()
    for i in range(2, num):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            prime_set.add(i)
    
    for prime in prime_set:
        other = num - prime
        if prime <= other and other in prime_set:
            print(f"{prime} + {other} = {num}")    
            
if __name__ == '__main__':
    num = int(input("请输入一个正偶数："))
    get_prime_pair(num)
    
