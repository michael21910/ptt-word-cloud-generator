# PTT word cloud generator
Generates a word cloud image according to first 1000 ptt article titles.
  
## Things you need to do :open_book:
* Install the library "requests"
```
pip install requests
```
* Install the library "BeautifulSoup"
```
pip install BeautifulSoup
```
* Install the library "jieba"
```
pip install jieba
```
* Install the library "wordcloud"
```
pip install wordcloud
```
* Install the library "matplotlib"
```
pip install matplotlib
```
* Install the library "numpy"
```
pip install numpy
```
* Install the library "pandas"
```
pip install pandas
```
* Install "chrome webdriver"  
Please go to [this webpage](https://chromedriver.chromium.org/) to download
  
## What will you get :icecream:
A word cloud in a fixed picture(you can go to cloud.png to see the picture), within the words after web crawling and word hyphenation using jieba.
  
## Demo :eyes:
* Demo 1  
![ptt-crawling](https://user-images.githubusercontent.com/78197510/132520861-c68efee6-b829-4081-a431-ad52cacb09b0.png)  
* Demo 2  
![ptt-crawling2](https://user-images.githubusercontent.com/78197510/132520900-a84d83e3-8002-436f-a4e5-3e480aebcc7d.png)  
  
Note that the word cloud image would change since the first 1000 ptt articles are always changing.  
Michael Hsueh 09/08/2021
