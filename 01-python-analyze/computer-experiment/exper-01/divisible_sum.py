"""
    应用continue 语句，计算累加1~100之间能被3整除的整数和
"""
total = 0
for i in range(1, 101):
    if i % 3 != 0:
        continue
    # print(f"{i} 能被3整除")
    total += i
print(f"1~100之间能被3整除的整数和为: {total}")

result = 0
index = 0
while index < 101:
    if index % 3 != 0:
        index += 1
        continue
    result += index
    index += 1
print(f"1~100之间能被3整除的整数和为: {result}")