## 寄信


import smtplib
from email.mime.text import MIMEText

smtpobj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
x = smtpobj.ehlo()
msg = MIMEText('Great!\n It is successful! 測試測試')
msg['Subject'] = '這是一封測試信件'
msg['From'] = 'aa2468291@gmail.com'
msg['To'] = 'ADT105107@gm.ntcu.edu.tw'
smtpobj.login('ntcudct3592@gmail.com', 'axnwnkaovqndcmvt')  ## 應用程式專用密碼，只能用來寄信
smtpobj.send_message(msg)
smtpobj.quit()
