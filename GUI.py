from PySimpleGUI import PySimpleGUI as GUI
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

#####################################INTERFACE######################################################

# Primeria janela
def Inicio():
    GUI.theme("DarkBlue")

    layout1 = [
         [GUI.Text('Bem-vindo, por favor escolha uma opção:')],
         [GUI.Button('Pesquisar Dólar',key='dolar'),GUI.Button('Pesquisar Euro',key='euro')],
         [GUI.Button('Pesquisar Bitcoin', key='bitcoin'),GUI.Button('Pesquisar por nome',key='texto')],
         [GUI.Text('', key="mensagem")]
    ]
    # Cria janela
    return GUI.Window('Buscar cotação atual', layout=layout1, finalize=True)


# Segunda Janela
def Digita():
    GUI.theme("DarkBlue")
    layout2 = [
        [GUI.Text('Digite o nome da moeda\nque deseja:')],
        [GUI.Input(key='escolha', size=(20,0))],
        [GUI.Button('Enviar', key='envia'), GUI.Button('Voltar', key='volta')]
     ]
    moeda = [layout2]
    return GUI.Window('Cotação', layout=layout2, finalize=True)

def Get():
    return values['escolha']

#####################################FUNÇÃO######################################################

chrome_options = Options()
chrome_options.add_argument("--headless")

def Dolar():
    navegador = webdriver.Chrome(options = chrome_options)
    navegador.get("https://www.google.com.br/?gws_rd=ssl")
    navegador.find_element_by_name("q").send_keys("Dolar")
    navegador.find_element_by_name("q").send_keys(Keys.ENTER)
    sleep(0.5)
    site = BeautifulSoup(navegador.page_source, 'html.parser')
    valor = site.find('div', class_="dDoNo ikb4Bb gsrt").get_text()
    GUI.popup_ok(f"Valor atual do Dólar é: {valor}!", title="Cotação mais recente",text_color="White")
    navegador.close()

def Euro():
    navegador = webdriver.Chrome(options = chrome_options)
    navegador.get("https://www.google.com/search?q=Dolar&hl=pt-BR&source=hp&ei=I3CWYujaCs2o5OUPzbmHiA8&iflsig=AJiK0e8AAAAAYpZ-MwcMYO1HAXqoieKybOm5wLrGQJO5&ved=0ahUKEwio-NKEwIr4AhVNFLkGHc3cAfEQ4dUDCAc&uact=5&oq=Dolar&gs_lcp=Cgdnd3Mtd2l6EAMyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIICAAQgAQQsQMyBQgAEIAEMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCAgAEIAEELEDOggIABCxAxCDAToKCAAQgAQQsQMQClAAWB1g7uwCaAFwAHgBgAGjBogByROSAQcwLjEuNi0zmAEAoAEB&sclient=gws-wiz")
    sleep(0.5)
    site = BeautifulSoup(navegador.page_source, 'html.parser')
    valor = site.find('div', class_="dDoNo ikb4Bb gsrt").get_text()
    GUI.popup_ok(f"Valor atual do Euro é: {valor}!", title="Cotação mais recente", text_color="White")
    navegador.close()

def Bitcoin():
    navegador = webdriver.Chrome(options = chrome_options)
    navegador.get("https://www.google.com/search?q=Bitcoin&oq=Bitcoin&aqs=edge..69i57.659j0j9&sourceid=chrome&ie=UTF-8")
    sleep(0.5)
    site = BeautifulSoup(navegador.page_source, 'html.parser')
    valor = site.find('span', class_="pclqee").get_text()
    GUI.popup_ok(f"Valor atual do Bitcoin é: {valor} BRL!", title="Cotação mais recente", text_color="White")
    # GUI.popup_error(f"Valor atual do Bitcoin é: {valor} BRL!", title="Cotação mais recente", text_color="White")
    navegador.close()

def Pesquisa():
    m = Get()
    print(m)
    navegador = webdriver.Chrome(options = chrome_options)
    navegador.get("https://www.google.com.br/?gws_rd=ssl")
    navegador.find_element_by_name("q").send_keys(m)
    navegador.find_element_by_name("q").send_keys(Keys.ENTER)
    sleep(0.5)
    try:
        site = BeautifulSoup(navegador.page_source, 'html.parser')
        valor = site.find('div', class_="dDoNo ikb4Bb gsrt").get_text()
        GUI.popup_ok(f"Valor atual do {m} é: {valor}!", title="Cotação mais recente")
        navegador.close()
    except:
        GUI.popup_ok("Moeda não encontrada, por favor verifique a escrita e tente novamente!",title="Erro de busca")

#####################################INTERFACE######################################################



# Cria janela
janela1,janela2 = Inicio(), None

# Loop inicio
while True:
    window,event,values = GUI.read_all_windows()

    # Quando janela for fechada
    if window == janela1 and event == GUI.WINDOW_CLOSED:
        break
    if window == janela2 and event == GUI.WINDOW_CLOSED:
        break

    if window == janela1 and event == 'dolar':
        window["mensagem"].update("Aguarde...")
        GUI.popup_auto_close("Aguarde..")
        Dolar()
        window["mensagem"].update(" ")

    if window == janela1 and event == 'euro':
        window["mensagem"].update("Aguarde...")
        Euro()
        window["mensagem"].update(" ")

    if window == janela1 and event == 'bitcoin':
        window["mensagem"].update("Aguarde...")
        Bitcoin()
        window["mensagem"].update(" ")

    if window == janela1 and event == 'texto':
        window["mensagem"].update("Aguarde...")
        janela2 = Digita()
        janela1.hide()
        window["mensagem"].update(" ")

    if window == janela2 and event == 'envia':
        Pesquisa()

    if window == janela2 and event == 'volta':
        janela2.hide()
        janela1.un_hide()
