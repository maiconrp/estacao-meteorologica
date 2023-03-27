import math

print("Calcular volume de água diário por planta")

ETo= float(input("Evapotranspiração do cultivo de referência, em mm/dia "))
a= float(input("Fração da área molhada, em decimais "))
As = float(input("Area sombreada, em m2 "))
Cu = float(input("Coeficiente de uniformidade de aplicação, em decimais"))
Kc = float(input("Coeficiente de cultura, adimensional"))
Am = 

Va= a+0.15*(1.0-a)
V= ETo* Va *(As/Cu)*Kc

print("o volume de água diário por planta",V )
