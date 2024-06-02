import pandas as pd


def merge():

    wynik_df = pd.read_csv('wynik.csv')
    babyNames_combined_df = pd.read_csv('babyNames_combined.csv')

    wynik_df['YearEncoded'] = pd.to_numeric(wynik_df['YearEncoded'], errors='coerce')
    wynik_df['NameEncoded'] = pd.to_numeric(wynik_df['NameEncoded'], errors='coerce')
    wynik_df['SexEncoded'] = pd.to_numeric(wynik_df['SexEncoded'], errors='coerce')

    wynik_df.dropna(subset=['YearEncoded', 'NameEncoded', 'SexEncoded'], inplace=True)

    wynik_df['YearEncoded'] = wynik_df['YearEncoded'].astype('float64')
    wynik_df['NameEncoded'] = wynik_df['NameEncoded'].astype('float64')
    wynik_df['SexEncoded'] = wynik_df['SexEncoded'].astype('float64')
    wynik_df['ClusterNumber'] = wynik_df['ClusterNumber'].astype('int64')

    merged_df = pd.merge(babyNames_combined_df, wynik_df[['YearEncoded', 'NameEncoded', 'SexEncoded', 'ClusterNumber']], 
                        on=['YearEncoded', 'NameEncoded', 'SexEncoded'], how='left')

    merged_df.to_csv('wynik_combined.csv', index=False)


merge()