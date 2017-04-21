#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
mailto_list=["xx@qq.com","xx@qq.com","xx@qq.com"]           #收件人(列表)
mail_host="smtp.163.com"            #使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_user="xx@163.com"                #用户名
mail_pass="xx"                             #密码,开启stmp后，默认为授权码
mail_postfix="163.com"                     #邮箱的后缀，网易就是163.com
def send_mail(to_list,sub,content):
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ",".join(to_list)                #将收件人列表以‘；’分隔
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)                            #连接服务器
        server.login(mail_user,mail_pass)               #登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception as e:
        print (str(e))
        return False
for i in range(3):                             #发送1封，range代表发送次数;#邮件主题和邮件内容
    word ='''
    Hi,

    I am thompson Cole the newly  appointed United Nations Inspection Agent in JFK Airport New York.
    During our Investigation, we discovered An abandoned shipment on your name through a Diplomat from London.
    which was transferred to our facility here in JF Kennedy Airport and when scanned it revealed an undisclosed
    sum of money in a Metal Trunk Box weighing approximately 55kg each.

    I beleived each of the boxes will contain more that $4M or above in each and the consignment is still left in
    storage house till today through a registered shipping Company, Courier Dispatch Service Limited a division of
    Tran guard LTD. The Consignment are two metal box with weight of about 55kg each (Internal dimension: W61 x H156
    x D73 (cm). Effective capacity: 680 L.)Approximately.

    The details of the consignment including your name the official document from United Nation office in London are
    tagged on the Metal Trunk box.If you want us to transact the delivery for mutual benefit, you should provide your
    Phone Number, full address, to cross check if it corresponds with the information on the official document, also
    you should provide the name of nearest Airport around you and other details to me for onward delivery.

    I want us to transact this business and share the money, since the shipper have abandoned it and ran away.I will
    pay for the Non inspection fee and arrange for the boxes to be moved out of this Airport to your address, Once we
    are through i will deploy the services of a secured shipping Company geared to provide the security it needs to
    your doorstep or i can bring it by myself to avoid any more trouble. But we will share it 70% for you and 30%
    for me. But you have to assure me of my 30%.

    Do respond to my through my direct private email : thompsoncole21@gmail.com  for more details.

    Best Regards,

    Thompson Cole
    INSPECTION OFFICE

    '''
    if send_mail(mailto_list,"Surprise!",
    word):
        print ("done!")
    else:
        print ("failed!")