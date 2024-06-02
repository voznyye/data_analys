import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder


def normalizuj():
    data = pd.read_csv('babyNamesUSYOB-full.csv')

    data.dropna(inplace=True)

    label_encoder = LabelEncoder()
    data['NameEncoded'] = label_encoder.fit_transform(data['Name'])
    data['SexEncoded'] = label_encoder.fit_transform(data['Sex'])
    data['NumberEncoded'] = label_encoder.fit_transform(data['Number'])
    data['YearEncoded'] = label_encoder.fit_transform(data['YearOfBirth'])

    x = data[['YearEncoded', 'NameEncoded', 'SexEncoded', 'NumberEncoded']]
    y = data[['YearOfBirth', 'YearEncoded', 'Name', 'NameEncoded', 'Sex', 'SexEncoded', 'Number', 'NumberEncoded']]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(x)

    X_scaled_df = pd.DataFrame(X_scaled, columns=['YearEncoded', 'NameEncoded', 'SexEncoded', 'NumberEncoded'])

    X_scaled_df.to_csv('babyNames_normalized.csv', index=False, header=False, mode='a')

    combined_df = y.copy()
    combined_df[['YearEncoded', 'NameEncoded', 'SexEncoded', 'NumberEncoded']] = X_scaled_df[['YearEncoded', 'NameEncoded', 'SexEncoded', 'NumberEncoded']]

    combined_df.to_csv('babyNames_combined.csv', index=False, mode='a')
    
    
normalizuj()