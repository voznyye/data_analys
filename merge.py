import pandas as pd


def merge():

    # Load the CSV files
    wynik_df = pd.read_csv('wynik.csv')
    babyNames_combined_df = pd.read_csv('babyNames_combined.csv')

    # Remove non-numeric values in the relevant columns in wynik_df
    # and convert them to numeric types
    wynik_df['YearEncoded'] = pd.to_numeric(wynik_df['YearEncoded'], errors='coerce')
    wynik_df['NameEncoded'] = pd.to_numeric(wynik_df['NameEncoded'], errors='coerce')
    wynik_df['SexEncoded'] = pd.to_numeric(wynik_df['SexEncoded'], errors='coerce')

    # Drop rows with NaN values after conversion
    wynik_df.dropna(subset=['YearEncoded', 'NameEncoded', 'SexEncoded'], inplace=True)

    # Convert columns to the appropriate data types
    wynik_df['YearEncoded'] = wynik_df['YearEncoded'].astype('float128')
    wynik_df['NameEncoded'] = wynik_df['NameEncoded'].astype('float128')
    wynik_df['SexEncoded'] = wynik_df['SexEncoded'].astype('float128')
    wynik_df['ClusterNumber'] = wynik_df['ClusterNumber'].astype('int64')

    # Merge the DataFrames on 'YearOfBirth', 'NameEncoded', and 'SexEncoded'
    merged_df = pd.merge(babyNames_combined_df, wynik_df[['YearEncoded', 'NameEncoded', 'SexEncoded', 'ClusterNumber']], 
                        on=['YearEncoded', 'NameEncoded', 'SexEncoded'], how='left')

    # Save the updated DataFrame to a new CSV file
    merged_df.to_csv('wynik_combined.csv', index=False)


merge()