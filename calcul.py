#moduł przechowuje początkową liczbę klastrów,
#oraz poczatkową pustą listę klastrów i centroidów.
#UWAGA: wartości poczatkowe zmiennych modułowych
#       są dostępne po każdorazowym załadowaniu modułu

import math
import random
import csv


# Открытие файла и чтение данных
with open('babyNames_normalized.csv', newline='\n') as f:
    reader = csv.reader(f)
    dane_normal = list(reader)
    
# Преобразование данных в float
dane_unpacked = []
for row in dane_normal:
    float_row = [float(item) for item in row]
    dane_unpacked.append(float_row)


liczbaKlastrów=5
# poczatkowa liczba klastrów
klastry=[]
#każdy z klastrów jest listą krotekNormal położonych najbliżej centroidy
Centroidy=[]


def writeCsv(*args):
    with open('wynik.csv', 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(args)

def losujCentroide():
# losuje początkowe położenie centroidy dla pojedynczego klastra
    centroida=[]
    YearOfBirth=random.uniform(-0.00012687038921343276,9.994243197473356)
    centroida.append(YearOfBirth)
    
    NameEncoded=random.choice([-0.8296983862193115,1.2052572556597374])
    centroida.append(NameEncoded)
    
    SexEncoded=random.uniform(-0.00012687038921343276, 9.994243197473356)
    centroida.append(SexEncoded)
    
    Number=random.uniform(-0.00012687038921343276,9.994243197473356)
    centroida.append(Number)
    
    return centroida

def losujCentroidy():
# losuje określoną przez liczbę klastrów poczatkowe położenia centroid
    i=1
    while i<=liczbaKlastrów:
        Centroidy.append(losujCentroide())
        i=i+1

def wypiszCentroide(centroida):
       writeCsv(centroida[0],centroida[1],centroida[2],centroida[3])

def wypiszCentroidy():
# wypisuje do interpretera aktualne wartości wszystkich centroid
   writeCsv('CENTROIDY')
   for centroida in Centroidy:
      wypiszCentroide(centroida)

def EuklidesPower(krotkaNormal,centroida):
# zwraca kwadrat odległości euklidesowej danej krotkiNormal od danej centroidy
   suma=0
   for i in range(0,len(krotkaNormal)-1):
       if i != 1:
          dif=float(centroida[i]) - float(krotkaNormal[i])
          difpow=math.pow(dif,2)
          suma+=difpow
   distance=math.sqrt(suma)
   return math.pow(distance,2)

def przypiszKrotkomNumeryKlastrów():
# przypisuje każdej znormalizowanej krotce najbliższą centroidę
    for dane_unpacked in dane_normal:
        minimum=1e100
        for i in range(len(Centroidy)):
            next=EuklidesPower(dane_unpacked,Centroidy[i])
            if next<minimum:
                minimum=next
                minimumIndex=i
        dane_unpacked[3]=minimumIndex

def utwórzKlastry():
    for i in range(0,len(Centroidy)):
        klaster=[]
        for krotka in dane_normal:
            if krotka[3]==i:
                klaster.append(krotka)
        klastry.append(klaster)

def wypiszKlaster(nrKlastra):
    writeCsv('NUMER KLASTRA',nrKlastra)
    for krotka in klastry[nrKlastra]:
        writeCsv (krotka[0],krotka[1],krotka[2],krotka[3])

def wypiszKlastry():
# wypisuje do interpretera aktualne wartości wszystkich klastrów
    for numer in range(0,len(Centroidy)):
       wypiszKlaster(numer)

def newCentroide(klaster):
# oblicza nowe położenie centroidy we wskazanym klastrze
# i zwraca wynik w postaci nowej centroidy dla wskazanego klastra
    sumState=sumYear=0
    sumFemName=sumMalName=numFemName=numMalName=0
    centroida=[]
    for krotka in klaster:
        sumState+=krotka[0]
        if krotka [1]==100:
            sumFemName+=krotka[3]
            numFemName+=1
        else:
            sumMalName+=krotka[3]
            numMalName+=1
        sumYear+=krotka[2]
    centroida.append(sumState//len(klaster))
    if numFemName>=numMalName:
        centroida.append(-0.8296983862193115)
    else:
        centroida.append(1.2052572556597374)
    centroida.append(sumYear//len(klaster))
    if numFemName>=numMalName:
        centroida.append(sumFemName//numFemName)
    else:
        centroida.append(sumMalName//numMalName)
    return centroida

def newCentroidy():
    Centroidy=[]
    writeCsv('\nprzesunięto centroidy ------------')
    for nr in range(liczbaKlastrów):
        Centroidy.append(newCentroide(klastry[nr]))


