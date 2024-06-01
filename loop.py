import math
import random
import csv
import numpy as np

# Открытие файла и чтение данных
with open('/mnt/data/babyNames_normalized.csv', newline='\n') as f:
    reader = csv.reader(f)
    dane_normal = list(reader)

# Преобразование данных в float и numpy массив
dane_unpacked = np.array([[float(item) for item in row] for row in dane_normal])

liczbaKlastrów = 6
klastry = []
Centroidy = []

def writeCsv(*args):
    with open('/mnt/data/wynik.csv', 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(args)

def EuklidesPower(krotkaNormal, centroida):
    dif = np.array(centroida) - np.array(krotkaNormal)
    difpow = np.square(dif)
    suma = np.sum(difpow)
    return suma

def kmeans_plus_plus():
    global Centroidy
    Centroidy = []
    # Шаг 1: случайный выбор первой центроиды
    first_centroid = dane_unpacked[random.randint(0, len(dane_unpacked) - 1)]
    Centroidy.append(first_centroid)

    # Шаг 2: выбор остальных центроид
    for _ in range(1, liczbaKlastrów):
        distances = np.zeros(len(dane_unpacked))
        for i, krotka in enumerate(dane_unpacked):
            min_dist = min(EuklidesPower(krotka, centroida) for centroida in Centroidy)
            distances[i] = min_dist

        sum_distances = np.sum(distances)
        probabilities = distances / sum_distances
        cumulative_probabilities = np.cumsum(probabilities)
        r = random.random()

        for i, cum_prob in enumerate(cumulative_probabilities):
            if r < cum_prob:
                Centroidy.append(dane_unpacked[i])
                break

def wypiszCentroide(centroida):
    writeCsv(centroida[0], centroida[1], centroida[2], centroida[3])

def wypiszCentroidy():
    writeCsv('CENTROIDY')
    for centroida in Centroidy:
        wypiszCentroide(centroida)

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
        if len(krotka) > 4:
            krotka[4] = minimumIndex
        else:
            krotka = np.append(krotka, minimumIndex)

def utwórzKlastry():
    global klastry
    klastry = [[] for _ in range(liczbaKlastrów)]
    for krotka in dane_unpacked:
        cluster_index = int(krotka[-1])
        klastry[cluster_index].append(krotka)

def wypiszKlaster(nrKlastra):
    writeCsv('NUMER KLASTRA', nrKlastra)
    for krotka in klastry[nrKlastra]:
        writeCsv(krotka[0], krotka[1], krotka[2], krotka[3], nrKlastra)

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
            centroida.append(random.choice([0.01, 9.1]))
    return centroida

def newCentroidy():
    global Centroidy
    writeCsv('\nprzesunięto центроиды ------------')
    Centroidy = [newCentroide(klastry[nr]) for nr in range(liczbaKlastrów)]
    # Проверка на пустые кластеры и переинициализация
    for i, klaster in enumerate(klastry):
        if not klaster:
            Centroidy[i] = losujCentroide()

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

# Основной алгоритм
kmeans_plus_plus()  # Инициализация центроидов с использованием K-Means++
przypiszKrotkomNumeryKlastrów()  # Присвоение точкам ближайших кластеров
utwórzKlastry()  # Создание кластеров
wypiszCentroidy()  # Запись центроидов
wypiszKlastry()  # Запись кластеров

# Перераспределение кластеров
for _ in range(10):  # Количество итераций перераспределения
    newCentroidy()
    przypiszKrotkomNumeryKlastrów()
    utwórzKlastry()
    wypiszCentroidy()
    wypiszKlastry()
