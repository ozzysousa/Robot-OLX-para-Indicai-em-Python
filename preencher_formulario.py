from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configuração do WebDriver (certifique-se de ter o chromedriver.exe na mesma pasta)
driver = webdriver.Chrome(executable_path='C:\\caminho\\para\\chromedriver.exe')

# URL do formulário que você deseja preencher
url_formulario = 'https://exemplo.com/meu-formulario'

# Abre a página do formulário
driver.get(url_formulario)

# Aguarda alguns segundos para a página carregar completamente (ajuste conforme necessário)
time.sleep(5)

# Preencha o formulário com os dados coletados da OLX
nome_input = driver.find_element_by_id('nome')  # Substitua 'nome' pelo ID do campo de nome no formulário
endereco_input = driver.find_element_by_id('endereco')  # Substitua 'endereco' pelo ID do campo de endereço no formulário
telefone_input = driver.find_element_by_id('telefone')  # Substitua 'telefone' pelo ID do campo de telefone no formulário

# Substitua 'nome_coletado', 'endereco_coletado' e 'telefone_coletado' pelos valores coletados da OLX
nome_input.send_keys('nome_coletado')
endereco_input.send_keys('endereco_coletado')
telefone_input.send_keys('telefone_coletado')

# Envie o formulário
submit_button = driver.find_element_by_id('submit_button')  # Substitua 'submit_button' pelo ID do botão de envio no formulário
submit_button.click()

# Feche o navegador após o preenchimento do formulário
driver.quit()
