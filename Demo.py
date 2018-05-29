import requests
from bs4 import BeautifulSoup

# 下載 Yahoo 首頁內容
#r = requests.get('https://tw.yahoo.com/')

#Google 搜尋 URL
google_url = 'https://www.google.com.tw/search'

# 查詢參數
my_params = {'q': '李珮琪'}

# 下載 Google 搜尋結果
r = requests.get(google_url, params = my_params)

# 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 程式碼
  soup = BeautifulSoup(r.text, 'html.parser')

  # 觀察 HTML 原始碼
  # print(soup.prettify())

  # 以 CSS 的 class 抓出各類頭條新聞
  stories = soup.select('div.g > h3.r > a[href^="/url"]')
  #stories = soup.find_all('a', class_='story-title')
  for s in stories:
    # 新聞標題
    print("標題：" + s.text)
    # 新聞網址
    print("網址：" + s.get('href'))