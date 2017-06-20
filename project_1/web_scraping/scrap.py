from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "hhtp://www.chicagoreader.com"

def get_category_links(section_url):
    html=urlopen(section_url).read()
    soup=BeautifulSoup(html,"lxml")
    boccat=soup.find("dl","boccat")
    category_links=[BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
    return category_links

