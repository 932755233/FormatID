import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_host = "smtp.163.com"
mail_sender = "zhouzhongyu6565@163.com"
mail_license = "NXENVDLERONRTAPG"
mail_receivers = ["932755233@qq.com"]


def sendEmail(number):
    mm = MIMEMultipart('related')

    subject_content = """Python邮件测试"""
    mm["From"] = "zhouzhongyu6565@163.com"
    mm["To"] = "932755233@qq.com"
    mm["Subject"] = Header(subject_content, 'utf-8')

    body_content = """测试邮件"""+str(number)
    message_text = MIMEText(body_content, "plain", "utf-8")
    mm.attach(message_text)

    stp = smtplib.SMTP()
    stp.connect(mail_host, 25)
    stp.set_debuglevel(1)
    stp.login(mail_sender, mail_license)
    stp.sendmail(mail_sender, mail_receivers, mm.as_string())
    print('发送成功！')
    stp.quit()


if __name__ == '__main__':
    for i in range(20):
        sendEmail(i);