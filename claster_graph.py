import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Создадим DataFrame из предоставленных данных
data = {
    "YearOfBirth": [1880]*19,
    "Name": ["Mary", "Anna", "Emma", "Elizabeth", "Minnie", "Margaret", "Ida", "Alice", "Bertha", "Sarah",
             "Annie", "Clara", "Ella", "Florence", "Cora", "Martha", "Laura", "Nellie", "Grace"],
    "Sex": ["F"]*19,
    "Number": [7065, 2604, 2003, 1939, 1746, 1578, 1472, 1414, 1320, 1288,
               1258, 1226, 1156, 1063, 1045, 1040, 1012, 995, 982]
}

df = pd.DataFrame(data)

# Выберем только числовые данные для кластеризации
X = df[['Number']]

# Стандартизация данных
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Применим алгоритм K-means
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Визуализация результатов кластеризации
plt.figure(figsize=(10, 6))
plt.scatter(df['Number'], [0]*len(df), c=df['Cluster'], cmap='viridis')
for i, txt in enumerate(df['Name']):
    plt.annotate(txt, (df['Number'][i], 0), textcoords="offset points", xytext=(0,10), ha='center')
plt.xlabel('Number of Occurrences')
plt.title('K-means Clustering of Names by Number of Occurrences')
plt.yticks([])
plt.show()

# Выведем DataFrame с результатами кластеризации
print(df)
