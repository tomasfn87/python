import requests as req
import re
import sys
import time as t
import datetime as dt
import numpy as np
from selenium import webdriver as wd
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
    if not is_a_valid_fixed_length_acronym(
        s=estado, length=2, acronym_list=estados_brasileiros):
        print("ERRO: o segundo argumento deve ser uma sigla válida ", end="")
        print("de estado brasileiro (UF).")
        print("\n  Siglas válidas:\n  ---------------\n\n    {}.".format(
            join(list_brazilian_states_acronyms_list(
                lista_estados=estados_brasileiros), "ou")))
    
    if not is_web_connection_active():
        print("ERRO: sem conexão à Internet.")
        return

    if len(inputs) == 4:
        headless = inputs[3]
        if re.match("(?i)^(true|false)$", headless):
            if re.match("(?i)true", headless):
                condicao_previsao_do_tempo(
                    cidade=cidade, estado=estado, headless=True)
            if re.match("(?i)false", headless):
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

def is_a_valid_fixed_length_acronym(
    s:str, length:int, acronym_list:List[Dict[str, str]]):

    if len(s.strip()) != length:
        return False
    return any(i["acronym"] == s.strip().upper() for i in acronym_list)

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

        texto:str = ""
        for i in range(0, len(lista_de_itens)):
            texto += str(lista_de_itens[i])
            if i == len(lista_de_itens) - 1:
                return texto
            elif i == len(lista_de_itens) - 2:
                texto += f" {espacador_1} "
            else:
                texto += f"{espacador_2} "

def list_brazilian_states_acronyms_list(
    lista_estados:List[Dict[str, str]]) -> List[str]:

    return [
        f'{estado["acronym"]} ({estado["name"]})'
            for estado in lista_estados
    ]

def condicao_previsao_do_tempo(cidade:str, estado:str, headless:bool=False):
    resultados_condicao_tempo:Results = condicao_tempo_accuweather(
        cidade=cidade, estado=estado, headless=headless)

    resultados_previsao_tempo:Results = previsao_tempo_climatempo(
        cidade=cidade, estado=estado, headless=headless)

    results_printer:ResultsPrinter = ResultsPrinter(margin=2)
    results_printer.add_results(resultados_condicao_tempo)
    results_printer.add_results(resultados_previsao_tempo)
    results_printer.print_all()
    
def is_web_connection_active() -> bool:
    try:
        response:req.Response = req.get("https://www.google.com", timeout=5)
        response.raise_for_status()
        return True
    except req.RequestException:
        return False

class Results:
    def __init__(self:Any, title:str):
        self.title:str = title
        self.results:np.ndarray = np.array([],
            dtype=[("key", "U100"), ("value", "U100")])

    def add_key_value(self:Any, result:Dict[str, str]):
        key:str = list(result.keys())[0]
        value:str = list(result.values())[0]
        if key.strip() and value.strip():
            self.results = np.append(self.results, result)
        else:
            print(f"Resultado não foi adicionado (chave: {key}, valor: {value}).")

    def get_title(self:Any) -> str:
        return self.title

    def get_max_key_length(self:Any) -> int:
        max_key_length:int = 0
        for i in range(len(self.results)):
            key:str = list(self.results[i].keys())[0]
            if len(key) > max_key_length:
                max_key_length = len(key)
        return max_key_length

class ResultsPrinter:
    def __init__(self:Any, margin):
        if margin < 1:
            self.margin = 2
        else:
            self.margin = margin
        self.result_list:np.ndarray = np.array([], dtype=Results)

    def add_results(self:Any, results:Results):
        self.result_list = np.append(self.result_list, results)

    def print_all(self:Any):
        data_hora:str = f"Data/hora: {str(dt.datetime.now())[0:19]}"
        print(f'{data_hora}\n{"-" * len(data_hora)}\n')

        padding:int = 0
        r_list:np.ndarray = self.result_list

        for r in r_list:
            if r.get_max_key_length() > padding:
                padding = r.get_max_key_length()
        padding += self.margin

        for i in range(len(r_list)):
            title = r_list[i].get_title()
            print(f'{title}\n{"-" * len(title)}')
            for j in range(len(r_list[i].results)):
                key = list(r_list[i].results[j].keys())[0]
                value = list(r_list[i].results[j].values())[0]
                print(f"{key.rjust(padding)}: {value}")
                if j is len(r_list[i].results) - 1 \
                    and i is not len(self.result_list) - 1:
                    print()

def condicao_tempo_accuweather(
    cidade:str, estado:str, headless:bool=False) -> Results:

    browser:wd.WebDriver = start_chrome(headless)
    browser.get("https://www.duckduckgo.com")

    browser.find_element(
        By.CSS_SELECTOR, "input[type=text]").send_keys(
            f"accuweather pt br brazil weather {cidade} {estado}", Keys.ENTER)

    url:str = browser.find_element(
        By.CSS_SELECTOR, "#r1-0 h2 a").get_attribute("href")

    browser.get(format_accuweather_url(url))
    t.sleep(1)
    browser.implicitly_wait(1)

    title:str = "[AccuWeather] Condições meteorológicas em "
    title += f"{capitalize_all(cidade)}/{estado.upper()}, Brasil"
    results:Results = Results(title=title)

    tempoAtualTitulo:str = browser.find_element(
        By.CSS_SELECTOR, ".current-weather-card h1").text

    tempoAtualValor:str = browser.find_element(
        By.CSS_SELECTOR,
            ".current-weather-card div.current-weather-info div.temp").text

    tempoAtualSensacaoValor:str = browser.find_element(
        By.CSS_SELECTOR, ".current-weather-card div.phrase").text

    tempoAtualExtraRealFeelData:str = browser.find_element(
        By.CSS_SELECTOR, ".current-weather-card div.current-weather-extra"
            ).text.split("\n")

    weatherDetails:str = browser.find_element(
        By.CSS_SELECTOR, ".current-weather-card .current-weather-details"
            ).text.split("\n")

    browser.quit()

    tempoAtualExtraRealFeelTitulo:str = \
        tempoAtualExtraRealFeelData[0].split(" ")[0]

    tempoAtualExtraRealFeelValor:str = \
        tempoAtualExtraRealFeelData[0].split(" ")[1]

    tempoAtualExtraRealFeelShadeTitulo:str = ""
    tempoAtualExtraRealFeelShadeValor:str = ""

    if len(tempoAtualExtraRealFeelData) == 2:
        tempoAtualExtraRealFeelShadeTitulo:str = \
            tempoAtualExtraRealFeelData[1].split(" ")[0] \
                + tempoAtualExtraRealFeelData[1].split(" ")[1]

        tempoAtualExtraRealFeelShadeValor:str = \
            tempoAtualExtraRealFeelData[1].split(" ")[2]

    results.add_key_value({tempoAtualTitulo:
        f"{tempoAtualValor} ({tempoAtualSensacaoValor})"})

    results.add_key_value({tempoAtualExtraRealFeelTitulo:
        f"{tempoAtualExtraRealFeelValor}C"})

    if tempoAtualExtraRealFeelShadeTitulo and tempoAtualExtraRealFeelShadeValor:
        results.add_key_value({tempoAtualExtraRealFeelShadeTitulo:
            f"{tempoAtualExtraRealFeelShadeValor}C"})

    for i in range(len(weatherDetails)):
        if i % 2 == 0:
            results.add_key_value({f"{weatherDetails[i]}":
                f'{weatherDetails[i+1].replace("° C", "°C")}'})

    return results

def previsao_tempo_climatempo(
    cidade:str, estado:str, headless:bool=False) -> Results:

    browser:wd.WebDriver = start_chrome(headless)
    browser.get("https://www.duckduckgo.com")

    browser.find_element(
        By.CSS_SELECTOR, "input[type=text]").send_keys(
            f"climatempo {cidade} {estado} brasil", Keys.ENTER)

    browser.find_element(
        By.CSS_SELECTOR, "#r1-0 h2 a").click()

    t.sleep(1)
    browser.implicitly_wait(1)

    data:List[str] = []
    option:int = 0
    
    title:str = "[ClimaTempo] Previsão do tempo em "
    title += f"{capitalize_all(cidade)}/{estado.upper()}, Brasil"
    results:Results = Results(title=title)

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
        tempMin = data[7]
        tempMax = data[8]
        precipitacao = data[10]
        umidadeMin = data[14]
        umidadeMax = data[15]
        nascerPorSol = ""

        for i in range(0, len(data)):
            if data[i] == "Sol":
                nascerPorSol = data[i+1].replace("h", "")

        results.add_key_value({"Temperatura mínima": f"{tempMin}C"})
        results.add_key_value({"Temperatura máxima": f"{tempMax}C"})
        results.add_key_value({"Comparação": comparacao})
        results.add_key_value({"Previsão": limit_empty_spaces(previsao)})
        results.add_key_value({"Precipitação": precipitacao})
        results.add_key_value({"Humidade mínima": umidadeMin})
        results.add_key_value({"Humidade máxima": umidadeMax})
        if nascerPorSol:
            results.add_key_value({
                "Nascer/pôr do sol": nascerPorSol.replace(" ", " / ")})

    elif option == 2:
        tempMin = data[2]
        tempMax = data[3]
        pluviosidade = data[4]
        previsao = limit_empty_spaces(data[5])
        umidade = ""
        lua = ""
        nascerPorSol = ""

        for i in range(0, len(data)):
            if data[i] == "UMIDADE DO AR":
                umidade = data[i+1]

        for i in range(0, len(data)):
            if data[i] == "SOL":
                nascerPorSol = data[i+1]

        for i in range(0, len(data)):
            if data[i] == "LUA":
                lua = data[i+1]

        results.add_key_value({"Temperatura mínima": f"{tempMin}C"})
        results.add_key_value({"Temperatura máxima": f"{tempMax}C"})
        results.add_key_value({"Previsão": previsao})
        results.add_key_value({"Pluviosidade": pluviosidade})
        results.add_key_value({"Umidade": umidade})
        results.add_key_value({"Nascer/pôr do sol": nascerPorSol.replace("-", "/")})
        results.add_key_value({"Lua": lua})

    return results

def start_chrome(headless:bool=False):
    options:wd.ChromeOptions = wd.ChromeOptions()
    headless and options.add_argument("--headless")
    options.add_argument("--disable-extensions")
    options.add_argument("--profile-directory=Default")
    options.add_argument("--incognito")
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    prefs:Dict[str, int] = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    return wd.Chrome(options=options)

def format_accuweather_url(url:str):
    return url.replace("en", "pt").replace(
        "weather-forecast", "current-weather")

def capitalize_all(text:str):
    exclude = ["de", "da", "do", "dos", "das"]
    words = text.split(" ")
    for w in words:
        w = w.lower()
    capitalized_words = []
    for w in words:
        if w in exclude or w[0:2] == 'd\"':
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
