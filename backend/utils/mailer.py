# -*- coding: utf-8 -*-
from django.core.mail import send_mail

FROM_EMAIL = 'itimor@sexy114.com'

MAIL_FOOT = """
<br/><br/><br/>
sexy114性感查询.<br/>
<a href="http://www.sexy114.com">sexy114.com</a>
"""


def send_regist_success_mail(userinfo):
    subject = u'注册成功'
    body = u'''你好！<b>%s</b><br />
    你已经成功注册成为sexy114用户<br />
    以下是您的信息：<br />
    <ul>
        <li>用户名：%s </li>
        <li>密码:%s</li>
    </ul>''' % (userinfo['realname'], userinfo['username'], userinfo['password'])
    recipient_list = [userinfo['email']]
    send(subject, body, recipient_list)


def send(subject, body, recipient_list):
    body += MAIL_FOOT
    send_mail(subject, body, FROM_EMAIL, recipient_list, fail_silently=True)


def test(request):
    send_regist_success_mail(
        {
            'username': 'itimor',
            'password': '123123',
            'email': 'itimor@qq.com',
            'realname': 'itimor',
        }
    )
