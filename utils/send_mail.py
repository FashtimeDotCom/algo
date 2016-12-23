# coding:utf-8

import os
import email
import smtplib
import traceback

from email.utils import formatdate
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class AlarmEmail(object):

    def __init__(self, host, user, passwd, to_list):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.to_list = to_list
        self.Me = "<" + self.user + ">"

    def send_mail(self, subject, content, attch=None):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.Me
        msg['To'] = ";".join(self.to_list)
        msg['date'] = formatdate(localtime=True)
        msg_context = MIMEText(content, _charset='utf-8', _subtype='html')
        msg_context["Accept-Language"] = "zh-CN"
        msg_context["Accept-Charset"] = "ISO-8859-1,utf-8"
        msg.attach(msg_context)
        if attch is not None and os.path.isfile(attch):
            msg_attch = email.MIMEBase.MIMEBase('application', 'octet-stream')
            with open(attch, 'rb') as fid:
                msg_attch.set_payload(fid.read())
            email.Encoders.encode_base64(msg_attch)
            msg_attch.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.split(attch)[-1])
            msg.attach(msg_attch)
        try:
            server = smtplib.SMTP()
            server.connect(self.host)
            server.login(self.user, self.passwd)
            server.sendmail(self.Me, self.to_list, msg.as_string())
            server.close()
        except Exception as e:
            traceback.print_exc()
