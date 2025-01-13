numero=5
fattoriale=1

def fatt_ricc(nume,fattt):
    fattt *= nume
    nume-=1
    if(nume>0):
        return fatt_ricc(nume,fattt)
    else:
        return fattt

fattoriale=fatt_ricc(numero,fattoriale)
print(fattoriale)