# 身分證字號check

import re
UID = ''' 
身分證A223456789
阿花H123234789
小張的id h198723476
Happy new Year
12345 A543234567
A12398734567938
 '''


text = re.findall(r"[a-zA-Z][1-2]{1}[0-9]{8}\D", UID)

print(text)