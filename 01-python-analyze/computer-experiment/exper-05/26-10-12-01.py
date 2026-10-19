import pandas as pd

"""
读取数据（mrbook数据），并打印数据集前10条记录
任意读取若干列存入一个dataframe数据类型中并输出
分别按照“大类”和“类别”进行分类统计平均销售量、平均定价，并按照降序排序
输出价格超过70元且销量大于100的数据
将行索引设置为“大类”，并统计每个大类中的图书数量
"""

df = pd.read_excel("./exper-05/mrbook.xlsx")
print(df.head(10))
print('\n' + '=' * 30 + '\n')

df_subset = df[['图书名称', '大类', '类别', '定价', '销量']]
print(df_subset)
print('\n' + '=' * 30 + '\n')

result_dalei = df.groupby('大类')[['销量', '定价']].mean().sort_values(by='销量', ascending=False)
print(result_dalei)
print('\n' + '=' * 30 + '\n')

filtered_data = df[(df['定价'] > 70) & (df['销量'] > 100)]
print(filtered_data)
print('\n' + '=' * 30 + '\n')

df_indexed = df.set_index('大类')
print(df_indexed.head())
print('\n' + '=' * 30 + '\n')

book_count = df_indexed.groupby('大类').size()
print(book_count)