numero=5
fattoriale=1

def fatt_ricc(nume,fatt):
    fatt *= nume
    nume-=1
    if(nume>0):
        return fatt_ricc(nume,fatt)
    else:
        return fatt

fattoriale=fatt_ricc(numero,fattoriale)
print(fattoriale)