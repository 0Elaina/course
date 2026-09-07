"""
    现要为一条街的住户制作门牌号。这条街一共有2020位住户，门牌号从1到2020编号。
    小蓝制作门牌的方法是先制作0到9这几个数字字符，最后根据需要将字符粘贴到门牌上，
    例如：门牌1017需要依次粘贴字符1、0、1、7，即需要1个字符0,2,个字符1,1个字符7。
    
    请问要制作所有的1到2024号门牌，每个字符总共需要多少个？
"""
ans = {}
for i in range(1, 2025):
    for char in str(i):
        ans[char] = ans.get(char, 0) + 1
for char in sorted(ans.keys()):
    print(f"char:{char}, value:{ans[char]}")