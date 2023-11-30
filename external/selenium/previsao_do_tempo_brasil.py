import re
import sys
import time as t
import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from typing import Any, Dict, List, Union

def main():
    inputs:list[str] = sys.argv
    if len(inputs) < 3:
        print("ERRO: é necessário digitar cidade e estado.")
        print_examples()
        return
    elif len(inputs) > 4:
        print("ERRO: digite apenas cidade e estado; coloque aspas simples ou")
        print("  duplas  se o nome da cidade possuir mais de uma palavra ou")
        print("    utilize  a barra invertida (\) para cancelar um espaço ")
        print("      vazio como separador de argumentos.")
        print_examples()
        return

    cidade, estado = inputs[1], inputs[2]
    if not isStringAValidFixedLengthAcronym(
        s=estado, length=2, acronym_list=estados_brasileiros):
        print("ERRO: o segundo argumento deve ser uma sigla válida ", end='')
        print("de estado brasileiro (UF).")
        print("\n  Siglas válidas:\n  ---------------\n\n    {}.".format(
            join(list_brazilian_states_acronyms_list(
                lista_estados=estados_brasileiros), 'ou')))
    elif len(inputs) == 4:
        headless = inputs[3]
        
        if re.match('(?i)^(true|false)$', headless):
            if re.match('(?i)true', headless):
                condicao_previsao_do_tempo(
                    cidade=cidade, estado=estado, headless=True)
            if re.match('(?i)false', headless):
                condicao_previsao_do_tempo(
                    cidade=cidade, estado=estado, headless=False)
    else:
        condicao_previsao_do_tempo(cidade=cidade, estado=estado)

def print_examples():
    print("\n - Exemplo 1:")
    print("\tpython3 previsao_do_tempo_brasil.py Brasília DF")
    print("\n - Exemplo 2:")
    print("\tpython3 previsao_do_tempo_brasil.py \"são paulo\" sp")
    print("\n - Exemplo 3:")
    print("\t", end="")
    print(r"python3 previsao_do_tempo_brasil.py rio\ de\ janeiro rj")

def isStringAValidFixedLengthAcronym(
    s:str, length:int, acronym_list:List[Dict[str, str]]):
    
    if len(s.strip()) != length:
        return False
    return any(item['acronym'] == s.strip().upper() for item in acronym_list)

estados_brasileiros:List[Dict[str, str]] = [
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
    {"acronym": "TO", "name": "Tocantins"}]

def join(lista_de_itens:List[Union[Any, str]], 
        espacador_1:str="e", espacador_2:str=",") -> str:
    
        texto = ""
        for i in range(0, len(lista_de_itens)):
            texto += str(lista_de_itens[i])
            if i == len(lista_de_itens) - 1:
                return texto
            elif i == len(lista_de_itens) - 2:
                texto += f" {espacador_1} "
            else:
                texto += f"{espacador_2} "

def list_brazilian_states_acronyms_list(lista_estados:List[Dict[str, str]]):
    return [f"{estado['acronym']} ({estado['name']})"
        for estado in lista_estados]

def condicao_previsao_do_tempo(cidade:str, estado:str, headless:bool=False):
    resultados_condicao_tempo = condicao_tempo_accuweather(
        cidade=cidade, estado=estado, headless=headless)
    resultados_previsao_tempo = previsao_tempo_climatempo(
        cidade=cidade, estado=estado, headless=headless)
    results_printer = ResultsPrinter()
    results_printer.add(resultados_condicao_tempo)
    results_printer.add(resultados_previsao_tempo)
    results_printer.print_all()

class Results:
    def __init__(self:Any, title:str):
        self.title:str = title
        self.results:List[Dict[str, str]] = []
    
    def add(self:Any, result:Dict[str, str]):
        if list(result.keys())[0].strip() \
            and list(result.values())[0].strip():
            self.results.append(result)
        else:
            print("Resultado não foi adicionado pois ou a chave ou")
        
    def get_title(self:Any) -> str:
        return self.title

    def get_max_key_length(self:Any) -> int:
        max_title_length:int = 0
        for i in range(len(self.results)):
            if len(list(self.results[i].keys())[0]) > max_title_length:
                max_title_length = len(list(self.results[i].keys())[0])
        return max_title_length
        
class ResultsPrinter:
    def __init__(self:Any):
        self.result_list:List[Results] = []
    
    def add(self:Any, results:Results):
        self.result_list.append(results)
        
    def print_all(self:Any):
        data_hora = f"Data/hora: {str(dt.datetime.now())[0:19]}"
        print(f"{data_hora}\n{'-' * len(data_hora)}\n")
        padding, r_list = 0, self.result_list
        
        for r in r_list:
            if r.get_max_key_length() > padding:
                padding = r.get_max_key_length()
        padding += 2
        
        for i in range(len(r_list)):
            title = r_list[i].get_title()
            print(f"{title}\n{'-' * len(title)}")
            for j in range(len(r_list[i].results)):
                print(
                    f"{list(r_list[i].results[j].keys())[0].rjust(padding)}:",
                        end='')
                print(f" {list(r_list[i].results[j].values())[0]}")
                if j is len(r_list[i].results) - 1 \
                    and i is not len(self.result_list) - 1:
                    print()

def condicao_tempo_accuweather(
    cidade:str, estado:str, headless:bool=False) -> Results:
    
    browser = start_chrome(headless)
    browser.get("https://www.duckduckgo.com")
    browser.find_element(
        By.CSS_SELECTOR, 'input[type=text]').send_keys(
            f"accuweather pt br brazil weather {cidade} {estado}", Keys.ENTER)
    url = browser.find_element(
        By.CSS_SELECTOR, '#r1-0 h2 a').get_attribute("href")
    browser.get(format_accuweather_url(url))
    t.sleep(2)
    browser.implicitly_wait(2)
    
    title = "[AccuWeather] Condições meteorológicas em "
    title += f"{capitalize_all(cidade)}/{estado.upper()}, Brasil"
    results = Results(title)

    TempoAtual = browser.find_element(
        By.CSS_SELECTOR, '.current-weather-card h1').text
    
    tempoAtual = browser.find_element(
        By.CSS_SELECTOR,
            '.current-weather-card div.current-weather-info div.temp').text
    
    tempoAtualSensacao = browser.find_element(
        By.CSS_SELECTOR, '.current-weather-card div.phrase').text
    
    tempoAtualExtraRealFeelData = browser.find_element(
        By.CSS_SELECTOR, '.current-weather-card div.current-weather-extra'
            ).text.split('\n')
    
    weather_details = browser.find_element(
        By.CSS_SELECTOR, '.current-weather-card .current-weather-details'
            ).text.split('\n')
    
    browser.quit()
    
    tempoAtualExtraRealFeelTitulo = tempoAtualExtraRealFeelData[0].split(' ')[0]
    tempoAtualExtraRealFeelValor = tempoAtualExtraRealFeelData[0].split(' ')[1]
    
    tempoAtualExtraRealFeelShadeTitulo = ''
    tempoAtualExtraRealFeelShadeValor = ''
    
    if len(tempoAtualExtraRealFeelData) == 2:
        tempoAtualExtraRealFeelShadeTitulo = \
            tempoAtualExtraRealFeelData[1].split(' ')[0] \
                + tempoAtualExtraRealFeelData[1].split(' ')[1]

        tempoAtualExtraRealFeelShadeValor = \
            tempoAtualExtraRealFeelData[1].split(' ')[2]
    
    results.add({TempoAtual:
        f"{tempoAtual} ({tempoAtualSensacao})"})

    results.add({tempoAtualExtraRealFeelTitulo:
        f"{tempoAtualExtraRealFeelValor}C"})
    
    if tempoAtualExtraRealFeelShadeTitulo and tempoAtualExtraRealFeelShadeValor:
        results.add({tempoAtualExtraRealFeelShadeTitulo:
            f"{tempoAtualExtraRealFeelShadeValor}C"})
 
    for i in range(len(weather_details)):
        if i % 2 == 0:
            results.add({f"{weather_details[i]}":
                f"{weather_details[i+1].replace('° C', '°C')}"})
            
    return results

def previsao_tempo_climatempo(cidade:str, estado:str, headless:bool=False) -> Results:
    browser = start_chrome(headless)
    browser.get("https://www.duckduckgo.com")
    
    browser.find_element(
        By.CSS_SELECTOR, "input[type=text]").send_keys(
            f"climatempo {cidade} {estado} brasil", Keys.ENTER)

    browser.find_element(
        By.CSS_SELECTOR, "#r1-0 h2 a").click()
    
    t.sleep(2)
    browser.implicitly_wait(2)
    
    data, option = [], 0
    title = "[ClimaTempo] Previsão do tempo em "
    title += f"{capitalize_all(cidade)}/{estado.upper()}, Brasil"
    results = Results(title)

    try:
        data = browser.find_element(
            By.CSS_SELECTOR,
            'div[class="card -no-top -no-bottom"]').text.split("\n")

        option = 1
    except:
        try:
            data = browser.find_element(
                By.CSS_SELECTOR, "#first-block-of-days section")

            option = 2
            data = remove_empty_elements(data.text.split("\n"))
        except:
            print("Informações indisponíveis. Tente novamente.")
            browser.quit()
            return
    
    browser.quit()

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

        results.add({"Temperatura mínima": f"{temp_min}C"})    
        results.add({"Temperatura máxima": f"{temp_max}C"})    
        results.add({"Comparação": comparacao})    
        results.add({"Previsão": limit_empty_spaces(previsao)})
        results.add({"Precipitação": precipitacao})
        results.add({"Humidade mínima": umidade_min})
        results.add({"Humidade máxima": umidade_max})
        if nascer_por_sol:
            results.add({
                "Nascer/pôr do sol": nascer_por_sol.replace(' ', ' / ')})

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

        results.add({"Temperatura mínima": f"{temp_min}C"})
        results.add({"Temperatura máxima": f"{temp_max}C"})
        results.add({"Previsão": previsao})
        results.add({"Pluviosidade": pluviosidade})
        results.add({"Umidade": umidade})
        results.add({"Nascer/pôr do sol": nascer_por_sol.replace('-', '/')})
        results.add({"Lua": lua})

    return results

def start_chrome(headless:bool=False):
    options = webdriver.ChromeOptions()
    headless and options.add_argument('--headless')
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    options.add_argument('--incognito')
    options.add_argument('--disable-plugins-discovery')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    
    return webdriver.Chrome(options=options)

def format_accuweather_url(url:str):
    return url.replace('en', 'pt').replace(
        'weather-forecast', 'current-weather')

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
    return " ".join(capitalized_words)

def remove_empty_elements(arr:List[str]):
    clean_arr = []
    for i in arr:
        if i != "":
            clean_arr.append(i)
    return clean_arr

def limit_empty_spaces(text: str):
    return re.sub(r"\s{2,}", " ", text, 0)

if __name__ == "__main__":
    main()
