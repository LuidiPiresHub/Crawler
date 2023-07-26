# Como começar o projeto Crawler

## Comandos:

python -m venv .venv ( Cria ambiente virtual )

source .venv/Scripts/activate ( Ativa ambiente virtual )

pip install selenium requests ( Baixa as dependencias )

## Para começar a usar o Selenium é necessário um Webdriver do navegador

### Driver do Chrome como exemplo:

https://chromedriver.chromium.org/downloads

Apos instalar é necessário descompactar o driver, abrir a pasta .venv/Scripts e adicionar o driver

Feito isso já podemos começar com o Selenium

# BÔNUS

## Comando para gerar o arquivo requirements.txt:

pip freeze > requirements.txt

## Comando para instalar depencias após clonar o projeto

pip install -r requirements.txt
