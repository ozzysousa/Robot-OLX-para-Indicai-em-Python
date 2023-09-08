from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

# Configuração do WebDriver (certifique-se de ter o chromedriver.exe na mesma pasta)
driver = webdriver.Chrome(executable_path='C:\\caminho\\para\\chromedriver.exe')

# URL da OLX com filtros aplicados (exemplo: aluguel em Águas Claras, Brasília)
url_olx = 'https://www.olx.com.br/brasilia-df/distrito-federal/aluguel?sf=1&sd=1&filters=town_in_id_3002'

# Abre a página da OLX
driver.get(url_olx)

# Aguarda alguns segundos para a página carregar completamente (ajuste conforme necessário)
time.sleep(5)

# Realiza a coleta de dados
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Exemplo de coleta de dados (ajuste conforme as informações que você deseja coletar)
for anuncio in soup.find_all('li', class_='sc-eqIVtm cCymlV'):
    nome = anuncio.find('h2').text.strip()
    endereco = anuncio.find('span', class_='sc-dlfnbm kKkHtf').text.strip()
    telefone = anuncio.find('span', class_='sc-jhAzac hvhLNa').text.strip()

    # Aqui você pode fazer o que desejar com os dados (imprimir, salvar em arquivo, etc.)
    print(f'Nome: {nome}')
    print(f'Endereço: {endereco}')
    print(f'Telefone: {telefone}')
    print('-' * 30)

# Feche o navegador após a coleta de dados
driver.quit()
