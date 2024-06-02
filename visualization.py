from sklearn.cluster import KMeans
import pandas as pd
import plotly.express as px
import numpy as np
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import matplotlib

def elbow():
    matplotlib.use('agg')
    normalized_df = pd.read_csv('babyNames_normalized.csv')

    numeric_df = normalized_df.select_dtypes(include=[np.number])

    wcss = []
    silhouette_scores = []
    cluster_range = range(2, 5)

    for n_clusters in cluster_range:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10, max_iter=10)
        kmeans.fit(numeric_df)
        print('1 done')
        
        wcss.append(kmeans.inertia_)
        print('2 done')
        
        cluster_labels = kmeans.labels_
        silhouette_avg = silhouette_score(numeric_df, cluster_labels)
        silhouette_scores.append(silhouette_avg)
        print('3 done')

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(cluster_range, wcss, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS')

    plt.subplot(1, 2, 2)
    plt.plot(cluster_range, silhouette_scores, marker='o')
    plt.title('Silhouette Scores')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Silhouette Score')

    plt.tight_layout()
    plt.savefig('analiz1.png')



def visual_matplotlib():
    matplotlib.use('agg')
    merged_df = pd.read_csv('wynik_combined.csv')
    
    plt.figure(figsize=(16, 10))
    plt.scatter(merged_df['YearEncoded'], merged_df['Number'], c=merged_df['ClusterNumber'])
    plt.colorbar(label='Cluster Number')
    plt.xlabel('Name Encoded')
    plt.ylabel('Year Encoded')
    plt.title('Scatter Plot of Names by Year and Cluster')
    plt.savefig('scatter_plot.png')


def visual_plotly():
    merged_df = pd.read_csv('wynik_combined.csv')
    
    fig = px.scatter(merged_df, 
                     x='Number', 
                     y='Name', 
                     color='ClusterNumber',
                     hover_data=['YearOfBirth', 'Name', 'Sex', 'Number', 'ClusterNumber'],
                     title='Number of Births by Year and Cluster')
    
    fig.write_image("plot2.png")




# visual_plotly()
visual_matplotlib()