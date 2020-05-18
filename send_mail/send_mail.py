#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# description: Send Mail
# author: xiaguliuxiang@foxmail.com
# date: 2020-05-18 20:00:00

import configparser
import logging
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

# 服务器地址
MAIL_HOST = ''
# 服务器端口号
MAIL_PORT = smtplib.SMTP_PORT
# 邮箱账号
MAIL_USER = ''
# 邮箱密码
MAIL_PASS = ''
# 收件人
TO_ADDRS = []


def _init():
    parser = configparser.ConfigParser()
    parser.read("conf.ini")
    # SMTP send_mail arguments
    global MAIL_HOST, MAIL_PORT, MAIL_USER, MAIL_PASS, TO_ADDRS
    MAIL_HOST = parser.get("mail", "mail_host")
    MAIL_PORT = parser.getint("mail", "mail_port")
    MAIL_USER = parser.get("mail", "mail_user")
    MAIL_PASS = parser.get("mail", "mail_pass")
    to_addrs = parser.get("mail", "to_addrs").split(',')
    for to_addr in to_addrs:
        TO_ADDRS.append(to_addr.strip())
    # Do basic configuration for the logging system.
    logging.basicConfig(format='[%(asctime)s][%(levelname)s]:[%(filename)s:%(lineno)d]:%(message)s',
                        level=logging.DEBUG)


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_mail(from_addr, to_addrs, msg):
    """This command performs an entire send_mail transaction.
    The arguments are:
        - from_addr    : The address sending this send_mail.
        - to_addrs     : A list of addresses to send this send_mail to.  A bare
                         string will be treated as a list with 1 address.
        - msg          : The message to send.
    """
    try:
        smtp_instance = smtplib.SMTP()
        # Connect to the LMTP daemon, on either a Unix or a TCP socket.
        smtp_instance.connect(MAIL_HOST, MAIL_PORT)
        # Log in on an SMTP server that requires authentication.
        smtp_instance.login(MAIL_USER, MAIL_PASS)
        # This command performs an entire send_mail transaction.
        smtp_instance.sendmail(from_addr, to_addrs, msg.as_string())
        logging.info(f'邮件发送成功:from:{from_addr},to:{to_addrs}')
    except smtplib.SMTPException as e:
        logging.error(f'邮件发送失败:{e}')


def wrapper_mail_msg(subject, text, from_addr, to_addrs):
    # Create a text/* type MIME document.
    msg = MIMEText(text, 'plain', 'utf-8')
    # The address sending this send_mail.
    msg['From'] = _format_addr(f'侠骨留香 <{from_addr}>')
    # A list of addresses to send this send_mail to. A bare string will be treated as a list with 1 address.
    msg['To'] = _format_addr(','.join(to_addrs))
    # Determine the subject for the email.
    msg['Subject'] = Header(subject, 'utf-8').encode()
    return msg


def main():
    _init()
    subject = '生命箴言'
    text = '''
    生命犹如一片绿叶，随着时间的流逝，慢慢变的枯黄，但他的叶脉还是那么清晰可见。
    -- python3 smtp test
    '''
    msg = wrapper_mail_msg(subject, text, MAIL_USER, TO_ADDRS)
    send_mail(MAIL_USER, TO_ADDRS, msg)


if __name__ == '__main__':
    main()
