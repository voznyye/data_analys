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

liczbaKlastrów = 15
klastry = []
Centroidy = []

def writeCsv(*args):
    with open('wynik.csv', 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(args)

def losujCentroide():
    centroida = []
    YearOfBirth = random.uniform(0.01, 9.1)
    centroida.append(YearOfBirth)
    
    NameEncoded = random.choice([0.01, 9.1])
    centroida.append(NameEncoded)
    
    SexEncoded = random.uniform(0.01, 9.1)
    centroida.append(SexEncoded)
    
    Number = random.uniform(0.01, 9.1)
    centroida.append(Number)
    
    return centroida

def losujCentroidy():
    global Centroidy
    Centroidy = [losujCentroide() for _ in range(liczbaKlastrów)]

def wypiszCentroide(centroida):
    writeCsv(centroida[0], centroida[1], centroida[2], centroida[3])

def wypiszCentroidy():
    writeCsv('CENTROIDY')
    for centroida in Centroidy:
        wypiszCentroide(centroida)

def EuklidesPower(krotkaNormal, centroida):
    suma = 0
    for i in range(len(krotkaNormal)):
        if i != 1:
            dif = float(centroida[i]) - float(krotkaNormal[i])
            difpow = math.pow(dif, 2)
            suma += difpow
    return suma

def przypiszKrotkomNumeryKlastrów():
    global dane_unpacked
    for krotka in dane_unpacked:
        minimum = float('inf')
        minimumIndex = -1
        for i, centroida in enumerate(Centroidy):
            dist = EuklidesPower(krotka, centroida)
            if dist < minimum:
                minimum = dist
                minimumIndex = i
        krotka.append(minimumIndex)

def utwórzKlastry():
    global klastry
    klastry = [[] for _ in range(liczbaKlastrów)]
    for krotka in dane_unpacked:
        cluster_index = krotka[-1]
        klastry[cluster_index].append(krotka)

def wypiszKlaster(nrKlastra):
    writeCsv('NUMER KLASTRA', nrKlastra)
    for krotka in klastry[nrKlastra]:
        writeCsv(krotka[0], krotka[1], krotka[2], krotka[3])

def wypiszKlastry():
    for numer in range(len(Centroidy)):
        wypiszKlaster(numer)

def newCentroide(klaster):
    if not klaster:
        return losujCentroide()
    centroida = []
    for i in range(len(klaster[0]) - 1):
        if i != 1:
            centroida.append(sum(krotka[i] for krotka in klaster) / len(klaster))
        else:
            centroida.append(random.choice([-0.8296983862193115, 1.2052572556597374]))
    return centroida

def newCentroidy():
    global Centroidy
    writeCsv('\nprzesunięто centroidy ------------')
    Centroidy = [newCentroide(klastry[nr]) for nr in range(liczbaKlastrów)]

