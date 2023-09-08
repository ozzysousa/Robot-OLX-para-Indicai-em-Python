# Robot-OLX-para-Indicai-em-Python
Robô de coleta de dados da OLX e preenchimento automático de formulários em Python. Automatiza a captura de informações de anúncios imobiliários na OLX e o preenchimento em outro site.

# Projeto de Automação da Web com Python

Este projeto é uma solução de automação da web desenvolvida em Python para coletar informações de anúncios de imóveis na OLX e preencher um formulário em outro site com esses dados.

## Funcionalidades Principais

- Coleta automática de informações de anúncios de imóveis na OLX.
- Filtro por cidade, permitindo a busca de anúncios apenas em Águas Claras, Brasília.
- Identificação de anúncios particulares.
- Preenchimento automático de um formulário em outro site com as informações coletadas.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter as seguintes dependências instaladas:

- Python 3.x
- Bibliotecas Python: [Selenium](https://pypi.org/project/selenium/), [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)

Você também precisará do driver apropriado para o seu navegador. Neste projeto, usamos o driver do Chrome.

## Configuração

1. Clone este repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   ```

2. Instale as dependências Python:

   ```bash
   pip install -r requirements.txt
   ```

3. Baixe o driver do navegador (no exemplo, usamos o ChromeDriver) e coloque-o na mesma pasta que o arquivo `code_robot.py`.

## Uso

Para executar o robô de automação, siga estas etapas:

1. Abra um terminal na pasta do projeto.

2. Execute o seguinte comando:

   ```bash
   python code_robot.py
   ```

3. O robô irá automatizar a coleta de dados da OLX e o preenchimento do formulário no outro site.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para melhorar este projeto e criar solicitações de pull.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
