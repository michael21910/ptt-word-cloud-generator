import requests
from bs4 import BeautifulSoup
import jieba
import jieba.analyse
from selenium import webdriver
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from PIL import Image

driverpath = 'chromedriver.exe'
browser = webdriver.Chrome(executable_path = driverpath)
browser.get("https://www.ptt.cc/bbs/Gossiping/index.html")
browser.find_element_by_xpath('/html/body/div[2]/form/div[1]/button').click()
browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/a[2]').click()
url = int(str(browser.current_url).strip('https://www.ptt.cc/bbs/Gossiping/index').strip('.html'))
browser.close()
rs = requests.session()
title = []; counter = 0
for i in range(url, 0, -1):
    payload = {
    'from': 'https://www.ptt.cc/bbs/Gossiping/index' + str(i) + '.html',
    'yes': 'yes'
    }
    res = rs.post('https://www.ptt.cc/ask/over18', data = payload)
    res = rs.get('https://www.ptt.cc/bbs/Gossiping/index' + str(i) + '.html')
    soup = BeautifulSoup(res.text)
    for entry in soup.select('.r-ent'):
        if(str(entry.select('.title')[0].text).strip('\n')[0] == "\t"):
            continue
        title.append(str(entry.select('.title')[0].text).strip('\n'))
        counter += 1
        if(counter >= 1000):
            break
    if(counter >= 1000):
        break
fromHere = 0
for i in range(0, 1000):
    for j in range(len(title[i])):
        if(title[i][j] == "]" and title[i][j + 1] == " "):
            fromHere = j + 2
            break
        elif(title[i][j] == "]" and title[i][j + 1] != " "):
            fromHere = j + 1
            break
    title[i] = title[i][fromHere : len(title[i])]
    
jieba.set_dictionary('dict.txt.big')
words_str = ' '.join(title)
words = jieba.cut(words_str, cut_all = False)
words_str = [word for word in words if len(word) >= 2]
word_count = Counter(words_str)
mask = np.array(Image.open("cloud.png"))
wordcloud = WordCloud(font_path = 'msyh.ttc') 
wordcloud = WordCloud(background_color = "white", mask = mask, font_path = 'msyh.ttc')
wordcloud.generate_from_frequencies(frequencies = word_count)
plt.figure(figsize = (12, 6))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
