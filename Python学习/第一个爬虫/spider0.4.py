import requests
from bs4 import BeautifulSoup
import re

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
#print(soup.prettify())
for tag in soup.find_all(re.compile('b')):
    print(tag.name)