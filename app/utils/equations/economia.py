from database import tempo_ant, vazao, Ai, esp_linhas, esp_plantas
from utils.equations.volume import Ti, Vt

economia = 100 - (((Ti/60)*vazao)/((tempo_ant/60)*vazao)*100)

quant_gotej = ((Ai*10000)/((esp_linhas/100)*(esp_plantas/100)))

litros_economizados = (quant_gotej*(tempo_ant/60)*vazao)-(Vt*1000)

litros_economizados = round(litros_economizados)
print(litros_economizados)

