# 正则表达式的使用
# 实际使用，邮箱的判断


# 爬取电话
"""
import re
str1 = '我的电话是10010，你的电话是：10086'
list1 = re.findall(r'\d', str1)         # 找出所有符合条件的字符并放入列表中,这里如果不加上r转义会提示，
print(list1)    # 结果为['1', '0', '0', '1', '0', '1', '0', '0', '8', '6']

list2 = re.findall(r'\d+', str1)         # 找出所有符合条件的字符并放入列表中,这里如果不加上r转义会提示，
print(list2)    # 结果为['10010', '10086']
"""

# 爬取图片
import requests
import re
with open('./wallhaven.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    # < img
    # src = "https://th.wallhaven.cc/small/zy/zyxvqy.jpg"
    # width = "300px"
    # alt = "" >
    links = re.findall(r'<img src="https://.+?\.jpg" width="\w+px" alt=""', content)       # 这里用.*?，懒惰模式，如果是贪婪模式就会只有一个元素
    for link in links:
        print(link)

