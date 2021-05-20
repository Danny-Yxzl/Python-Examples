import zmail

mail_content = {
    "subject": "邮件主题",
    "content_html": """
        <p>邮件正文</p>
        <p>Hello World!</p>
    """,
    "from": "Zmail发送测试 <sender@example.com>",  # 收到邮件后显示的发件人名称
    "attachments": ["D:/Desktop/附件.txt"]  # 附件，如果没有请删除字典的这一项
}

server = zmail.server("sender@example.com", "PASSWORD")  # 使用你的邮件账户名和密码登录服务器
try:
    server.send_mail(["receiver@example.com"], mail_content)  # 列表可设置多个收件人
    # server.send_mail(["receiver@example.com"], mail_content, cc=["cc@example.com"])  # 如果有抄送请用这个配置
    print("Seccess")
except:
    print("Failed")
