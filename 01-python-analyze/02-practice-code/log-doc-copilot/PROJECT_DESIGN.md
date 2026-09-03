# LogDoc-Copilot 系统架构与实战设计文档 (PROJECT_DESIGN)

> 本文档由 `/grill-me` 深度讨论确认生成，作为本项目（智能日志与文档分析助手）从设计到编码落地的权威蓝图。

---

## 1. 项目定位与设计原则

- **学习目标**：高密度覆盖并实践大学 Python 核心课件（变量类型、控制结构、可迭代对象与推导式、函数与装饰器、文件与异常、类与模块、正则表达式）共 8 大知识体系。
- **极简无中间件**：杜绝 Redis、MySQL、Docker、消息队列等外部服务，仅使用 Python 标准库内置的 `sqlite3` 单文件存储。
- **高效轻量**：整体代码量精简平铺（约 5~7 个核心文件），适合 1~2 天内完整编码、测试与答辩演练。
- **现代化 AI**：基于 LangGraph 状态机（StateGraph）实现预处理、意图路由、文档分析与精准问答。

---

## 2. 课程 8 大知识点深度融合对照表

| 课件章节 | 对应项目模块 / 核心实现 | 知识点落地代码与场景 |
| :--- | :--- | :--- |
| **课件 1：环境搭建与规范** | 根目录配置与工程结构 | `requirements.txt`、`.env` 配置加载、PEP 8 规范、虚拟环境管理 |
| **课件 2：变量与简单数据类型** | Pydantic Schema 与类型提示 | Python 3.10+ `Type Hints`、字符串高级切片与 `f-string` 提示词模板动态注入 |
| **课件 3：程序控制结构** | 意图识别与业务条件分支 | 文件类型白名单判断、LangGraph 条件路由分支（摘要报告 vs 问答检索） |
| **课件 4：可迭代对象与推导式** | 数据聚合与特征统计 | **字典推导式**提取日志级别统计、**集合**去重唯一 IP/用户、**列表推导式**快速清洗数据行 |
| **课件 5：函数与高阶特性** | 装饰器与高阶接口 | 自定义 API 执行耗时与审计装饰器 `@timing_decorator`、闭包、FastAPI 依赖注入（`Depends`） |
| **课件 6：文件与异常处理** | 文件流式上传与异常回滚 | `with open(...)` 文本/CSV 文件流安全读写、自定义全局异常体系 `AppException`、统一错误拦截处理器 |
| **课件 7：类与面向对象模块** | 核心服务与上下文管理器 | 面向对象手写 `DatabaseManager` 实现 `__enter__` 与 `__exit__` 魔法方法（自动开启事务与异常回滚）、服务类封装 |
| **课件 8：正则表达式** | 文本解析与敏感数据脱敏 | `re.compile` 预编译、命名捕获分组 `(?P<...>)`、`re.findall` 提取 IP/邮箱/时间戳/异常栈，`re.sub` 脱敏 |

---

## 3. 系统技术栈

- **后端 Web 框架**：FastAPI (0.110+)
- **ASGI 服务器**：Uvicorn
- **AI 编排框架**：LangChain Core + LangGraph (0.2+)
- **模型接口适配**：`langchain-openai`（适配 DeepSeek、通义千问、智谱等所有 OpenAI 兼容 API）
- **数据持久化**：Python 内置 `sqlite3`（单文件数据库：`data/app.db`）
- **前端交互**：FastAPI 原生 Swagger UI (`/docs`) + 单文件原生轻量 HTML/CSS/JS 界面 (`static/index.html`)

---

## 4. 目录树规划

```text
02-practice-code/log-doc-copilot/
├── PROJECT_DESIGN.md          # 详细架构与技术设计文档（本文档）
├── README.md                  # 项目快速启动与运行指南
├── requirements.txt           # 极简依赖列表
├── .env.example               # 环境变量配置模版
├── data/                      # 运行时自动生成的存储目录
│   ├── app.db                 # SQLite 数据库文件
│   └── uploads/               # 上传文本/日志原件暂存
├── static/
│   └── index.html             # 单文件前端（拖拽上传、结构化指标面板、流式问答卡片）
├── core/
│   ├── __init__.py
│   ├── config.py              # 读取 .env 配置类（API_KEY, BASE_URL 等）
│   ├── db_manager.py          # [第6,7章] 原生 sqlite3 + 上下文管理器封装
│   └── text_processor.py      # [第4,8章] 正则提取、脱敏清洗与字典推导式统计
├── ai/
│   ├── __init__.py
│   └── workflow.py            # [LangGraph] 状态机定义：提取 -> 路由 -> 摘要/问答
└── main.py                    # [FastAPI] 路由接口、全局异常处理、静态资源挂载
```

---

## 5. 数据库模型设计 (SQLite3)

### 5.1 数据表: `documents` (上传文档元数据与正则特征)
| 字段名 | 类型 | 说明 |
| :--- | :--- | :--- |
| `id` | INTEGER PRIMARY KEY AUTOINCREMENT | 主键 ID |
| `filename` | TEXT NOT NULL | 原始文件名 |
| `file_path` | TEXT NOT NULL | 本地暂存路径 |
| `file_size` | INTEGER NOT NULL | 文件大小 (Bytes) |
| `cleaned_content`| TEXT NOT NULL | 脱敏与清洗后的正文文本 |
| `extracted_meta` | TEXT NOT NULL | JSON 字符串：正则提取的特征（IP列表、邮箱、时间跨度、错误级别统计） |
| `created_at` | DATETIME DEFAULT CURRENT_TIMESTAMP | 上传时间 |

### 5.2 数据表: `chat_history` (问答记录与状态轨迹)
| 字段名 | 类型 | 说明 |
| :--- | :--- | :--- |
| `id` | INTEGER PRIMARY KEY AUTOINCREMENT | 主键 ID |
| `doc_id` | INTEGER | 关联的文档 ID |
| `query` | TEXT NOT NULL | 用户提问 / 分析指令 |
| `intent` | TEXT NOT NULL | 意图识别结果 (`summary` 或 `qa`) |
| `response` | TEXT NOT NULL | AI 生成的分析报告或问答回答 |
| `created_at` | DATETIME DEFAULT CURRENT_TIMESTAMP | 创建时间 |

---

## 6. LangGraph AI 状态机架构

### 6.1 State 定义
```python
from typing import TypedDict, List, Dict, Any, Optional

class AgentState(TypedDict):
    doc_id: Optional[int]
    raw_content: str
    cleaned_content: str
    extracted_features: Dict[str, Any]  # 正则提取的指标字典
    query: str                          # 用户输入的问题或分析指令
    intent: str                         # 'summary' | 'qa'
    context_chunks: List[str]           # 检索到的相关文档切片
    final_output: str                   # 最终生成的结果
```

### 6.2 流程节点与条件边
1. **Node: `preprocess_node`**
   - 提取正则特征（IP、邮箱、错误日志），完成脱敏。
2. **Node: `intent_router` (条件分支判断)**
   - 判断用户意图：
     - 若 `query` 为空或明确要求生成报告 $\rightarrow$ 进入 `summary_node`
     - 若 `query` 为具体提问 $\rightarrow$ 进入 `retrieval_qa_node`
3. **Node: `summary_node`**
   - 结合正则统计指标与核心文本，生成结构化摘要报告。
4. **Node: `retrieval_qa_node`**
   - 对文本分块匹配相关内容，组织上下文回答用户问题。
5. **Node: `persist_node`**
   - 结果格式化并自动调用 `DatabaseManager` 写入 SQLite。

---

## 7. 实施路线图 (Phase 1 ~ Phase 4)

- [ ] **Phase 1**：搭建工程骨架，编写 `requirements.txt` 与 `core/db_manager.py`（面向对象与上下文管理器）。
- [ ] **Phase 2**：编写 `core/text_processor.py`（正则表达式、字典/集合推导式与脱敏）。
- [ ] **Phase 3**：编写 `ai/workflow.py`（LangGraph 状态图与 OpenAI 兼容接口接入）。
- [ ] **Phase 4**：编写 `main.py`（FastAPI 路由与异常处理器）与 `static/index.html`（单页现代化前端），全流程端到端联调。
