from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv

# Função para calcular a distância com base em um endereço
def calcular_distancia(endereco, endereco_fixo):
    # Configurar o WebDriver do Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    # Navegar para a página do Google Maps
    driver.get("https://www.google.com/maps")

    # Localizar o campo de pesquisa e inserir o endereço
    campo_pesquisa = driver.find_element("input", {"id": "searchboxinput-1"})
    campo_pesquisa.send_keys(endereco)
    campo_pesquisa.send_keys(Keys.RETURN)

    # Esperar até que a página do Google Maps seja carregada completamente
    driver.implicitly_wait(10)

    # Localizar o elemento com as informações de distância
    elemento_distancia = driver.find_element("div", {"class": "section-directions-trip-distance"})

    # Extrair a distância do elemento
    distancia_texto = elemento_distancia.text

    # Calcular a distância em relação ao endereço fixo
    distancia_fixo = calcular_distancia_fixo(endereco_fixo, driver)

    # Fechar o WebDriver do Chrome
    driver.quit()

    return distancia_texto, distancia_fixo

# Função para calcular a distância em relação ao endereço fixo
def calcular_distancia_fixo(endereco_fixo, driver):
    # Localizar o campo de pesquisa e inserir o endereço fixo
    campo_pesquisa = driver.find_element("input", {"id": "searchboxinput-1"})
    campo_pesquisa.clear()
    campo_pesquisa.send_keys(endereco_fixo)
    campo_pesquisa.send_keys(Keys.RETURN)

    # Esperar até que a página do Google Maps seja carregada completamente
    driver.implicitly_wait(10)

    # Localizar o elemento com as informações de distância
    elemento_distancia = driver.find_element("div", {"class": "section-directions-trip-distance"})

    # Extrair a distância do elemento
    distancia_texto = elemento_distancia.text

    return distancia_texto

enderecos = []
with open('enderecos.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        enderecos.append(row[0])  # Supondo que o endereço esteja na primeira coluna (índice 0)

endereco_fixo = "Banco de Alimentos de Botucatu, Av. Paula Vieira, 704 - Vila Jahu, Botucatu - SP, 18611-020"

distancias = []
distancias_fixo = []
for endereco in enderecos:
    distancia, distancia_fixo = calcular_distancia(endereco, endereco_fixo)
    distancias.append(distancia)
    distancias_fixo.append(distancia_fixo)

# Salvar as distâncias em um arquivo CSV
with open('distancias.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Distancia', 'Distancia Fixo'])
    writer.writerows(zip(distancias, distancias_fixo))
