from pathlib import Path
import sys

"""
编写一个 Python 程序，实现一个简单的文本统计工具。程序应实现以下功能：
（1）用户输入：程序运行时，提示用户输入要统计的文本文件名（例如 input.txt）。

（2）文件存在性检查：如果文件不存在，程序应捕获异常并输出友好提示：“错误：文件不存在，请检查文件名。”
然后程序结束。

（3）统计内容：

行数：统计文件中的总行数（按换行符 \n 分隔，空行也计为一行）。
单词数：统计文件中所有单词的数量。
单词定义为由空白字符（空格、制表符、换行等）分隔的连续字符序列（使用 str.split() 即可，它会自动处理空白分隔）。
字符数：统计文件中的总字符数（包括空格、换行符等所有字符）。
（4）结果写入：

将统计结果以“键:值”格式写入到文件 result.txt 中，每行一个统计项，格式如下：
行数: 10

单词数: 120

字符数: 800

（5）覆盖处理：如果 result.txt 文件已存在，则询问用户是否覆盖。
输入 y（不区分大小写）表示覆盖，输入其他任意键则退出程序。

（6）程序结束：操作完成后，输出“统计完成，结果已保存至 result.txt”。
"""


def main():
    filename = input("请输入文件名: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("错误：文件不存在，请检查文件名。")
        sys.exit()
    except Exception as e:
        print("读取文件时发生错误: {e}")
        sys.exit()

    char_count = len(content)
    word_count = len(content.split())
    line_count = len(content.splitlines()) if content else 0

    output_file = Path("result.txt")
    if output_file.exists():
        user_choice = (
            input(f"文件 {output_file.name} 已存在, 是否覆盖? (y/n): ").strip().lower()
        )
        if user_choice != "y":
            print("操作取消, 程序已退出")
            sys.exit()

    result_txt = (
        f"行数: {line_count}\n" f"单词数: {word_count}\n" f"字符数: {char_count}\n"
    )

    try:
        output_file.write_text(result_txt, encoding="utf-8")
    except Exception as e:
        print(f"文件写入时发生错误: {e}")
        sys.exit()

    print(f"统计完成, 结果已保存至 {output_file.resolve()}")


if __name__ == "__main__":
    main()
