# 抓出 學號是ADT 且 後面五位數字的學生

import re

student = '''
周阿花 XXT11020 18分 台中市
劉阿翔 ADT10502 90分 台北市
ADT10503
ADT10209
ADT9802
XYZ10508 '''

text = re.findall(r"ADT[0-9]{5}", student)


print(text)
