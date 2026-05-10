import requests
from bs4 import BeautifulSoup

base = 'https://apod.nasa.gov/apod/'
url = 'https://apod.nasa.gov/apod/astropix.html'
get_request = requests.get(url)
soup = BeautifulSoup(get_request.content, 'html.parser')

img_element = soup.find('img')

if img_element:
  pic_of_the_day = base + img_element.parent['href']
  caption = soup.findAll('center')[1].find('b').text.strip()
  
  README_TEMPLATE = f'''
  <div align="center">
    <h1>
      NASA-APOD
    </h1>
  </div>
    
  <div align="center">
    A fun program that displays NASA's Astronomy Picture of the Day
  </div>
  
  <br>
  
  ![]({pic_of_the_day})
  
  <p align = "center">
    <b>{caption}</b>
  </p>
  '''
  
  open('README.md', 'w').writelines(README_TEMPLATE)
else:
  README_TEMPLATE = f'''
  <div align="center">
    <h1>
      NASA-APOD
    </h1>
  </div>
    
  <div align="center">
    A fun program that displays NASA's Astronomy Picture of the Day
  </div>
  
  <br>
  
  <p align = "center">
    <b>NO IMAGE FOR TODAY :)</b>
  </p>
  '''
  
  open('README.md', 'w').writelines(README_TEMPLATE)
