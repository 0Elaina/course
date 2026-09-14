# 5.4 函数变量作用域与 LEGB 规则

[🏠 知识总索引](../00-INDEX.md) | [⬅️ 上一节：5.3 函数返回值机制](03-函数返回值机制.md) | [下一节：5.5 匿名函数与 lambda 表达式 ➡️](05-匿名函数与lambda表达式.md)

---

> [!TIP]
> **30秒速记卡**
> - **LEGB 查找铁律**：按 $\text{Local (局部)} \to \text{Enclosing (闭包外层)} \to \text{Global (全局)} \to \text{Built-in (内置)}$ 顺序由内向外只读查找，遇阻即停，查无则报 `NameError`。
> - **同名遮蔽（Shadowing）**：函数内直接对变量赋值，默认在 Local 空间创建同名变量，隐藏外层变量。
> - **跨层改写关键字**：
>   - **`global`**：声明改写模块级全局变量；
>   - **`nonlocal`**：声明改写外层嵌套函数（Enclosing）的局部变量，**不触及全局**。
> - **`UnboundLocalError` 陷阱**：Python 编译期若在函数内扫描到任何赋值语句（如 `x = ...`），会将 `x` 静态标记为局部变量。如果在赋值前读取它，直接抛出未绑定异常。

**标签**：`#Python` `#变量作用域` `#LEGB` `#global` `#nonlocal` `#UnboundLocalError` `#闭包`

---

## 一、命名空间与作用域四层金字塔（LEGB）

Python 解释器在**读取变量**时，严格按如下层级自内向外检索：

```mermaid
graph TD
    subgraph 作用域层级 (由近及远)
        L["1. Local (局部作用域)<br>当前函数内部的形参及局部变量"] --> E["2. Enclosing (闭包外层作用域)<br>外层嵌套函数的局部环境"]
        E --> G["3. Global (全局作用域)<br>当前模块/脚本顶层定义的变量"]
        G --> B["4. Built-in (内置作用域)<br>Python 自带的 print, len, range 等"]
    end
```

- 只能**由内向外**查找，外层作用域无法直接访问内层作用域的私有变量；
- 一旦在某一层级找到匹配名称，立即终止查找；若四层均未命中，触发 `NameError`。

---

## 二、读写权限分离与关键字穿透

| 访问意图 | 是否需要关键字 | 语法示例 | 行为特征 |
| :--- | :--- | :--- | :--- |
| **纯读取外层变量** | 否 | `print(total)` | 天然遵循 LEGB 规则向上穿透查找。 |
| **就地创建局部变量** | 否 | `x = 10` | 默认在当前 Local 作用域创建新变量，发生**同名遮蔽**。 |
| **修改全局变量** | **是 (`global`)** | `global total; total += 1` | 将变量名绑定到模块全局命名空间。 |
| **修改闭包外层变量** | **是 (`nonlocal`)** | `nonlocal count; count += 1` | 穿透至最近的外层嵌套函数局部环境，**不影响全局**。 |

### 核心对比代码
```python
x = 5

def outer():
    x = 10
    def inner():
        nonlocal x
        x = 11      # 修改的是 outer 的 x，global 的 x 依然是 5
    inner()
    print(x)        # 输出: 11

outer()
print(x)            # 输出: 5
```

---

## 三、天王级避坑指南：`UnboundLocalError`

### 1. 经典案发现场
```python
x = 10

def demo():
    print(x)  # 💥 UnboundLocalError: local variable 'x' referenced before assignment
    x = x + 1

demo()
```

### 2. 根因与机理剖析
1. **静态作用域分析**：Python 解释器在执行函数体前，先静态扫描当前代码块。
2. **赋值即占位**：一旦发现 `x = x + 1` 包含赋值号，解释器直接把 `x` 打上 **Local 局部变量** 的烙印，全局变量 `x` 在该作用域内被彻底遮蔽。
3. **未初始化引用**：执行首行 `print(x)` 时，由于局部变量 `x` 尚未完成赋值绑定，无法被读取，抛出 `UnboundLocalError`。

> [!CAUTION]
> **解决方案**：若想在函数内读取并修改外层变量，必须在首行添加 `global x`（改全局）或 `nonlocal x`（改嵌套外层）。
