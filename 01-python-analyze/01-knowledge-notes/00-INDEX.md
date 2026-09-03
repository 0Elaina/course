# Python 数据分析与编程实践 — 全局知识总索引与速查中心

> 涵盖大学 Python 基础到进阶核心知识点，并直通实战项目 `LogDoc-Copilot`。

---

## 🗺️ 全景知识地图与实战映射

| 章节编号 | 核心模块 | 核心概念与技能点 | 实战项目应用场景 (LogDoc-Copilot) |
| :--- | :--- | :--- | :--- |
| **ch01** | 环境搭建与编程规范 | 解释器、虚拟环境、pip、PEP 8 规范 | 依赖管理与项目结构划分 |
| **ch02** | 变量与简单数据类型 | 动态类型、字符串切片、格式化、Type Hints | FastAPI Schema 与类型约束 |
| **ch03** | 程序控制结构 | if-elif-else、for/while 循环、break/continue | 意图识别条件路由、文件校验 |
| **ch04** | 可迭代对象与推导式 | 列表/元组/字典/集合、推导式、生成器 | 指标聚合、去重 IP/用户、词频统计 |
| **ch05** | 函数与高阶特性 | 参数传递(*args/**kwargs)、装饰器、闭包 | API 耗时装饰器、FastAPI 依赖注入 |
| **ch06** | 文件与异常处理 | open、with、编码、try-except-finally、自定义异常 | 文本上传安全读取、全局异常拦截 |
| **ch07** | 类与面向对象编程 | class、继承、多态、魔法方法(__enter__/__exit__) | 手写 DatabaseManager 上下文管理器 |
| **ch08** | 正则表达式 | re.compile、findall、sub、命名分组、贪婪/非贪婪 | 日志解析、特征抽取与敏感脱敏 |

---

## ⚡ 30秒核心避坑与速查卡 (CheatSheet)

### 1. 字典/集合推导式 (课件 4)
```python
# 过滤并统计日志级别频次
level_counts = {level: logs.count(level) for level in ["INFO", "WARNING", "ERROR"]}
# 快速去重唯一 IP 集合
unique_ips = {item["ip"] for item in log_items if "ip" in item}
```

### 2. 自定义上下文管理器与魔法方法 (课件 6 & 7)
```python
class SafeFile:
    def __init__(self, filepath, mode="r"):
        self.filepath = filepath
        self.mode = mode
    def __enter__(self):
        self.file = open(self.filepath, self.mode, encoding="utf-8")
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # 返回 True 会吞掉异常，返回 False 会向上抛出异常
        return False
```

### 3. 正则命名分组与脱敏 (课件 8)
```python
import re
# 命名分组抽取
pattern = re.compile(r"(?P<date>\d{4}-\d{2}-\d{2})\s+\[(?P<level>[A-Z]+)\]\s+(?P<msg>.*)")
# 敏感手机号脱敏
masked = re.sub(r"(\d{3})\d{4}(\d{4})", r"\1****\2", text)
```

---

## 📂 实战项目指引
- 🚀 **项目工程目录**：[`02-practice-code/log-doc-copilot/`](../02-practice-code/log-doc-copilot/)
- 📘 **详细系统设计与架构**：[`02-practice-code/log-doc-copilot/PROJECT_DESIGN.md`](../02-practice-code/log-doc-copilot/PROJECT_DESIGN.md)
- 📊 **当前学习与推进进度**：[`PROGRESS.md`](../PROGRESS.md)
