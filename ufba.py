from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import schedule
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

lista_trs = []
anterior = 0
atual = 0
ultMsg = ''
loop = 0
def web_scraping():
    lista_trs.clear()
    url = "https://www.ingresso.ufba.br/"
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page, "html.parser")

    title = soup.title.text
    table = soup.find_all('table', {'class': 'table-responsive'})
    trs = table[0].find_all("tr")
    start = 0

    for i in range(0, len(trs)):
        span = trs[i].find_all("span")
        if span: 
            if span[0].text == "Convocações e Publicações:": 
                start = i
        
    for i in range (start, len(trs)):
        span = trs[i].find_all("span")
        if span:
            lista_trs.append(span[0].text.strip())
        else:
            break
        


schedule.every().second.do(web_scraping)

while True:
    schedule.run_pending()
    time.sleep(1)
    atual = len(lista_trs)

    if (anterior != atual):
        contatos = ["Eu", "Lili"]
        driver = webdriver.Chrome()
        driver.get("https://web.whatsapp.com")
        time.sleep(12)
        if loop:
            for contato in contatos:
                mensagem = "Nova noticia cadastrada em https://www.ingresso.ufba.br/." + ultMsg
                
                search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')
                search_box.send_keys(contato)
                time.sleep(2)
                contact = driver.find_element(By.XPATH, f'//span[contains(@title,"{contato}")]')
                contact.click()
                time.sleep(2)
                msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
                msg_box.send_keys(mensagem)
                time.sleep(2)

                button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
                button.click()
                time.sleep(2)
            anterior = atual
            print(len(lista_trs))
    loop = 1