import re
import sys
import time as t
import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def condicao_previsao_do_tempo(cidade, estado, headless=False):
    data_hora = f"Data/hora: {str(dt.datetime.now())[0:19]}"
    print(data_hora)
    print(fill_with_times('-', len(data_hora)))
    print()
    condicao_tempo_accuweather(cidade, estado, headless)
    print()
    previsao_tempo_climatempo(cidade, estado, headless)

def fill_with_times(char: str, times: int):
    return times * char[0]

def condicao_tempo_accuweather(cidade: str, estado: str, headless=False):
    browser = start_chrome(headless)
    browser.get("https://www.duckduckgo.com")
    browser.find_element(By.XPATH, '//*[@id="search_form_input_homepage"]')\
        .send_keys(f"accuweather pt br brazil weather {cidade} {estado}", Keys.ENTER)

    url = browser.find_element(By.XPATH, '//*[@id="r1-0"]/div/h2/a[1]').get_attribute("href")
    browser.get(format_accuweather_url(url))
    t.sleep(2)
    browser.implicitly_wait(2)

    title = f"Condições meteorológicas em {capitalize_all(cidade)}/{estado.upper()}, Brasil"
    print(title)
    print(fill_with_times('-', len(title)))

    #print(browser.find_element(By.CSS_SELECTOR, 'body').text.split("\n"))
    # not all localities have the same kind of data available, so it needs to be wrapped in a try block
    try:
        data = browser.find_element(By.CSS_SELECTOR, 'div[class="current-weather-card card-module content-module non-ad"]').text.split("\n")
        condicao = data[3]
        temperatura_atual = data[2]
        sensacao_termica = f"{data[4].split(' ')[1]}C"
        sensacao = data[5]
        umidade = data[-11]
        cobertura_nuvens = data[-5]
    except:
        print("Informações indisponíveis. Tente novamente.")
        browser.quit()
        return

    browser.quit()

    print(f"               Tempo: {condicao}")
    print(f"         Temperatura: {temperatura_atual}")
    print(f"    Sensação Térmica: {sensacao_termica}")
    print(f"            Sensação: {sensacao}")
    print(f"             Umidade: {umidade}")
    print(f" Cobertura de nuvens: {cobertura_nuvens}")

def previsao_tempo_climatempo(cidade: str, estado: str, headless=False):
    browser = start_chrome(headless)
    browser.get("https://www.duckduckgo.com")
    browser.find_element(By.XPATH, '//*[@id="search_form_input_homepage"]')\
        .send_keys(f"climatempo {cidade} {estado} brasil", Keys.ENTER)
    browser.find_element(By.XPATH, '//*[@id="r1-0"]/div/h2/a[1]').click()

    t.sleep(2)
    browser.implicitly_wait(2)

    data, option = [], 0

    title = f"Previsão do tempo em {capitalize_all(cidade)}/{estado.upper()}, Brasil"
    print(title)
    print(fill_with_times('-', len(title)))

    try:
        data = browser.find_element(By.CSS_SELECTOR, 'div[class="card -no-top -no-bottom"]').text.split("\n")
        option = 1
    except:
        try:
            data = browser.find_element(By.XPATH, '//*[@id="first-block-of-days"]/div[4]/section[1]')
            option = 2
            data = remove_empty_elements(data.text.split("\n"))
        except:
            print("Informações indisponíveis. Tente novamente.")
            browser.quit()
            return

    if option == 1:
        comparacao = data[0]
        previsao = data[1]
        temp_min = data[7]
        temp_max = data[8]
        precipitacao = data[10]
        umidade_min = data[14]
        umidade_max = data[15]
        nascer_por_sol = ""

        for i in range(0, len(data)):
            if data[i] == 'Sol':
                nascer_por_sol = data[i+1].replace('h', '')

        print(f"        Temp. mínima: {temp_min}C")
        print(f"        Temp. máxima: {temp_max}C")
        print(f"          Comparação: {comparacao}.")
        print(f"            Previsão: {previsao}")
        print(f"        Precipitação: {precipitacao}")
        print(f"      Umidade mínima: {umidade_min}")
        print(f"      Umidade máxima: {umidade_max}")
        if nascer_por_sol:
            print(f"   Nascer/pôr do sol: {nascer_por_sol.replace(' ', ' / ')}")

    elif option == 2:
        temp_min = data[2]
        temp_max = data[3]
        pluviosidade = data[4]
        previsao = data[5]
        umidade = ""
        lua = ""
        nascer_por_sol = ""

        for i in range(0, len(data)):
            if data[i] == 'UMIDADE DO AR':
                umidade = data[i+1]

        for i in range(0, len(data)):
            if data[i] == 'SOL':
                nascer_por_sol = data[i+1]

        for i in range(0, len(data)):
            if data[i] == 'LUA':
                lua = data[i+1]

        browser.quit()

        print(f"        Temp. mínima: {temp_min}C")
        print(f"        Temp. máxima: {temp_max}C")
        print(f"            Previsão: {previsao}")
        print(f"        Pluviosidade: {pluviosidade}")
        print(f"             Umidade: {umidade}")
        print(f"   Nascer/pôr do sol: {nascer_por_sol.replace(' - ', ' / ')}")
        print(f"                 Lua: {lua}")

def start_chrome(headless=False):
    options = webdriver.ChromeOptions()
    headless and options.add_argument('--headless')
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    options.add_argument("--incognito")
    options.add_argument("--disable-plugins-discovery");
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(options=options)

def format_accuweather_url(url: str):
    url_components = url.split("/")
    query_url = ""
    for i in range(0, len(url_components)):
        if i == 3:
            query_url += "pt"
        elif i == 7:
            query_url += "current-weather"
        else:
            query_url += url_components[i]
        if i != len(url_components) - 1:
            query_url += "/"
    return query_url

def capitalize_all(text:  str):
    exclude = ["de", "da", "do", "dos", "das"]
    words = text.split(" ")

    for w in words:
        w = w.lower()

    capitalized_words = []
    for w in words:
        if w in exclude or w[0:2] == "d'":
            capitalized_words.append(w)
        else:
            capitalized_words.append(w.capitalize())

    capitalized_text = ""
    for i in range(0, len(words)):
        capitalized_text += capitalized_words[i]
        if i != len(words)-1:
            capitalized_text += " "
    return capitalized_text

def remove_empty_elements(arr: list):
    clean_arr = []
    for i in arr:
        if i != "":
            clean_arr.append(i)
    return clean_arr

if __name__ == "__main__":
    inputs = sys.argv

    if len(inputs) < 3:
        print("ERRO: é necessário digitar cidade e estado.\
            \nExemplo:\
                \n\tpython3 previsao_do_tempo_brasil.py manaus am")
    elif len(inputs) > 4:
        print("ERRO: digite apenas cidade e estado; coloque aspas simples ou duplas\
            \nse o nome da cidade possuir mais de uma palavra ou utilize\
            \na barra invertida (\\) para cancelar um espaço em branco como\
            \nseparador de argumentos.\
            \nExemplo 1:\
                \n\tpython3 previsao_do_tempo_brasil.py \"são paulo\" sp\
            \nExemplo 2:\
                \n\tpython3 previsao_do_tempo_brasil.py rio\ de\ janeiro rj")
    else:
        cidade = inputs[1].strip()
        estado = inputs[2].strip()

    if len(inputs) == 4:
        headless = inputs[3].strip()
        if re.match('(?i)true|false', headless):
            if re.match('(?i)true', headless):
                condicao_previsao_do_tempo(cidade, estado, True)
            if re.match('(?i)false', headless):
                condicao_previsao_do_tempo(cidade, estado, False)
    else:
        condicao_previsao_do_tempo(cidade, estado)
