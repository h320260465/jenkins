import webbrowser
import time
import os,sys
import zipfile


def send_mail(username, passwd, recv, title, content, mail_host='smtp.163.com', port=25):
    try:
        msg = MIMEText(content) # 邮件内容
        print(msg)
        msg['Subject'] = title # 邮件主题
        msg['From'] = username # 发送者账号
        msg['To'] = recv # 接收者账号列表
        smtp = smtplib.SMTP(mail_host, port=port) # 连接邮箱，传入邮箱地址，和端口号，smtp的端口号是25
        smtp.login(username, passwd) # 登录发送者的邮箱账号，密码
        # 参数分别是 发送者，接收者，第三个是把上面的发送邮件的 内容变成字符串
        smtp.sendmail(username, recv, msg.as_string())
        smtp.quit() # 发送完毕后退出smtp
        print('邮件发送成功')
    except:
        print('邮件发送失败')


        
def JY():        
    path = r'D:\PDC\2018云南大学中国海外投资企业调查项目'+'\\'+'qData'+time.strftime("%Y%m%d")+'.zip'  #压缩包位置
    path2 = r'D:\FTP\技术部\部门共享\数据提取\[To 质控]\2018云南大学中国海外投资企业调查项目'                    #解压位置
    f = zipfile.ZipFile(path,'r')
    for file in f.namelist():
        f.extract(file,path2)
    time.sleep(6)
 


email_user = 'h948411318@163.com' # 发送者账号
email_pwd = 'h320260465' # 发送者密码,授权码
maillist = 'yangxiaolong@chfs.cn'   
title = '22018云南大学中国海外投资企业调查项目'
JY()
content = title+',数据解压完成'+'\n'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
send_mail(email_user, email_pwd, maillist, title, content)
