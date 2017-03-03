#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: send_email.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header


class SendEmail:
    def __init__(self, host, port, user, password, ssl=False):
        lInfo = user.split("@")
        self._user = user
        self._account = lInfo[0]
        self._me = self._account + "<" + self._user + ">"
        if ssl:
            server = smtplib.SMTP_SSL(host=host, port=port)
        else:
            server = smtplib.SMTP(host=host, port=port)
        server.login(self._account, password)
        self._server = server

    def sendTxtMail(self, to_list, sub, content, subtype='html'):
        msg = MIMEText(content, _subtype=subtype, _charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = self._me
        msg['To'] = ";".join(to_list)
        try:
            self._server.sendmail(self._me, to_list, msg.as_string())
            return True
        except smtplib.SMTPException as e:
            print(e)
            return False

    # 发送带附件的文件或html邮件
    def sendAttachMail(self, to_list, sub, content, subtype='html'):
        # 创建一个带附件的实例
        msg = MIMEMultipart()
        # 增加附件1
        att1 = MIMEText(open(r'D:\javawork\PyTest\src\main.py', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="main.py"'
        msg.attach(att1)

        # 增加附件2
        att2 = MIMEText(open(r'D:\javawork\PyTest\src\main.py', 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="main.txt"'
        msg.attach(att2)

        # 增加邮件内容
        msg.attach(MIMEText(content, _subtype=subtype, _charset='utf-8'))

        msg['Subject'] = sub
        msg['From'] = self._me
        msg['To'] = ";".join(to_list)

        try:
            self._server.sendmail(self._me, to_list, msg.as_string())
            return True
        except smtplib.SMTPException as e:
            print(e)
            return False
            # 发送带附件的文件或html邮件

    def sendImageMail(self, to_list, sub, content, subtype='html'):
        # 创建一个带附件的实例
        msg = MIMEMultipart()

        # 增加邮件内容
        msg.attach(MIMEText(content, _subtype=subtype, _charset='utf-8'))

        # 增加图片附件
        image = MIMEImage(open(r'D:\javawork\PyTest\src\test.jpg', 'rb').read())
        # 附件列表中显示的文件名
        image.add_header('Content-Disposition', 'attachment;filename=p.jpg')
        msg.attach(image)

        msg['Subject'] = sub
        msg['From'] = self._me
        msg['To'] = ";".join(to_list)

        try:
            self._server.sendmail(self._me, to_list, msg.as_string())
            return True
        except smtplib.SMTPException as e:
            print(e)
            return False

    # 析构函数：释放资源
    def __del__(self):
        self._server.quit()
        self._server.close()


mailto_list = ['405634654@qq.com']
mail = SendEmail(host='smtp.163.com', port=465, user='caowei0403@163.com', password='TIAN1992a', ssl=True)
if mail.sendTxtMail(mailto_list, "测试邮件", "hello world！<br><br><h1>你好，发送文本文件测试<h1>"):
    print("发送成功")
else:
    print("发送失败")
# if mail.sendAttachMail(mailto_list, "测试邮件-带两个附件", "hello world！<br><br><h1>你好，发送文本文件测试<h1>"):
#     print
#     "发送成功"
# else:
#     print
#     "发送失败"
#
# if mail.sendImageMail(mailto_list, "测试邮件-带一个图片的附件", "hello world！<br><br><h1>你好，发送文本文件测试<h1>"):
#     print
#     "发送成功"
# else:
#     print
#     "发送失败"