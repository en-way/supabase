# Enway - 权威英语真题研习与全真模考系统

> **面向全国大学英语四六级（CET-4 / CET-6）与全国硕士研究生统一招生考试英语（英语一 / 英语二）的专业级在线研习、智能刷题、全真限时模考与学习数据自愈平台。**

---

## 🌟 平台核心亮点

* **历年权威真题全量收录**：权威收录 2010 ~ 2024 年共 **60 套完整真题**（四级 22 套、六级 22 套、考研英语一 16 套），严谨还原官方试卷排版与结构。
* **分栏对照沉浸研习**：长篇仔细阅读与对应客观试题左右双栏独立滑动对照，支持自由调节文章字号与焦点同步。
* **12 万词条离线分片词典**：基于 26 字母分片静态加载（走 Cloudflare Pages 全球 CDN），支持形态还原、词根衍生自动追溯、美音/英音高可用真人发音，**0 数据库开销**。
* **双模研习与即刻落盘**：支持全真限时模考与专项智能练习；每次按键答题瞬间持久化至本地，断网/意外关闭后可无缝恢复作答断点。
* **智能错题本与单题回溯**：错题自动分类归档，支持“边看边写”双栏回溯原文、错题重练与一键导出 TXT / 打印 PDF。

---

## 🛡️ 架构特色：极致免费配额守护与红队级安全防线

Enway 创新性地采用了 **Local-First (本地优先) + Edge Mirror (边缘镜像) + Serverless Cloud (极简无服务云)** 架构，在保障极致用户体验的同时，将 Supabase 免费配额消耗降至几乎为零：

1. **客户端配额熔断守护哨兵 (Client Quota Sentinel)**：
   - 挂载全局 Fetch 拦截代理，内置 10 秒滑动窗口速率监测；
   - 10s 内 > 12 次激活自适应指数退避延迟削峰；
   - 10s 内 > 25 次触发 30 秒硬熔断断路，前端就地合成 HTTP 429，**物理网络请求数降为 0**，彻底杜绝前端死循环刷爆 Supabase 50 万次月配额；
   - 账号登出与考场交卷享有特权豁免通道。
2. **0-WebSocket 极致省流在场监测**：
   - 彻底移除 Supabase Realtime 连接，**并发长连接消耗彻底归零 (0 / 200)**，消息量消耗彻底归零；
   - 学员仅在前台活跃时每 5 分钟轻量打点；后台采用 `head: true`（0 字节 Body）统计在线人数。
3. **四级离线持久缓存网络 (Tiered Caching & SWR)**：
   - **Tier 1 (内存 0ms)**：会话内存快速命中；
   - **Tier 2 (CacheStorage 0ms)**：基于浏览器 Web 标准 `enway-static-v2` 本地磁盘持久缓存，支持 SWR 后台静默校验；
   - **Tier 3 (Cloudflare CDN 15ms)**：60 套真题单卷详情包与词库分片 100% 静态化分发，真题全文 1 年边缘强缓存，大厅索引 5 分钟自愈刷新；
   - **Tier 4 (Supabase 兜底)**：精确声明字段投影兜底。
4. **致命数据防清空熔断保险丝**：
   - 错题库在与云端题库校对时，一旦网络异常或分片出错立即激活原子级熔断终止，杜绝将学员本地错题误判删除。
5. **数据库深度安全防御**：
   - `BEFORE UPDATE` 触发器拦截非超管对 `role` 权限的篡改；
   - 篇章与题目 RLS 行级权限隔离，未过审试卷严禁被爬取；
   - 特权 RPC 函数显式声明 `SET search_path = public`，根除模式劫持风险；
   - `user-backups` 私有存储桶单路径锁定（仅限 `${auth.uid()}/backup.json`）。

---

## 📂 工程目录结构

```text
├── app/                        # Next.js 15 App Router 页面层
│   ├── page.tsx                # 真题大厅 (SWR 缓存加载、科目切换、学习概览)
│   ├── exam/page.tsx           # 全真限时模考 (最新引用防闭包、即刻草稿落盘)
│   ├── practice/page.tsx       # 智能专项练习 (双栏阅读、即时精析反馈、快捷键)
│   ├── mistakes/page.tsx       # 错题研习库 (CDN 静态解耦、一键校准最新考点)
│   ├── vocabulary/page.tsx     # 生词研习本 (本地持久化、真人发音)
│   ├── profile/page.tsx        # 个人中心 (学习档案云端备份与恢复)
│   ├── login/page.tsx          # 安全登录页 (防开放重定向)
│   ├── admin/page.tsx          # 考务后台 (在场监控、试卷审批、配额哨兵看板)
│   └── layout.tsx              # 全局布局 (挂载网络指示器、哨兵告警胶囊、AuthGuard)
├── components/                 # 核心组件库
│   ├── AuthGuard.tsx           # 全站登录态安全拦截守卫
│   ├── Navbar.tsx              # 顶栏导航与安全退出模态框
│   ├── SentinelAlertCapsule.tsx# 客户端流量防刷保护告警胶囊
│   ├── DictionaryPopover.tsx   # 划词/查词弹窗与形态还原
│   ├── PresenceProvider.tsx    # 5分钟轻量活跃在场打点 Provider
│   └── NetworkStatusIndicator.tsx # 断网容灾与离线状态指示器
├── lib/                        # 核心基础设施与通用逻辑
│   ├── quotaSentinel.ts        # 客户端配额熔断守护哨兵 (Sentinel)
│   ├── supabase.ts             # Supabase 客户端配置与 Fetch 代理注入
│   ├── examLoader.ts           # 多级缓存加载器 (Memory + CacheStorage + CDN)
│   ├── storage.ts              # 本地学习数据存取、Gzip 压缩备份与自愈引擎
│   └── dictionary.ts           # 12 万词条离线分片词典与 LRU 内存置换
├── public/                     # 静态资产与边缘配置
│   ├── data/                   # 60 套真题静态镜像与大厅索引
│   ├── dict/                   # 26 字母分片词典静态 JSON
│   ├── _headers                # Cloudflare Pages 精细化边缘缓存与安全头规则
│   └── _redirects              # Cloudflare Pages 重定向路由规则
├── supabase/migrations/        # PostgreSQL 数据库演进迁移脚本 (RLS、索引、触发器)
└── docs/                       # 架构与工程规范文档
    ├── quota_and_security_architecture.md # 全站配额防护与哨兵架构全景白皮书
    └── storage_architecture.md            # 文件与数据存储架构分析报告
```

---

## 🚀 快速启动指南

### 1. 环境准备
* Node.js $\ge$ 18.18.0 (推荐 Node.js 20+)
* npm $\ge$ 9.0.0

### 2. 安装依赖
```bash
npm install
```

### 3. 本地开发调试
```bash
npm run dev
```
本地服务将在 `http://localhost:3000` 启动。

### 4. 生产环境构建与静态导出
```bash
npm run build
```
项目已配置 `output: "export"`，构建完成后将在 `out/` 目录生成完整的静态站点，可直接部署至 Cloudflare Pages、Vercel、Netlify 或任何静态 Web 服务器。

---

## 📚 延伸架构文档

* 详细技术白皮书：[docs/quota_and_security_architecture.md](docs/quota_and_security_architecture.md)
* 存储与快照分析：[docs/storage_architecture.md](docs/storage_architecture.md)
* 交付记录与更新日志：[walkthrough.md](walkthrough.md)

---

## 📄 License
MIT License.
