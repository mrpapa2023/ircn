import requests
from bs4 import BeautifulSoup
property=[]
url = "https://irancode.ir/Search/ProductECatalogue?ID_NationalCode=4699780"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all div elements with class name 'display p-name'
    div_tozih_fa = soup.find_all('div', class_='display p-name')
    div_tozih_en = soup.find('div', id='l-name')
    ISIC_element = soup.find_all('a', href=lambda href: href and 'ISIC' in href)
    CPC_element = soup.find_all('a', href=lambda href: href and 'CPC' in href)
    HS_element = soup.find_all('a', href=lambda href: href and 'HS' in href)
    UNSPSC_element = soup.find_all('a', href=lambda href: href and 'UNSPSC' in href)
    UMDNS_element = soup.find_all('a', href=lambda href: href and 'UMDNS' in href)
    div_elements = soup.select('tbody tr td div')

    # Initialize the variables with None
    ISIC_code = None
    HS_code = None
    CPC_code= None
    tozih_fa = None
    tozih_en = None
    UNSPSC_code= None
    UMDNS_code= None

    for anchor in UMDNS_element:
        UMDNS_code = anchor.text.replace('\r\n', '').replace('                                                ', '').replace('UMDNS', '')

    for anchor in UNSPSC_element:
        UNSPSC_code = anchor.text.replace('\r\n', '').replace('                                                ', '').replace('UNSPSC', '')

    for anchor in CPC_element:
        CPC_code = anchor.text.replace('\r\n', '').replace('                                                ', '').replace('CPC', '')
    
    for anchor in HS_element:
            HS_code = anchor.text.replace('\r\n', '').replace('                                                ', '').replace('HS', '')

    for anchor in ISIC_element:
        ISIC_code = anchor.text.replace('\r\n', '').replace('                                                ', '').replace('ISIC', '')
    
    for div in div_elements:
        property.append(div.get_text(strip=True))

    for div in div_tozih_fa:
        tozih_fa = div.text.replace('                                    ', '').replace('\r\n', '')

    if div_tozih_en:
        tozih_en = div_tozih_en.text.replace('                                    ', '').replace('\r\n', '')

    # Check if the variables are still None and replace with "null"
    HS_code = HS_code if HS_code is not None else "null"
    UNSPSC_code = UNSPSC_code if UNSPSC_code is not None else "null"
    UMDNS_code=UMDNS_code if UMDNS_code is not None else "null"
    CPC_code = CPC_code if CPC_code is not None else "null"
    ISIC_code = ISIC_code if ISIC_code is not None else "null"
    tozih_fa = tozih_fa if tozih_fa is not None else "null"
    tozih_en = tozih_en if tozih_en is not None else "null"
    
    vahed_shomaresh= property[2]
    noe=property[5]
    karbord=property[8]
    noe_bastebandi=property[11]
    meghdar=property[14]
    name_tejari=property[17]
    marjae_arze_konande=property[-1]
    print(vahed_shomaresh)
    print(noe)
    print(karbord)
    print(noe_bastebandi)
    print(meghdar)
    print(name_tejari)
    print(marjae_arze_konande)
    print(property)



else:
    print("Failed to retrieve the content from the URL.")
