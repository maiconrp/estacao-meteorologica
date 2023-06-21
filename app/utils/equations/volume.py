from utils.equations.etc import Etc
from database import Am, esp_linhas, esp_plantas, vazao, TR, Ai

Cu = 0.85

print(Etc)

#Vt = volume total de água a ser aplicado por irrigação, m3;
#Ai = 0.5
Vt = 1000*((Etc*TR*Ai)/(Cu))

Vt = (int(Vt/100))

print(Vt)

esp_plantas = esp_plantas/100
esp_linhas = esp_linhas/100

Ti = 6*((Vt*esp_linhas*esp_plantas)/(Ai*vazao))

Ti = round(Ti)

print(Ti)

#Tempo de funcionamento por posição(Setor) para Irrigação em faixa contínua


