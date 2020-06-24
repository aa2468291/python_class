# 威力彩號碼爬蟲
import requests
from bs4 import BeautifulSoup

article_href = []
r = requests.get("https://www.taiwanlottery.com.tw/")  # 指定要抓取的網址

soup = BeautifulSoup(r.text, "html.parser")
results = soup.select("div.contents_box02")[0]  # 指定抓取威力彩區
green = results.find_all('div', {'class': 'ball_green'})
red = results.find_all('div', {'class': 'ball_red'})
normal_num = []
special_num = []

for i in green:
    normal_num.append(i.string.strip())

for j in red:
    special_num.append(j.string.strip())

print("威力彩號碼第一區" + str(normal_num[0:6]))
print("威力彩號碼第二區" + str(special_num))
