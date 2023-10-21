import re
import sys
import time as t
import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from typing import Any, Dict, List, Union

def condicao_previsao_do_tempo(cidade:str, estado:str, headless:bool=False):
    data_hora = f"Data/hora: {str(dt.datetime.now())[0:19]}"
    print(data_hora)
    print('-' * len(data_hora))
    print()
    condicao_tempo_accuweather(cidade=cidade, estado=estado, headless=headless)
    print()
    previsao_tempo_climatempo(cidade=cidade, estado=estado, headless=headless)

def limit_empty_spaces(text: str):
    return re.sub(r"\s{2,}", " ", text, 0)

def condicao_tempo_accuweather(cidade:str, estado:str, headless:bool=False):
    browser = start_chrome(headless)
    browser.get("https://www.duckduckgo.com")
    browser.find_element(By.CSS_SELECTOR, 'input[type=text]')\
        .send_keys(f"accuweather pt br brazil weather {cidade} {estado}", Keys.ENTER)
    url = browser.find_element(By.CSS_SELECTOR, '#r1-0 h2 a').get_attribute("href")
    browser.get(format_accuweather_url(url))
    t.sleep(2)
    browser.implicitly_wait(2)
    title = f"[AccuWeather] Condições meteorológicas em {capitalize_all(cidade)}/{estado.upper()}, Brasil"
    print(title)
    print('-' * len(title))
    TempoAtual = browser.find_element(By.CSS_SELECTOR, '.current-weather-card h1').text
    tempoAtual = browser.find_element(By.CSS_SELECTOR, '.current-weather-card div.current-weather-info div.temp').text
    tempoAtualSensacao = browser.find_element(By.CSS_SELECTOR, '.current-weather-card div.phrase').text
    tempoAtualExtraRealFeelData = browser.find_element(By.CSS_SELECTOR, '.current-weather-card div.current-weather-extra').text.split('\n')
    tempoAtualExtraRealFeelTitulo = ''
    tempoAtualExtraRealFeelValor = ''
    tempoAtualExtraRealFeelTitulo = tempoAtualExtraRealFeelData[0].split(' ')[0]
    tempoAtualExtraRealFeelValor = tempoAtualExtraRealFeelData[0].split(' ')[1]
    if len(tempoAtualExtraRealFeelData) == 2:
        tempoAtualExtraRealFeelShadeTitulo = tempoAtualExtraRealFeelData[1].split(' ')[0]+tempoAtualExtraRealFeelData[1].split(' ')[1]
        tempoAtualExtraRealFeelShadeValor = tempoAtualExtraRealFeelData[1].split(' ')[2]
    print(f"{TempoAtual.rjust(20)}: {tempoAtual} ({tempoAtualSensacao})")
    print(f"{tempoAtualExtraRealFeelTitulo.rjust(20)}: {tempoAtualExtraRealFeelValor}C")
    if len(tempoAtualExtraRealFeelData) == 2:
        print(f"{tempoAtualExtraRealFeelShadeTitulo.rjust(20)}: {tempoAtualExtraRealFeelShadeValor}C")
    weather_details = browser.find_element(By.CSS_SELECTOR, '.current-weather-card .current-weather-details').text.split('\n')
    for i in range(len(weather_details)):
        if i % 2 == 0:
            print(f'{weather_details[i].rjust(20)}: {weather_details[i+1].replace("° C", "°C")}')
    browser.quit()

def previsao_tempo_climatempo(cidade:str, estado:str, headless:bool=False):
    browser = start_chrome(headless)
    browser.get("https://www.duckduckgo.com")
    browser.find_element(By.CSS_SELECTOR, "input[type=text]")\
        .send_keys(f"climatempo {cidade} {estado} brasil", Keys.ENTER)
    browser.find_element(By.CSS_SELECTOR, "#r1-0 h2 a").click()

    t.sleep(2)
    browser.implicitly_wait(2)

    data, option = [], 0

    title = f"[ClimaTempo] Previsão do tempo em {capitalize_all(cidade)}/{estado.upper()}, Brasil"
    print(title)
    print('-' * len(title))

    try:
        data = browser.find_element(By.CSS_SELECTOR, 'div[class="card -no-top -no-bottom"]').text.split("\n")
        option = 1
    except:
        try:
            data = browser.find_element(By.CSS_SELECTOR, "#first-block-of-days section")
            option = 2
            data = remove_empty_elements(data.text.split("\n"))
        except:
            print("Informações indisponíveis. Tente novamente.")
            browser.quit()
            return

    if option == 1:
        comparacao = data[0]
        previsao = limit_empty_spaces(data[1])
        temp_min = data[7]
        temp_max = data[8]
        precipitacao = data[10]
        umidade_min = data[14]
        umidade_max = data[15]
        nascer_por_sol = ""

        for i in range(0, len(data)):
            if data[i] == 'Sol':
                nascer_por_sol = data[i+1].replace('h', '')

        print("Temp. mínima: ".rjust(22)+f"{temp_min}C")
        print("Temp. máxima: ".rjust(22)+f"{temp_max}C")
        print("Comparação: ".rjust(22)+comparacao)
        print("Previsão: ".rjust(22)+limit_empty_spaces(previsao))
        print("Precipitação: ".rjust(22)+precipitacao)
        print("Humidade mínima: ".rjust(22)+umidade_min)
        print("Humidade máxima: ".rjust(22)+umidade_max)
        if nascer_por_sol:
            print("Nascer/pôr do sol: ".rjust(22)+nascer_por_sol.replace(' ', ' / '))

    elif option == 2:
        temp_min = data[2]
        temp_max = data[3]
        pluviosidade = data[4]
        previsao = limit_empty_spaces(data[5])
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

        print("Temp. mínima: ".rjust(22)+f"{temp_min}C")
        print("Temp. máxima: ".rjust(22)+f"{temp_max}C")
        print("Previsão: ".rjust(22)+previsao)
        print("Pluviosidade: ".rjust(22)+pluviosidade)
        print("Umidade: ".rjust(22)+umidade)
        print("Nascer/pôr do sol: ".rjust(22)+nascer_por_sol.replace(' - ', ' / '))
        print("Lua: ".rjust(22)+lua)

def start_chrome(headless:bool=False):
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

def format_accuweather_url(url:str):
    return url.replace('en', 'pt').replace('weather-forecast', 'current-weather')

def capitalize_all(text:str):
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

def remove_empty_elements(arr:List[str]):
    clean_arr = []
    for i in arr:
        if i != "":
            clean_arr.append(i)
    return clean_arr

estados_brasileiros = [
    {"acronym": "AC", "name": "Acre"},
    {"acronym": "AL", "name": "Alagoas"},
    {"acronym": "AP", "name": "Amapá"},
    {"acronym": "AM", "name": "Amazonas"},
    {"acronym": "BA", "name": "Bahia"},
    {"acronym": "CE", "name": "Ceará"},
    {"acronym": "DF", "name": "Distrito Federal"},
    {"acronym": "ES", "name": "Espírito Santo"},
    {"acronym": "GO", "name": "Goiás"},
    {"acronym": "MA", "name": "Maranhão"},
    {"acronym": "MT", "name": "Mato Grosso"},
    {"acronym": "MS", "name": "Mato Grosso do Sul"},
    {"acronym": "MG", "name": "Minas Gerais"},
    {"acronym": "PA", "name": "Pará"},
    {"acronym": "PB", "name": "Paraíba"},
    {"acronym": "PR", "name": "Paraná"},
    {"acronym": "PE", "name": "Pernambuco"},
    {"acronym": "PI", "name": "Piauí"},
    {"acronym": "RJ", "name": "Rio de Janeiro"},
    {"acronym": "RN", "name": "Rio Grande do Norte"},
    {"acronym": "RS", "name": "Rio Grande do Sul"},
    {"acronym": "RO", "name": "Rondônia"},
    {"acronym": "RR", "name": "Roraima"},
    {"acronym": "SC", "name": "Santa Catarina"},
    {"acronym": "SP", "name": "São Paulo"},
    {"acronym": "SE", "name": "Sergipe"},
    {"acronym": "TO", "name": "Tocantins"}
]

def isStringAValidFixedLengthAcronym(s:str, length:int, acronym_list:List[Dict[str, str]]):
    if len(s.strip()) != length:
        return False
    return any(estado['acronym'] == s.strip().upper() for estado in estados_brasileiros)

def getBrazilianStatesAcronymsList(lista_estados:List[Dict[str, str]]):
    return [estado['acronym'] for estado in estados_brasileiros]

def conectar(lista_de_itens:List[Union[Any, str]], espacador_1:str=" e ", espacador_2:str=", "):
        assert type(espacador_1) == str \
            and  type(espacador_2) == str
        texto = ""
        for i in range(0, len(lista_de_itens)):
            texto += str(lista_de_itens[i])
            if i == len(lista_de_itens) - 1:
                return texto
            elif i == len(lista_de_itens) - 2:
                texto += espacador_1
            else:
                texto += espacador_2

def print_examples():
    print("\n - Exemplo 1:")
    print("\tpython3 previsao_do_tempo_brasil.py Brasília DF")
    print("\n - Exemplo 2:")
    print("\tpython3 previsao_do_tempo_brasil.py \"são paulo\" sp")
    print("\n - Exemplo 3:")
    print("\t", end="")
    print(r"python3 previsao_do_tempo_brasil.py rio\ de\ janeiro rj")

def main():
    inputs = sys.argv

    if len(inputs) < 3:
        print("ERRO: é necessário digitar cidade e estado.")
        print_examples()
        return
    elif len(inputs) > 4:
        print("ERRO: digite apenas cidade e estado; coloque aspas simples ou duplas")
        print("  se o nome da cidade possuir mais de uma palavra ou utilize")
        print(r"  a barra invertida (\) para cancelar um espaço em branco como")
        print("  separador de argumentos.")
        print_examples()
        return
    else:
        cidade = inputs[1]
        estado = inputs[2]

    if not isStringAValidFixedLengthAcronym(s=estado, length=2, acronym_list=estados_brasileiros):
        print("ERRO: o segundo argumento deve ser uma sigla válida de estado brasileiro (UF).")
        print("\n - Siglas válidas: {}".format(
            conectar(getBrazilianStatesAcronymsList(lista_estados=estados_brasileiros), ' ou ')))
    elif len(inputs) == 4:
        headless = inputs[3]
        if re.match('(?i)true|false', headless):
            if re.match('(?i)true', headless):
                condicao_previsao_do_tempo(cidade=cidade, estado=estado, headless=True)
            if re.match('(?i)false', headless):
                condicao_previsao_do_tempo(cidade=cidade, estado=estado, headless=False)
    else:
        condicao_previsao_do_tempo(cidade=cidade, estado=estado)

if __name__ == "__main__":
    main()
