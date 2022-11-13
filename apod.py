import requests
from bs4 import BeautifulSoup

base = 'https://apod.nasa.gov/apod/'
url = 'https://apod.nasa.gov/apod/astropix.html'
get_request = requests.get(url)
soup = BeautifulSoup(get_request.content, 'html.parser')

pic_of_the_day = base + soup.find('img').parent['href']
caption = soup.findAll('center')[1].find('b').text.strip()

readme_data = open('README.md', 'r').readlines()

original_url = readme_data[3][readme_data[3].find('(') + 1 : readme_data[3].find(')')]
original_caption = readme_data[6][readme_data[6].find('<b>') + 3 : readme_data[6].find('</b>')]

readme_data[6] = readme_data[6].replace(original_caption, caption)
readme_data[3] = readme_data[3].replace(original_url, pic_of_the_day)

open('README.md', 'w').writelines(readme_data)