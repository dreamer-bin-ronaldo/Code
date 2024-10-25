import requests
from bs4 import BeautifulSoup

# 会议官网链接
url = 'https://dblp.org/db/journals/tdsc/tdsc21.html'

# 发送请求并获取网页内容
response = requests.get(url)
response.raise_for_status()  # 确保请求成功

# 解析HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有论文标题
papers = soup.find_all('li', class_='entry')

# 提取论文名称
paper_titles = []
for paper in papers:
    title = paper.find('span', class_='title').text
    paper_titles.append(title)

# 打印论文名称
for index, title in enumerate(paper_titles, start=1):
    print(f"{title}")
