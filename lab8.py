mounth = 0
invest = 333
brutto = 3891
netto = brutto*0.8
suma = 0
bbjon=0
p = 1.08

while mounth < 12:
    suma *= p
    suma += invest
    bbjon+= netto-invest
    mounth +=1
    print((suma)//1,mounth)
print((suma+bbjon)//1)