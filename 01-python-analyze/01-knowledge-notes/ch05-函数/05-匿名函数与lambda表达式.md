# 5.5 匿名函数与 lambda 表达式

[🏠 知识总索引](../00-INDEX.md) | [⬅️ 上一节：5.4 变量作用域与LEGB规则](04-变量作用域与LEGB规则.md) | [下一节：5.6 常用内置函数与高阶序列操作 ➡️](06-常用内置函数与高阶序列操作.md)

---

> [!TIP]
> **30秒速记卡**
> - **核心语法**：`lambda [arg1, arg2, ...]: expression`。
> - **纯表达式铁律**：冒号后只能写单一表达式，求值结果自动返回；**严禁包含语句**（禁止写 `return`、赋值 `=`、循环 `for/while` 等）。
> - **参数灵活性**：支持无参、多参、形参默认值以及关键字实参调用。
> - **三元条件运算**：支持行内条件表达式 `value1 if condition else value2`。
> - **杀手级场景**：作为 `sort()` / `sorted()` / `min()` / `max()` 的 `key` 特征提取器，以及存入列表/字典充当轻量函数路由器。

**标签**：`#Python` `#lambda` `#匿名函数` `#高阶函数` `#排序key` `#三元表达式`

---

## 一、`lambda` 语法结构与三大约束

```python
# 语法模板
lambda arg1, arg2, ... : expression
```

```
 lambda    a, b=5    :    a * b if a > 0 else a + b
   │         │       │              │
关键字    形参列表   冒号      单一返回表达式
```

### 与常规 `def` 的三大维度对比

| 维度 | 常规函数 `def` | 匿名函数 `lambda` |
| :--- | :--- | :--- |
| **命名要求** | 必须显式命名，登记入命名空间 | 匿名（即用即弃，亦可绑定给变量） |
| **代码结构** | 允许多行复合语句块 | **单行纯表达式** |
| **控制与返回** | 必须由 `return` 交付数据 | **隐式自动返回**，禁止书写 `return` |

---

## 二、参数配置与三元运算支持

`lambda` 具备完整的函数形参支持能力：

```python
# 1. 默认参数
calc_power = lambda x, n=2: x ** n
print(calc_power(4))     # 16 (采用默认值 n=2)
print(calc_power(4, 3))  # 64 (覆盖默认值)

# 2. 三元条件表达式结合
check_parity = lambda n: "Even" if n % 2 == 0 else "Odd"
print(check_parity(7))   # "Odd"
```

---

## 三、高频工程应用场景

### 1. 复杂数据结构的多维度排序（`key` 参数）
```python
students = [
    {'name': 'Alice', 'score': 92, 'age': 20},
    {'name': 'Bob', 'score': 85, 'age': 19},
    {'name': 'Charlie', 'score': 92, 'age': 18}
]

# 复合规则排序：优先按成绩降序，成绩相同时按年龄升序
students.sort(key=lambda s: (-s['score'], s['age']))
```

### 2. 容器化函数路由器（Function Dispatcher）
利用函数的一等公民特性，将多个 `lambda` 组织为字典：
```python
operations = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y
}

print(operations['mul'](6, 7))  # 42
```
