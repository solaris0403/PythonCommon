#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.163.com"  # SMTP服务器
mail_user = "caowei0403@163.com"  # 用户名
mail_pass = "TIAN1992a"  # 密码

sender = 'caowei0403@163.com'  # 发件人邮箱(最好写全, 不然会失败)
receivers = ['405634654@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

content = '过期教程害死人!'
# message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
# message['From'] = "{}".format(sender)
# message['To'] = ",".join(receivers)
# message['Subject'] = title
msg = MIMEText(content, 'plain', 'utf-8')
msg['From'] = Header("菜鸟教程", 'utf-8')
msg['To'] = ";".join(receivers)
subject = 'Python SMTP Mail Test'  # 邮件主题
msg['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
    smtpObj.login(mail_user, mail_pass)  # 登录验证
    smtpObj.sendmail(sender, receivers, msg.as_string())  # 发送
    print("mail has been send successfully.")
except smtplib.SMTPException as e:
    print(e)