## Cálculo da Evapotranspiração de Referência (ETo)
## https://ainfo.cnptia.embrapa.br/digital/bitstream/CNPUV/8815/1/cir065.pdf
from database import Rn, vv, ur, Temp

# Definição das variáveis

Rn = 12.3
G = 0 # Fluxo total diário de calor do solo em MJ/m2.dia 
z = 335     # Altitude do local em m'''

# Cálculo da declividade da curva de pressão de vapor em relação à temperatura (kPa/oC)
delta = 4098*(0.6108*2.71828**((17.27*Temp)/(Temp+237.3)))/(Temp+237.3)**2


# Cálculo do coeficiente psicométrico (kPa/oC)
gama = 0.665*(0.001)*(101.3*((293-0.0065*z)/293)**5.26)


# Cálculo do déficit de saturação 
# (Diferença entre Pressão de saturação de vapor - es e Pressão atual de vapor - ea) (kPa)
es = 0.6108*2.71828**((17.27*Temp)/(Temp+237.3))

ea = (es*ur)/100


# Cálculo da Evapotranspiração de Referência em mm
EToPMF = (0.408*delta*(Rn-G)+((gama*900*vv*(es-ea))/(Temp+273)))/(delta+gama*(1+0.34*vv))
print(EToPMF)
