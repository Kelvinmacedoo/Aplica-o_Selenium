from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--headless")

# navegador.find_element_by_id().send_keys(Keys.ENTER) > envia comando 'ENTER'

def Dolar():
    print("Pesquisando...")
    navegador = webdriver.Chrome(options = chrome_options)
    navegador.get("https://www.google.com.br/?gws_rd=ssl")
    navegador.find_element_by_name("q").send_keys("Dolar")
    navegador.find_element_by_name("q").send_keys(Keys.ENTER)
    sleep(0.5)
    site = BeautifulSoup(navegador.page_source, 'html.parser')
    valor = site.find('div', class_="dDoNo ikb4Bb gsrt").get_text()
    p = print(f"Valor atual do Dólar é: {valor}!")
    navegador.close()
    main()

def Euro():
    print("Pesquisando...")
    navegador = webdriver.Chrome(options = chrome_options)
    navegador.get("https://www.google.com/search?q=Dolar&hl=pt-BR&source=hp&ei=I3CWYujaCs2o5OUPzbmHiA8&iflsig=AJiK0e8AAAAAYpZ-MwcMYO1HAXqoieKybOm5wLrGQJO5&ved=0ahUKEwio-NKEwIr4AhVNFLkGHc3cAfEQ4dUDCAc&uact=5&oq=Dolar&gs_lcp=Cgdnd3Mtd2l6EAMyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIICAAQgAQQsQMyBQgAEIAEMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCAgAEIAEELEDOggIABCxAxCDAToKCAAQgAQQsQMQClAAWB1g7uwCaAFwAHgBgAGjBogByROSAQcwLjEuNi0zmAEAoAEB&sclient=gws-wiz")
    sleep(0.5)
    site = BeautifulSoup(navegador.page_source, 'html.parser')
    valor = site.find('div', class_="dDoNo ikb4Bb gsrt").get_text()
    print(f"Valor atual do Euro é: {valor}!")
    navegador.close()
    main()

def Bitcoin():
    print("Pesquisando...")
    navegador = webdriver.Chrome(options = chrome_options)
    navegador.get("https://www.google.com/search?q=Bitcoin&oq=Bitcoin&aqs=edge..69i57.659j0j9&sourceid=chrome&ie=UTF-8")
    sleep(0.5)
    site = BeautifulSoup(navegador.page_source, 'html.parser')
    valor = site.find('span', class_="pclqee").get_text()
    print(f"Valor atual do Bitcoin é: {valor} BRL!")
    navegador.close()
    main()

def Pesquisa():
    m = input("Por favor, digite corretamente o nome da moeda que deseja:\n")
    print("Pesquisando...")
    navegador = webdriver.Chrome(options = chrome_options)
    navegador.get("https://www.google.com.br/?gws_rd=ssl")
    navegador.find_element_by_name("q").send_keys(m)
    navegador.find_element_by_name("q").send_keys(Keys.ENTER)
    sleep(0.5)
    try:
        site = BeautifulSoup(navegador.page_source, 'html.parser')
        valor = site.find('div', class_="dDoNo ikb4Bb gsrt").get_text()
        print(f"Valor atual do {m} é: {valor}!")
        navegador.close()
        main()
    except:
        print("Moeda não encontrada, por favor verifique a escrita e tente novamente!")
        main()

def main():
    x= int(input("""\nESCOLHA UMA OPÇÃO:
    1 - PESQUISAR DOLAR
    2 - PESQUISAR EURO
    3 - PESQUISAR BITCOIN
    4 - PESQUISAR POR NOME
    5 - SAIR\n"""))
    if x == 1:
        Dolar()
    if x == 2:
        Euro()
    if x == 3:
        Bitcoin()
    if x == 4:
        Pesquisa()
    if x == 5:
        print("\nSaindo...")
        exit()
    while x != 5:
        print("Escolha uma opção correta!")
        main()

main()