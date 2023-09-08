from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicialize o WebDriver do Selenium (certifique-se de ter o driver instalado)
# Exemplo para o Chrome:
driver = webdriver.Chrome(executable_path='C:\\Users\\telex\\RobotOlx\\chromedriver.exe')

# Abra a página com o formulário
driver.get('https://indicaai.quintoandar.com.br/')

# Encontre o elemento de input para o endereço e preencha-o
address_input = driver.find_element_by_id('address')  # Substitua 'address' pelo ID correto do campo
address_input.send_keys('Avenida Paulista, 300')  # Preencha com o endereço desejado

# Encontre o elemento de input para o número e preencha-o
number_input = driver.find_element_by_id('number')  # Substitua 'number' pelo ID correto do campo
number_input.send_keys('123')  # Preencha com o número desejado

# Encontre o botão de envio e clique nele
submit_button = driver.find_element_by_id('simple_referral_submit_form')  # Substitua pelo ID do botão
submit_button.click()

# Aguarde alguns segundos (opcional)
time.sleep(5)

# Feche o navegador
driver.quit()
