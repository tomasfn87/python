import json
import os
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

def main() -> None:
    inputs:List[str] = sys.argv
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

    cidade:str = inputs[1]
    estado:str = inputs[2]

    file_dir:str = os.path.dirname(os.path.realpath(__file__))
    with open(f"{file_dir}/brazilian_states_list.min.json", "r") as data:
        states_list_json:str = data.read()
        estados_brasileiros:List[Dict[str, str]] = json.loads(states_list_json)

    if not is_a_valid_fixed_length_acronym(
        s=estado, length=2, acronym_list=estados_brasileiros):
        print("ERRO: o segundo argumento deve ser uma sigla válida ", end="")
        print("de estado brasileiro (UF).")
        subtitle = "Siglas válidas:"
        print("\n  {}\n  {}\n\n    {}.".format(
            subtitle, "-" * len(subtitle), semantically_unite(
                list_brazilian_states_acronyms(
                    states_list=estados_brasileiros), "ou")))
        return

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

def print_examples() -> None:
    print("\n - Exemplo 1:")
    print("\tpython3 previsao_do_tempo_brasil.py Brasília DF")
    print("\n - Exemplo 2:")
    print("\tpython3 previsao_do_tempo_brasil.py \"são paulo\" sp")
    print("\n - Exemplo 3:")
    print("\t", end="")
    print(r"python3 previsao_do_tempo_brasil.py rio\ de\ janeiro rj")

def is_a_valid_fixed_length_acronym(
    s:str, length:int, acronym_list:List[Dict[str, str]]) -> bool:

    if len(s.strip()) != length:
        return False
    return any(i["acronym"] == s.strip().upper() for i in acronym_list)

def is_web_connection_active() -> bool:
    try:
        response:req.Response = req.get(url="https://www.google.com", timeout=5)
        response.raise_for_status()
        return True
    except req.RequestException:
        return False

def semantically_unite(item_list:List[Union[Any, str]],
    last_union:str="and", general_union:str=",") -> str:

    result:str = ""
    if len(item_list) == 1:
        result = item_list[0].strip()
    else:
        for i in range(0, len(item_list)):
            result += str(item_list[i])
            if i == len(item_list) - 2:
                result += f" {last_union} "
            else:
                result += f"{general_union} "
    return result

def list_brazilian_states_acronyms(
    states_list:List[Dict[str, str]]) -> List[str]:

    return [ f'{state["acronym"]} ({state["name"]})'
            for state in states_list ]

def condicao_previsao_do_tempo(
    cidade:str, estado:str, headless:bool=False) -> None:

    resultados_condicao_tempo:ResultSet = condicao_tempo_accuweather(
        cidade=cidade, estado=estado, headless=headless)

    resultados_previsao_tempo:ResultSet = previsao_tempo_climatempo(
        cidade=cidade, estado=estado, headless=headless)

    result_printer:ResultSetsPrinter = ResultSetsPrinter(margin=2)

    if resultados_condicao_tempo.get_num_of_results():
        result_printer.add_results(resultados_condicao_tempo)

    if resultados_previsao_tempo.get_num_of_results():
        result_printer.add_results(resultados_previsao_tempo)

    if result_printer.get_num_of_results():
        result_printer.print_all()
    else:
        print("ERRO: as informações estão indisponíveis. Tenta novamente mais tarde.")

class ResultSet:
    def __init__(self:Any, title:str="Result set title"):
        self.title:str = title
        self.num_of_results:int = 0
        self.results:List[Dict[str, str]] = []

    def add_key_value(self:Any, key:str, value:str) -> bool:
        if (not any(list(i.keys())[0] == key for i in self.results) \
            and key.strip() and value.strip()):
            self.results.append({key: value})
            self.num_of_results += 1
            return True
        else:
            print(f"Resultado não foi adicionado (chave: {key}, valor: {value}).")
            return False

    def get_title(self:Any) -> str:
        return self.title

    def get_num_of_results(self:Any) -> int:
        return self.num_of_results

    def get_max_key_length(self:Any) -> int:
        max_key_length:int = 0
        for i in range(len(self.results)):
            key:str = list(self.results[i].keys())[0]
            if len(key) > max_key_length:
                max_key_length = len(key)
        return max_key_length

class ResultSetsPrinter:
    def __init__(self:Any, margin:int):
        if margin < 1:
            self.margin = 2
        else:
            self.margin = margin
        self.num_of_results:int = 0
        self.result_list:List[ResultSet] = []

    def add_results(self:Any, results:ResultSet):
        if results.get_num_of_results():
            self.result_list.append(results)
            self.num_of_results += results.get_num_of_results()

    def get_num_of_results(self:Any) -> int:
        return self.num_of_results

    def print_all(self:Any):
        data_hora:str = f"Data/hora: {str(dt.datetime.now())[0:19]}"
        print(f'{data_hora}\n{"-" * len(data_hora)}\n')

        padding:int = 0
        r_list = self.result_list

        for r in r_list:
            if r.get_max_key_length() > padding:
                padding = r.get_max_key_length()
        padding += self.margin

        for i in range(len(r_list)):
            title = r_list[i].get_title()
            print(f'{title}\n{"-" * len(title)}')
            for j in range(len(r_list[i].results)):
                key   = list(r_list[i].results[j].keys())[0]
                value = list(r_list[i].results[j].values())[0]
                print(f"{key.rjust(padding)}: {value}")
                if j is len(r_list[i].results) - 1 \
                    and i is not len(self.result_list) - 1:
                    print()

def condicao_tempo_accuweather(
    cidade:str, estado:str, headless:bool=False) -> ResultSet:

    browser:wd.Chrome = start_chrome(headless)
    browser.get("https://www.duckduckgo.com")

    browser.find_element(
        By.CSS_SELECTOR, "input[type=text]").send_keys(
            f"accuweather pt br brazil weather {cidade} {estado}", Keys.ENTER)

    url:str|None = browser.find_element(
        By.CSS_SELECTOR, "#r1-0 h2 a").get_attribute("href")

    browser.get(format_accuweather_url(url))
    t.sleep(1)
    browser.implicitly_wait(1)

    title:str = "[AccuWeather] Condições meteorológicas em "
    title += f"{capitalize_all(cidade)}/{estado.upper()}, Brasil"
    results:ResultSet = ResultSet(title=title)

    tempoAtualTitulo:str = browser.find_element(
        By.CSS_SELECTOR, ".current-weather-card h1").text

    tempoAtualValor:str = browser.find_element(
        By.CSS_SELECTOR,
            ".current-weather-card div.current-weather-info div.temp").text

    tempoAtualSensacaoValor:str = browser.find_element(
        By.CSS_SELECTOR, ".current-weather-card div.phrase").text

    tempoAtualExtraRealFeelData = np.char.splitlines([browser.find_element(
        By.CSS_SELECTOR, ".current-weather-card div.current-weather-extra"
            ).text])[0]

    detalhes = np.char.splitlines([browser.find_element(
        By.CSS_SELECTOR, ".current-weather-card .current-weather-details"
            ).text])[0]

    browser.quit()

    tempoAtualExtraRealFeelTitulo:str = np.char.split(
        [tempoAtualExtraRealFeelData[0]])[0][0]
    tempoAtualExtraRealFeelValor:str = np.char.split(
        [tempoAtualExtraRealFeelData[0]])[0][1]

    tempoAtualExtraRealFeelShadeTitulo:str = ""
    tempoAtualExtraRealFeelShadeValor:str = ""

    if len(tempoAtualExtraRealFeelData) == 2:
        realFeel = np.char.split([tempoAtualExtraRealFeelData[1]])[0]
        tempoAtualExtraRealFeelShadeTitulo = f"{realFeel[0]} {realFeel[1]}"
        tempoAtualExtraRealFeelShadeValor = realFeel[2]

    results.add_key_value(tempoAtualTitulo,
        f"{tempoAtualValor} ({tempoAtualSensacaoValor})")

    results.add_key_value(tempoAtualExtraRealFeelTitulo,
        f"{tempoAtualExtraRealFeelValor}C")

    if tempoAtualExtraRealFeelShadeTitulo and tempoAtualExtraRealFeelShadeValor:
        results.add_key_value(tempoAtualExtraRealFeelShadeTitulo,
            f"{tempoAtualExtraRealFeelShadeValor}C")

    for i in range(len(detalhes)):
        if i % 2 == 0:
            results.add_key_value(f"{detalhes[i]}",
                f'{detalhes[i+1].replace("° C", "°C")}')

    return results

def previsao_tempo_climatempo(
    cidade:str, estado:str, headless:bool=False) -> ResultSet:

    browser:wd.Chrome = start_chrome(headless)
    browser.get("https://www.duckduckgo.com")

    browser.find_element(
        By.CSS_SELECTOR, "input[type=text]").send_keys(
            f"climatempo {cidade} {estado} brasil", Keys.ENTER)

    browser.find_element(
        By.CSS_SELECTOR, "#r1-0 h2 a").click()

    t.sleep(1)
    browser.implicitly_wait(1)

    data = np.array([], dtype="S")
    option:int = 0

    title:str = "[ClimaTempo] Previsão do tempo em "
    title += f"{capitalize_all(cidade)}/{estado.upper()}, Brasil"
    results:ResultSet = ResultSet(title=title)

    try:
        data = np.char.splitlines([browser.find_element(
            By.CSS_SELECTOR, 'div[class="card -no-top -no-bottom"]').text])[0]

        option = 1
    except:
        try:
            data = remove_empty_elements(np.char.splitlines(
                [browser.find_element(By.CSS_SELECTOR,
                    "#first-block-of-days section").text])[0])

            option = 2
        except:
            browser.quit()
            return ResultSet()

    browser.quit()

    tempMin:str = ""
    tempMax:str = ""
    previsao:str = ""
    nascerPorDoSol:str = ""

    if option == 1:
        comparacao:str = data[0]
        previsao = limit_empty_spaces(data[1])
        tempMin = data[7]
        tempMax = data[8]
        precipitacao:str = data[10]
        umidadeMin:str = data[14]
        umidadeMax:str = data[15]
        nascerPorDoSol = ""

        for i in range(0, len(data)):
            if data[i] == "Sol":
                nascerPorDoSol = data[i+1].replace("h", "")

        results.add_key_value("Temperatura mínima", f"{tempMin}C")
        results.add_key_value("Temperatura máxima", f"{tempMax}C")
        results.add_key_value("Comparação", comparacao)
        results.add_key_value("Previsão", limit_empty_spaces(previsao))
        results.add_key_value("Precipitação", precipitacao)
        results.add_key_value("Humidade mínima", umidadeMin)
        results.add_key_value("Humidade máxima", umidadeMax)
        if nascerPorDoSol:
            results.add_key_value("Nascer/pôr do sol",
                nascerPorDoSol.replace(" ", " / "))

    elif option == 2:
        tempMin = data[2]
        tempMax = data[3]
        pluviosidade:str = data[4]
        previsao = limit_empty_spaces(data[5])
        umidade:str = ""
        lua:str = ""
        nascerPorDoSol = ""

        for i in range(0, len(data)):
            if data[i] == "UMIDADE DO AR":
                umidade = data[i+1]

        for i in range(0, len(data)):
            if data[i] == "SOL":
                nascerPorDoSol = data[i+1]

        for i in range(0, len(data)):
            if data[i] == "LUA":
                lua = data[i+1]

        results.add_key_value("Temperatura mínima", f"{tempMin}C")
        results.add_key_value("Temperatura máxima", f"{tempMax}C")
        results.add_key_value("Previsão", previsao)
        results.add_key_value("Pluviosidade", pluviosidade)
        results.add_key_value("Umidade", umidade)
        results.add_key_value("Nascer/pôr do sol", nascerPorDoSol.replace("-", "/"))
        results.add_key_value("Lua", lua)

    return results

def start_chrome(headless:bool=False) -> wd.Chrome:
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

def format_accuweather_url(url:str|None) -> str:
    if url is None:
        return ""
    return url.replace("en", "pt").replace(
        "weather-forecast", "current-weather")

def capitalize_all(text:str) -> str:
    if " " not in text:
        return text.capitalize()
    exclude = np.array(["de", "da", "do", "dos", "das"], dtype="S")
    words = np.char.split([text])
    for w in words[0]:
        w = w.lower()
    capitalized_words = np.array([], dtype="S")
    for w in words[0]:
        if w in exclude or w[0:2] == "d'":
            capitalized_words = np.append(capitalized_words, w)
        else:
            capitalized_words = np.append(capitalized_words, w.capitalize())
    result = np.char.add(" ", capitalized_words)
    return "".join(result).strip()

def remove_empty_elements(arr: List[str]) -> np.ndarray:
    clean_arr = np.array([x for x in arr if x != ""], dtype=np.str_)
    return clean_arr

def limit_empty_spaces(text: str) -> str:
    return re.sub(r"\s{2,}", " ", text, 0)

if __name__ == "__main__":
    main()
