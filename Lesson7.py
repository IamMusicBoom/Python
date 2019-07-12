# http://kaijiang.500.com/shtml/dlt/19079.shtml
# 彩票开奖
from collections import Counter
from time import sleep

import requests
from bs4 import BeautifulSoup

host = "http://kaijiang.500.com/shtml"
# kind = input("请输入您想查询的彩票种类")
# date = input("请输入您要查询的期数")
kind = "dlt"
date = 19079
end = ".shtml"

proxy_dict = {
    "http": "http://10.14.11.97:3122/",
    "https": "https://10.14.11.97:3122/"
}

balls = []
allBalls = []
file_handle = open('1.txt', mode='w')
while date >= 7001:
    if date in range(18155, 19001):
        date = date - 1
        continue
    elif date in range(17154, 18001):
        date = date - 1
        continue
    elif date in range(16155, 17001):
        date = date - 1
        continue
    elif date in range(15154, 16001):
        date = date - 1
        continue
    elif date in range(14155, 15001):
        date = date - 1
        continue
    elif date in range(13154, 14001):
        date = date - 1
        continue
    elif date in range(12155, 13001):
        date = date - 1
        continue
    elif date in range(11154, 12001):
        date = date - 1
        continue
    elif date in range(10155, 11001):
        date = date - 1
        continue
    elif date in range(9154, 10001):
        date = date - 1
        continue
    elif date in range(8155, 9001):
        date = date - 1
        continue
    elif date in range(7154, 8001):
        date = date - 1
        continue
    elif date <= 10000:
        url = host + "/" + kind + "/" + "0" + str(date) + end
    else:
        url = host + "/" + kind + "/" + str(date) + end
    print(url)
    allHtml = requests.get(url=url, proxies=proxy_dict)
    allHtml.encoding = "utf-8"
    allBf = BeautifulSoup(allHtml.text, "html.parser")
    redBalls = allBf.find_all("li", class_="ball_red")
    for red in redBalls:
        balls.append(red.string + " ")
    blueBalls = allBf.find_all("li", class_="ball_blue")
    for blue in blueBalls:
        balls.append(blue.string + " ")
    date = date - 1
    str_ball = "".join(balls)
    formatBall = str_ball[0:len(str_ball) - 1]
    file_handle.write(formatBall)
    file_handle.write("\n")
    print(balls)
    balls.clear()
    allBalls.append(formatBall)
    print(allBalls)
    sleep(1)

b = dict(Counter(allBalls))
dup = [key for key, value in b.items() if value > 1]  # 只展示重复元素
file_handle2 = open('2.txt', mode='w')

file_handle3 = open('3.txt', mode='w')
for i in dup:
    file_handle2.write(i);
    file_handle2.write("\n")

dic = {key: value for key, value in b.items() if value > 1}  # 展现重复元素和重复次数
for i in dic.keys():
    file_handle3.write(i + " : " + str(dic.get(i)))
    file_handle3.write("\n")
