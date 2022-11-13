import requests
from bs4 import BeautifulSoup

base = 'https://apod.nasa.gov/apod/'
url = 'https://apod.nasa.gov/apod/astropix.html'
get_request = requests.get(url)
soup = BeautifulSoup(get_request.content, 'html.parser')

pic_of_the_day = base + soup.find('img').parent['href']
caption = soup.findAll('center')[1].find('b').text.strip()

readme_data = open('README.md', 'r').readlines()

original_url = readme_data[12][readme_data[12].find('(') + 1 : readme_data[12].find(')')]
original_caption = readme_data[15][readme_data[15].find('<b>') + 3 : readme_data[15].find('</b>')]

readme_data[15] = readme_data[15].replace(original_caption, caption)
readme_data[12] = readme_data[12].replace(original_url, pic_of_the_day)

open('README.md', 'w').writelines(readme_data)