import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
import plotly.express as px

# Загрузка данных из CSV файла
data = pd.read_csv('babyNamesUSYOB-full.csv')

# Удаление строк с отсутствующими значениями
data.dropna(inplace=True)

# Преобразование имен и пола в числовые значения
label_encoder = LabelEncoder()
data['NameEncoded'] = label_encoder.fit_transform(data['Name'])
data['SexEncoded'] = label_encoder.fit_transform(data['Sex'])

# Выбор признаков для кластеризации
x = data[['YearOfBirth', 'NameEncoded', 'SexEncoded', 'Number']]
y = data[['YearOfBirth', 'Name', 'NameEncoded', 'Sex', 'SexEncoded', 'Number']]

# Создание объекта для масштабирования данных
scaler = StandardScaler()

# Нормализация данных
X_scaled = scaler.fit_transform(x)

# Преобразование нормализованных данных обратно в DataFrame
X_scaled_df = pd.DataFrame(X_scaled, columns=['YearOfBirth', 'NameEncoded', 'SexEncoded', 'Number'])

# Сохранение нормализованных данных в CSV файл
X_scaled_df.to_csv('babyNames_normalized.csv', index=False)

# Объединение нормализованных данных и оригинальных данных в нужном порядке
combined_df = y.copy()
combined_df[['YearOfBirth', 'NameEncoded', 'SexEncoded', 'Number']] = X_scaled_df[['YearOfBirth', 'NameEncoded', 'SexEncoded', 'Number']]

# Запись объединенных данных в новый CSV файл
combined_df.to_csv('babyNames_combined.csv', index=False)