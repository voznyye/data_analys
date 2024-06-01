import matplotlib.pyplot as plt
import matplotlib
from sklearn.cluster import KMeans
import pandas as pd


matplotlib.use('agg')
# Чтение данных
data = pd.read_csv('babyNames_normalized.csv')

# Преобразование данных в float
data = data.astype(float)

def calculate_sse(data, max_k):
    sse = []
    for k in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(data)
        sse.append(kmeans.inertia_)
    return sse

# Определение максимального количества кластеров для анализа
max_k = 20
sse = calculate_sse(data, max_k)

# Построение графика метода локтя
plt.figure(figsize=(10, 6))
plt.plot(range(1, max_k + 1), sse, marker='o')
plt.xlabel('Количество кластеров')
plt.ylabel('SSE')
plt.title('Метод локтя для определения оптимального количества кластеров')
plt.grid(True)
plt.savefig('fig.png')
plt.show()
