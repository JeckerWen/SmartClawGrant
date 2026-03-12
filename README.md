# Project Proposal Writer

通用课题申报书撰写助手 - An AI-powered tool for writing research project proposals.

## 概述

本技能提供完整的课题申报书撰写工作流，适用于各类课题申报：

- 国家自然科学基金
- 国家社会科学基金
- 省市级课题
- 科技计划项目
- 其他科研课题申报

支持学科领域：医学、心理学、计算机、社科、经管、工程技术等。

## 功能特性

### 四大工作流阶段

| 阶段 | 描述 | 交互方式 |
|------|------|----------|
| 1. 课题申报网址获取 | 获取申报系统入口和指南 | 交互输入 |
| 2. 研究现状调研 | 自动完成国内外研究调研，生成调研报告和选题建议 | 自动 → 邮箱 |
| 3. 申报书内容确认 | 确认选题和填写要求 | 交互输入 |
| 4. 申报书撰写 | 自动撰写完整申报书并发送 | 自动 → 邮箱 |

### 核心功能

- 📚 国内外研究现状自动调研
- 💡 智能选题建议生成（10个左右）
- 📝 完整申报书撰写
- 📧 邮件自动发送
- 🔧 多学科领域适配

## 项目结构

```
project-proposal-writer/
├── SKILL.md                    # 技能核心定义文件
├── README.md                   # 使用说明（本文件）
├── LICENSE                     # MIT 许可证
├── references/                 # 参考资料目录
│   └── proposal_template.md   # 申报书模板参考
└── scripts/                    # 脚本目录
    └── send_email.py          # 邮件发送脚本（需配置SMTP）
```

## 快速开始

### 前置要求

- Python 3.8+
- 网络访问能力（用于调研和发送邮件）

### 安装

1. 克隆仓库：
```bash
git clone https://github.com/your-repo/project-proposal-writer.git
cd project-proposal-writer
```

2. 配置邮件服务（可选）：
```bash
# 复制配置示例文件
cp scripts/config_example.py scripts/config.py

# 编辑 config.py，填入您的 SMTP 配置
```

### 使用方式

#### 方式一：作为 OpenClaw 技能使用

将本技能目录复制到 OpenClaw 技能目录：
```bash
cp -r project-proposal-writer ~/.openclaw/workspace/skills/
```

#### 方式二：独立使用邮件发送功能

```bash
cd scripts
python3 send_email.py --to recipient@example.com \
  --subject "Subject" \
  --body "Email body" \
  --attachment /path/to/file.pdf
```

## 配置说明

### 邮件配置（config.py）

```python
# SMTP 配置
SMTP_SERVER = "smtp.example.com"    # SMTP 服务器
SMTP_PORT = 587                      # SMTP 端口
SENDER_EMAIL = "your@email.com"     # 发件人邮箱
SMTP_PASSWORD = "your_password"       # 授权码/密码
```

**推荐使用环境变量：**
```python
import os

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
```

## 申报书结构参考

本技能生成的申报书包含以下标准结构：

### 课题设计论证

1. **选题**
   - 国内外研究现状述评
   - 选题的意义

2. **内容**
   - 基本思路（视角、方法、途径、目的）
   - 主要观点

3. **价值**
   - 创新之处
   - 理论意义
   - 应用价值

4. **前期成果**
   - 近年来前期相关成果
   - 主要参考文献

### 完成条件与保证

- 负责人和主要成员曾完成的课题
- 科研成果社会评价
- 时间保证、资料设备及科研条件

## 学科领域适配

| 学科领域 | 侧重点 |
|---------|--------|
| 医学/生物 | 临床研究、基础研究、转化医学 |
| 计算机/AI | 算法创新、系统应用、产业落地 |
| 社科/经管 | 政策建议、实证研究、案例分析 |
| 工程技术 | 技术突破、工程应用、标准制定 |
| 心理学 | 心理健康、认知行为、危机预警 |

## 常见问题

### Q: 如何修改调研报告的格式？
A: 可以在 `SKILL.md` 中修改报告模板部分。

### Q: 调研功能需要网络吗？
A: 是的，需要网络访问才能进行文献调研和信息检索。

### Q: 支持其他邮件服务商吗？
A: 支持任何 SMTP 邮件服务，只需在配置中修改 SMTP 服务器地址。

### Q: 可以自定义申报书章节吗？
A: 可以，阶段三交互时会询问具体的填写要求。

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 许可证

本项目采用 MIT License - 详见 [LICENSE](LICENSE) 文件

## 致谢

- OpenClaw 框架
- 各学科领域的研究者和实践者
