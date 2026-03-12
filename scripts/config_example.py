"""
邮件发送配置示例

复制此文件为 config.py 并填入您的配置：
cp config_example.py config.py
"""

import os

# ==================== SMTP 配置 ====================
# 方式1: 直接填写配置（不推荐，敏感信息会暴露）
# SMTP_SERVER = "smtp.qq.com"
# SMTP_PORT = 587
# SENDER_EMAIL = "your@email.com"
# SMTP_PASSWORD = "your_auth_code"

# 方式2: 从环境变量读取（推荐，更安全）
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")

# ==================== 邮件模板配置 ====================
# 调研报告邮件主题模板
REPORT_EMAIL_SUBJECT_TEMPLATE = "【调研报告】{topic}领域研究现状调研"

# 申报书邮件主题模板
PROPOSAL_EMAIL_SUBJECT_TEMPLATE = "【课题申报书】{title}"

# ==================== 其他配置 ====================
# 默认语言
DEFAULT_LANGUAGE = "zh-CN"

# 调研报告选题建议数量
DEFAULT_TOPIC_SUGGESTIONS_COUNT = 10
