from datetime import date, datetime
from database import data_plantio, setIdade, Ai

Area = Ai*10000
data1 = date.today()
data2 = datetime.strptime(data_plantio, "%d/%m/%Y").date()

idade = data1 - data2

idade = idade.days

setIdade(idade)
print(idade)
