import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
import plotly.express as px

# Загрузка данных из CSV файла
data = pd.read_csv('babyNamesUSYOB-full.csv')

# Удаление строк с отсутствующими значениями
data.dropna(inplace=True)

# Преобразование имен в числовые значения
label_encoder = LabelEncoder()
data['NameEncoded'] = label_encoder.fit_transform(data['Name'])

# Выбор признаков для кластеризации
X = data[['YearOfBirth', 'NameEncoded']]

# Создание объекта для масштабирования данных
scaler = StandardScaler()

# Нормализация данных
X_scaled = scaler.fit_transform(X)

# Инициализация модели k-means
kmeans = KMeans(n_clusters=12, random_state=42)

# Обучение модели
kmeans.fit(X_scaled)

# Получение меток кластеров для каждого примера
labels = kmeans.labels_

# Добавление меток кластеров в исходные данные
data['Cluster'] = labels

# Вывод результатов кластеризации
print(data.head())

# Визуализация результатов с использованием plotly
fig = px.scatter(data, x='YearOfBirth', y='NameEncoded', color='Cluster', title='Clusters of Birth Names')
fig.show()
