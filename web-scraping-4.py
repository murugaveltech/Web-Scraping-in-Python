import requests
from bs4 import BeautifulSoup

url = "https://thehub.io/startups/freshland" 

reg = requests.get(url)
soup = BeautifulSoup(reg.text,'html.parser')


h1 = soup.find('h2')
cas =  soup.find('div',{'class':'col-lg-7'})
last = soup.find('div',{'class':'details__info col-lg-5'})
lindin = soup.find('section',{'class':'mb-30 component-container component-container--width--medium component-container--spacing--medium component-container--border-top'})
options = soup.find('section',{'class':'component-container component-container--width--medium component-container--spacing--default'})
footer = soup.find('footer',{'class':'app-footer'})


freshland = {
    'title':h1.get_text(),
    'paragraph':cas.get_text(),
    'lest':last.get_text(),
    'linkdin_profile':lindin.get_text(),
    'options':options.get_text(),
    'about':footer.get_text()
    
}

print(freshland['about'])