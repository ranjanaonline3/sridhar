from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import re, os

i = 0
os.chdir("pictures")
for i in range(27):
    i = i+1
    html = urlopen("https://www.azquotes.com/picturequotes?p="+str(i))
    bs = BeautifulSoup(html, 'html.parser') 
    images = bs.find_all('img')
    for image in images:
        if "/image-quotes/" in image['src']:
            img_url = "https://www.azquotes.com"+image['src']
            img_name = os.path.basename(img_url)
            urlretrieve(img_url,img_name)