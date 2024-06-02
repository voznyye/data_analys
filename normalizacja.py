import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
import plotly.express as px


def normalizuj():
    # Загрузка данных из CSV файла
    data = pd.read_csv('babyNamesUSYOB-full.csv')

    # Удаление строк с отсутствующими значениями
    data.dropna(inplace=True)

    # Преобразование имен и пола в числовые значения
    label_encoder = LabelEncoder()
    data['NameEncoded'] = label_encoder.fit_transform(data['Name'])
    data['SexEncoded'] = label_encoder.fit_transform(data['Sex'])
    data['NumberEncoded'] = label_encoder.fit_transform(data['Number'])
    data['YearEncoded'] = label_encoder.fit_transform(data['YearOfBirth'])

    # Выбор признаков для кластеризации
    x = data[['YearEncoded', 'NameEncoded', 'SexEncoded', 'NumberEncoded']]
    y = data[['YearOfBirth', 'YearEncoded', 'Name', 'NameEncoded', 'Sex', 'SexEncoded', 'Number', 'NumberEncoded']]

    # Создание объекта для масштабирования данных
    scaler = StandardScaler()

    # Нормализация данных
    X_scaled = scaler.fit_transform(x)

    # Преобразование нормализованных данных обратно в DataFrame
    X_scaled_df = pd.DataFrame(X_scaled, columns=['YearEncoded', 'NameEncoded', 'SexEncoded', 'NumberEncoded'])

    # Сохранение нормализованных данных в CSV файл
    X_scaled_df.to_csv('babyNames_normalized.csv', index=False, header=False, mode='a')

    # Объединение нормализованных данных и оригинальных данных в нужном порядке
    combined_df = y.copy()
    combined_df[['YearEncoded', 'NameEncoded', 'SexEncoded', 'NumberEncoded']] = X_scaled_df[['YearEncoded', 'NameEncoded', 'SexEncoded', 'NumberEncoded']]

    # Запись объединенных данных в новый CSV файл
    combined_df.to_csv('babyNames_combined.csv', index=False, mode='a')
    
    
normalizuj()