# ESSE CODIGO FAZ A BUSCAS DOS SUPERMERCADOS DE BOTUCATU COM BASE EM UMA PESQUISA NO
# GOOGLE MAPS

import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?hl=pt-BR&tbs=lf:1,lf_ui:10&tbm=lcl&sxsrf=APwXEdehx2XVacLC2Jj-TaYuGOyeDedoKA:1686024587369&q=supermercados+em+botucatu&rflfq=1&num=10&sa=X&ved=2ahUKEwjgifOE463_AhUcr5UCHVGACQIQjGp6BAgeEAE&biw=1920&bih=929&dpr=1#rlfi=hd:;si:;mv:[[-22.8467776,-48.423397099999995],[-22.903525,-48.4760821]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:10'

headers = {
   'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
#ultima_pagina = soup.find('span', class_='SJajHc NVbCr').get_text().strip()

for i in range(1,120):
    url_pag = f'https://www.google.com/search?hl=pt-BR&tbs=lf:1,lf_ui:10&tbm=lcl&sxsrf=APwXEdehx2XVacLC2Jj-TaYuGOyeDedoKA:1686024587369&q=supermercados+em+botucatu&rflfq=1&num=10&sa=X&ved=2ahUKEwjgifOE463_AhUcr5UCHVGACQIQjGp6BAgeEAE&biw=1920&bih=929&dpr=1#rlfi=hd:;si:;mv:[[-22.8439993,-48.4212785],[-22.9345017,-48.504976]];start:{i}'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    lista_mercados = soup.find_all('div', class_='rllt__details')
    
    with open ('lista_mercados.csv', 'a', newline = '', encoding= 'UTF-8') as f:
        for mercado in lista_mercados:
            nome_mercado = mercado.find('span',class_='OSrXXb').get_text().strip()
            
            endereco = mercado.find_all('div', text=lambda texto: texto and (texto.startswith('Av') or texto.startswith('Avenida') or texto.startswith('Rua') or texto.startswith('R.')))
            endereco_text = str(endereco)
            endereco_text = endereco_text[6:]
            endereco_text = endereco_text[:-7]

            linha = nome_mercado + ';' + endereco_text + '\n'

            print(linha)
            f.write(linha)
    print(url_pag)
