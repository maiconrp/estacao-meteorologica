import math


print("Calcular evapotranspiracao de cultura")

Eto= float(input("Qual o valor da evapotranspiracao de referencia?"))
Kc= float(input("qual o coeficiente de crescimento da cultura utilizada?"))
Etc= (Eto*Kc)

print("a evapotranspiracao da sua cultura é", Etc )
