#正規 EMAIL

import re

data = ''' 
email:sdf@ude.wer.sdf.tw
小張的電子郵箱chang@ntcu.edu.tw
Happy new Year
12345 fff@kjd.sjw.dmc.cn
 '''
text = re.findall(r'[a-zA-Z0-9_]+@[a-zA-Z0-9\._]+', data)

print(text)

