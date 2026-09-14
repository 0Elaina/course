# blog-demo 项目上下文

## 项目简介
基于前后端分离架构的现代化个人博客系统 Demo。涵盖游客只读浏览/检索/评论，以及单博主管理员登录鉴权后的文章全生命周期管理与分类标签维护。

## 技术栈
- **前端**：Vue 3 (Composition API / <script setup>) + TypeScript + Vite + Pinia + Vue Router + Naive UI + Axios + Markdown (md-editor-v3)
- **后端**：Spring Boot + MyBatis-Plus + H2 嵌入式数据库
- **鉴权方案**：轻量 JWT + 自定义 HandlerInterceptor + BCrypt 密码加密
- **工程组织**：单工作区 Monorepo（`backend/` + `frontend/`）
- **版本控制**：保持在课程父级 Git 仓库管理，子目录配专属 `.gitignore` 过滤构建与数据库文件
- **通信/跨域**：Vite 本地反向代理 (server.proxy: /api -> http://localhost:8080) + 后端 CORS 配置双重保障
- **协议契约**：标准 RESTful + 统一响应包装 Result<T> (code, message, data)

## 架构与权限设计
- **角色模型**：单博主/管理员模式
  - 游客权限：文章列表分页、分类/标签检索筛选、文章 Markdown 详情阅读、发表评论、时间线归档浏览
  - 管理员权限：账号密码登录、JWT 签发与续期、文章发布/修改/删除、分类与标签管理、评论审核与删除
- **鉴权闭环**：
  - 登录成功返回 JWT 令牌
  - 前端 Pinia useUserStore 响应式维护 Token，并在 Axios 请求拦截器中自动附加 Authorization: Bearer <token>
  - 后端自定义 JwtInterceptor 拦截器校验 Token 有效性，注入上下文
  - 前端 Axios 响应拦截器针对 HTTP 401 状态统一拦截，清理 Token 并重定向至登录页

## 数据持久化方案
- **H2 存储模式**：本地文件持久化 (jdbc:h2:file:./data/blogdb;AUTO_SERVER=TRUE;MODE=MySQL)
- **初始化**：通过 schema.sql 自动创建表结构（User, Article, Category, Tag, Article_Tag, Comment），并在初次启动时初始化默认管理员账号与种子文章
- **可视化调试**：开启 /h2-console 路径直连可视化

## 核心业务与实体范围
1. **文章模块 (Article)**: Markdown 格式源码、正文渲染、标题/摘要/分类ID/发布状态/浏览量/创建时间
2. **分类模块 (Category)**: 文章与分类一对多 (1:N)
3. **标签模块 (Tag)**: 文章与标签多对多 (M:N)
4. **评论模块 (Comment)**: 访客免登录评论 (昵称 + 内容 + 文章ID)，一对多挂载 (1:N)
5. **归档模块 (Archive)**: 按发布时间（年/月）聚合的时间线

## 当前进度
- 前期基础架构设计与 Git 规则已确认。
- 第一阶段目标确立：**分类模块 (Category) 极简端到端垂直切片**。
- 表结构与业务逻辑重构决策完成：
  - 彻底移除 `sort_order`；
  - 默认排序规则确立为自然时间序（`id ASC` / `created_at ASC`）；
  - 新增分类入参精简为仅包含 `name` 字段。

## 当前改动同步清单
- `db/schema.sql`：移除建表语句中的 `sort_order` 及初始插入数据中的权重列。
- `Category.java` 实体类：移除 `sortOrder` 字段。
- `CategoryServiceImpl.java`：查询排序精简为 `.orderByAsc(Category::getId)`。
- `CategoryCreateRequest.java`：移除 `sortOrder`，并修正 String 长度注解为 `@Size(max = 50)`。
