#!/usr/bin/env python3
"""
邮件发送脚本
用于将生成的调研报告或申报书发送到指定邮箱

使用方式:
    python3 send_email.py --to recipient@example.com --subject "Subject" --body "Body" [--attachment /path/to/file]

环境变量（推荐）:
    SMTP_SERVER  - SMTP 服务器地址
    SMTP_PORT    - SMTP 端口
    SENDER_EMAIL - 发件人邮箱
    SMTP_PASSWORD - 授权码/密码
"""

import os
import sys
import argparse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# 尝试导入配置（如果存在）
try:
    from config import (
        SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SMTP_PASSWORD,
        REPORT_EMAIL_SUBJECT_TEMPLATE, PROPOSAL_EMAIL_SUBJECT_TEMPLATE
    )
except ImportError:
    # 使用环境变量或默认值
    SMTP_SERVER = os.getenv("SMTP_SERVER", "")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    SENDER_EMAIL = os.getenv("SENDER_EMAIL", "")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
    REPORT_EMAIL_SUBJECT_TEMPLATE = "【调研报告】{topic}领域研究现状调研"
    PROPOSAL_EMAIL_SUBJECT_TEMPLATE = "【课题申报书】{title}"


def send_email(to_email, subject, body, attachment_path=None):
    """
    发送邮件
    
    Args:
        to_email: 收件人邮箱
        subject: 邮件主题
        body: 邮件正文
        attachment_path: 附件路径（可选）
    
    Returns:
        bool: 发送是否成功
    """
    # 验证配置
    if not SMTP_SERVER or not SENDER_EMAIL or not SMTP_PASSWORD:
        print("错误: 请配置 SMTP 服务器信息")
        print("可以通过设置环境变量或创建 config.py 文件进行配置")
        return False
    
    # 创建邮件
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # 添加正文
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
    # 添加附件
    if attachment_path:
        try:
            with open(attachment_path, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
            encoders.encode_base64(part)
            filename = os.path.basename(attachment_path)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {filename}'
            )
            msg.attach(part)
        except Exception as e:
            print(f"警告: 无法添加附件 {attachment_path}: {e}")
    
    # 发送邮件
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"错误: 邮件发送失败: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='发送邮件工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
    python3 send_email.py --to user@example.com --subject "测试" --body "内容"
    python3 send_email.py --to user@example.com --subject "报告" --body "请查收" --attachment report.pdf

环境变量配置:
    export SMTP_SERVER="smtp.example.com"
    export SMTP_PORT="587"
    export SENDER_EMAIL="your@email.com"
    export SMTP_PASSWORD="your_password"
        """
    )
    
    parser.add_argument('--to', '-t', required=True, help='收件人邮箱')
    parser.add_argument('--subject', '-s', required=True, help='邮件主题')
    parser.add_argument('--body', '-b', required=True, help='邮件正文')
    parser.add_argument('--attachment', '-a', help='附件路径（可选）')
    
    args = parser.parse_args()
    
    # 发送邮件
    success = send_email(args.to, args.subject, args.body, args.attachment)
    
    if success:
        print(f"邮件已成功发送到: {args.to}")
        sys.exit(0)
    else:
        print("邮件发送失败")
        sys.exit(1)


if __name__ == '__main__':
    main()
