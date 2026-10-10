import re

"""
    读取文件learning.txt中的每一行（这文件中包含了python字符串），
    将其中的“python”都替换为“java”，并将修改后的各行打印到屏幕上。
"""


with open("leading.txt", "r", encoding="utf-8") as file:
    for line in file:
        modified_line = re.sub(r'python', "java", line, flags=re.IGNORECASE)
        print(modified_line, end="")
