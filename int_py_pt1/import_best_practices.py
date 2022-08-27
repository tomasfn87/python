# 1) Right #1
import math
import re
#--------------
# 2) Wrong
# import math, re
#==================

texto1 = 'A máquina não era deus não, nem possuía os distintivos\
 femininos de que o herói gostava tanto. Caldo de cana é bom, mas\
 faz bem para a saúde?'
def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    return sentencas

x = math.sqrt(144)
print(x, separa_sentencas(texto1))