# from mlxtend.frequent_patterns import apriori
# from mlxtend.preprocessing import TransactionEncoder
# import pandas as pd

# # Dane
# transakcje = [['B', 'C', 'A'], ['C', 'A'], ['D', 'B'], ['E', 'F', 'A'], ['B', 'C', 'A']]

# # Kodowanie transakcji
# te = TransactionEncoder()
# te_ary = te.fit(transakcje).transform(transakcje)
# df = pd.DataFrame(te_ary, columns=te.columns_)

# # Zastosowanie algorytmu Apriori
# czeste_zbiory = apriori(df, min_support=0.6, use_colnames=True)

# print(czeste_zbiory)


from sklearn import tree
import pandas as pd

# Dane
data = {'BólGłowy': ['Nie', 'Tak', 'Tak', 'Nie', 'Nie', 'Nie'],
        'BólMięśni': ['Tak', 'Nie', 'Tak', 'Tak', 'Nie', 'Tak'],
        'Temperatura': ['Wysoka', 'Wysoka', 'Bardzo wysoka', 'Normalna', 'Wysoka', 'Bardzo wysoka'],
        'Grypa': ['Tak', 'Tak', 'Tak', 'Nie', 'Nie', 'Tak']}
df = pd.DataFrame(data)

# Kodowanie danych
df_encoded = df.apply(lambda x: pd.factorize(x)[0])

# Budowanie drzewa decyzyjnego
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(df_encoded[['BólGłowy', 'BólMięśni', 'Temperatura']], df_encoded['Grypa'])

# Wyświetlanie istotności atrybutów
print(clf.feature_importances_)
