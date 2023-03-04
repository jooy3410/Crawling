import requests as req

url = "https://news.naver.com/"

webpage = req.get(url, verify=False)
print(webpage.text)
print('test')