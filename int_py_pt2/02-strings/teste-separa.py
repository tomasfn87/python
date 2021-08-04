import separa
import pytest

class Teste_Separa():
    '''Qualquer função dentro de uma classe tem como primeiro parâmetro
    self (?), incluindo os fixtures do pytest.
    '''

    @pytest.fixture
    def sep_f(self):
        return separa.separa_f

    @pytest.fixture
    def sep_w(self):
        return separa.separa_w
    
    @pytest.mark.parametrize("string_entrada, resultado", [
        (" Oi, tudo bem?", ["Oi,", "tudo", "bem?"]),
        ("   Tudo ótimo, e com você ?", ["Tudo", "ótimo,", "e", "com", "você", "?"]),
        ("  Que  horas   são?", ["Que", "horas", "são?"]),
        (" Booom diiia !!!", ["Booom", "diiia", "!!!"]),
        ("Será que vale a pena?", ["Será", "que", "vale", "a", "pena?"]),
        ("Quero sim, por favor...", ["Quero", "sim,", "por", "favor..."]),
        ("      Vamos   deixar     para    outro   dia!", ["Vamos", "deixar", "para", "outro", "dia!"]),
        ("Beleza           !", ["Beleza", "!"]),
        ("Tranquilo!", ["Tranquilo!"]),
        ("  Oi!  ", ["Oi!"]),
        (" Oi! ", ["Oi!"]),
        ("Oi!", ["Oi!"]),
        ("Oi !", ["Oi", "!"])
    ])

    def teste_separa(self, string_entrada, resultado, sep_f, sep_w):
        # É preciso adicionar os fixtures como parâmetros do teste
        assert sep_f(string_entrada) == resultado \
           and sep_w(string_entrada) == resultado