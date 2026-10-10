"""
实验1：根据输入的参数（行数）不同，输出下面图形，定义函数实现（默认3行，可以接收指定的行）。
            *
           ***
          *****
         *******
"""


def print_graph(line: int = 3):
    end = 1
    count = 1
    for i in range(line - 1):
        end += 2
    for i in range(line):
        space_len = (end - count) // 2
        print(" " * space_len + "*" * count + " " * space_len)
        count += 2


if __name__ == "__main__":
    line = int(input("请输入行数："))
    print_graph(line)
