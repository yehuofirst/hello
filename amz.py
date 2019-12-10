# import urllib2
import lxml.html
import requests
from lxml import etree
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def amazon_price(url, user_agent):

    kv = {'user-agent': user_agent}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    tree = lxml.html.fromstring(r.text.encode("utf-8"))
    #发件人
    sender = 'keezyao@126.com'
    #客户端授权码：需要在注册邮箱后，登录进入->设置->常规设置->客户端授权码 里面进行设置
    authCode = 'aa111111'
    email = '117712779@qq.com'

    # price = tree.cssselect("span#priceblock_ourprice")[0]
    prices = tree.cssselect("[class='a-size-large a-color-price olpOfferPrice a-text-bold']")[0]
    price_list = tree.find_class('a-row a-spacing-mini olpOffer')
    out_list = []
    seller_list = []
    for pp in price_list:
        seller = pp.xpath('./div/h3/span/a/text()')
        price = str(pp.xpath('./div/span/text()')[0])
        price0 = price.replace('$' ,'')
        price1 = price0.strip()     
        out_list.append(price1)
        seller_list.append(seller[0])

        if seller[0] == 'Hotrate':
            Hotrate_price = str(pp.xpath('./div/span/text()')[0])
            Hotrate_price0 = Hotrate_price.replace('$' ,'')
            # Hotrate_price1 = float(Hotrate_price0.strip())
            Hotrate_seller1 = seller[0]
            Hotrate_price1 = price1
            print(Hotrate_seller1, Hotrate_price1)
            # print(seller_list)
            


    min_price = min(out_list)

    if min_price < Hotrate_price1:
        message = str(seller_list) + 'min_price:'+str(min_price)
        messageObj = MIMEText(message, "plain", "utf-8")
        #设置主题
        messageObj['Subject'] = Header("跟棕", "utf-8")
        #设置发件人
        messageObj['From'] = sender
        #设置收件人
        messageObj['To'] = email
        try:
            #建立客户端
            smtpObj = smtplib.SMTP()
            #连接
            #此处是网易126邮箱，使用163邮箱则为smtp.163.com
            smtpObj.connect('smtp.126.com')
            #认证
            smtpObj.login(sender, authCode)
            #发送邮件
            smtpObj.sendmail(sender, [email], messageObj.as_string())
            #断开连接
            smtpObj.close()
            print("send mail sucess")
            return True
        except smtplib.SMTPException as ex:
            print("send email failed")
            print(ex)
            return False




if __name__=="__main__": 
    
    urls = ["https://www.amazon.com/gp/offer-listing/B07PVW1KZY/ref=dp_olp_new_mbc?ie=UTF8&condition=new", "https://www.amazon.com/gp/offer-listing/B07PGK45BH/ref=dp_olp_new_mbc?ie=UTF8&condition=new"]
    user_agent = 'Mozilla/5.0'
    for url in urls:
        amazon_price(url, user_agent)


