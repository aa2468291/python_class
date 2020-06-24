import requests
import re
import pprint

url = 'https://dct.ntcu.edu.tw/intro.php?j=2#intro02'
html = requests.get(url)
html.encoding = 'utf-8'
html_text = html.text

email = re.findall(r'>([a-zA-Z0-9_]+@[a-zA-Z0-9_\.]+)<', html_text)

pprint.pprint(email)
