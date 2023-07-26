import requests
from bs4 import BeautifulSoup
import arabic_reshaper
from bidi.algorithm import get_display

property = []

def convert(text):
    reshaped_text = arabic_reshaper.reshape(text)
    converted = get_display(reshaped_text)
    return converted

url = "https://irancode.ir/Search/ProductECatalogue?ID_NationalCode=3731650"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
td_elements = soup.find_all('td', attrs={'colspan': '2'})
a = []
for td in td_elements:
    a.append(td.text.replace('   ', '').replace('\n\n\n', '').replace('\r\n', ''))
result = [(item.split('\n')[0].strip(), item.split('\n')[1].strip() if len(item.split('\n')) > 1 else '') for item in a]
print(result)


'''
if result[0][0] mojod bod query add 
if mojod nabod qurey add columns and add
'''



'''
for td in eCatalogueTab-1 ... eCatalogueTab-4
'''
