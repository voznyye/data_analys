import math
import random
import csv
import numpy as np
import pandas as pd

with open('babyNames_normalized.csv', newline='\n') as f:
    reader = csv.reader(f)
    dane_normal = list(reader)

dane_unpacked = np.array([[float(item) for item in row] for row in dane_normal])

liczbaKlastrów = 15
klastry = []
Centroidy = []

def EuklidesPower(krotkaNormal, centroida):
    if centroida is None:
        return float('inf')  # Возвращаем бесконечность, если центроида нет
    dif = np.array(centroida[:4]) - np.array(krotkaNormal[:4])
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

def przypiszKrotkomNumeryKlastrów():
    global dane_unpacked
    new_column = np.empty((len(dane_unpacked), 1))  # Создаем новый столбец
    for i in range(len(dane_unpacked)):
        minimum = float('inf')
        minimumIndex = -1
        for j, centroida in enumerate(Centroidy):
            dist = EuklidesPower(dane_unpacked[i], centroida)
            if dist < minimum:
                minimum = dist
                minimumIndex = j
        new_column[i] = minimumIndex  # Записываем новое значение в новый столбец
    dane_unpacked = np.hstack((dane_unpacked, new_column))  # Добавляем новый столбец к исходному массиву

def utwórzKlastry():
    global klastry
    dane_copy = dane_unpacked.copy()  # Создаем копию массива
    klastry = [[] for _ in range(liczbaKlastrów)]
    for krotka in dane_copy:
        cluster_index = int(krotka[-1])
        klastry[cluster_index].append(krotka)

def wypiszCentroidy():
    centroidy_df = pd.DataFrame(Centroidy, columns=['YearOfBirth', 'NameEncoded', 'SexEncoded', 'NumberOfBirth'])
    centroidy_df['Cluster'] = range(len(Centroidy))
    centroidy_df.to_csv('wynik.csv', index=False, mode='a')

def wypiszKlastry():
    klastry_data = []
    for numer in range(len(Centroidy)):
        for krotka in klastry[numer]:
            klastry_data.append(list(krotka[:4]) + [numer])
    klastry_df = pd.DataFrame(klastry_data, columns=['YearOfBirth', 'NameEncoded', 'SexEncoded', 'NumberOfBirth', 'ClusterNumber'])
    klastry_df.to_csv('wynik.csv', index=False, mode='a')

def newCentroide(klaster):
    if not klaster:
        return None
    centroida = np.mean(klaster, axis=0)
    centroida[-1] = np.mean(klaster[-1])  # Используем среднее значение NumberOfBirth из существующих данных
    return centroida[:4]


def newCentroidy():
    global Centroidy
    new_Centroidy = []
    for nr in range(liczbaKlastrów):
        new_centroida = newCentroide(klastry[nr])
        if new_centroida is None:
            # Если кластер пустой, сохраняем старую центроиду
            new_centroida = Centroidy[nr]
        new_Centroidy.append(new_centroida)
    Centroidy = new_Centroidy

