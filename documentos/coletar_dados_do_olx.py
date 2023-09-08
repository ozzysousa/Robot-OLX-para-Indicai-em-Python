import requests
from bs4 import BeautifulSoup

# URL do OLX com anúncios de casas para alugar em Águas Claras, Brasília
olx_url = 'https://www.olx.com.br/distrito-federal-e-regiao/aguas-claras?q=&sf=1'

# Função para extrair informações dos anúncios
def extract_ads_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    ads = []
    for ad in soup.find_all('li', class_='sc-1fcmfeb-2'):
        title = ad.find('h2', class_='sc-1mbetcw-0').text
        price = ad.find('span', class_='sc-ifAKCX eoKYee').text
        description = ad.find('p', class_='sc-1mbetcw-4').text
        is_private = 'particular' in description.lower()  # Filtra anúncios particulares
        
        if is_private:
            ads.append({'title': title, 'price': price, 'description': description})
    
    return ads

# Exemplo de uso:
ads_info = extract_ads_info(olx_url)
for ad_info in ads_info:
    print(ad_info)
