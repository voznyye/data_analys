from sklearn.cluster import KMeans
import pandas as pd
import plotly.express as px
import numpy as np
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

def elbow():
    matplotlib.use('agg')
    # Load the normalized data
    normalized_df = pd.read_csv('babyNames_normalized.csv')

    # Remove non-numeric columns if any
    numeric_df = normalized_df.select_dtypes(include=[np.number])

    # Determine the optimal number of clusters using the Elbow method
    wcss = []
    silhouette_scores = []
    cluster_range = range(5, 9)

    for n_clusters in cluster_range:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10, max_iter=10)
        kmeans.fit(numeric_df)
        print('1 done')
        
        # Within-cluster sum of squares
        wcss.append(kmeans.inertia_)
        print('2 done')
        
        # Silhouette score
        cluster_labels = kmeans.labels_
        silhouette_avg = silhouette_score(numeric_df, cluster_labels)
        silhouette_scores.append(silhouette_avg)
        print('3 done')

    # Plot the Elbow method results
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(cluster_range, wcss, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS')

    # Plot the Silhouette scores
    plt.subplot(1, 2, 2)
    plt.plot(cluster_range, silhouette_scores, marker='o')
    plt.title('Silhouette Scores')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Silhouette Score')

    plt.tight_layout()
    plt.savefig('analiz.png')



def visual():

    # Load the updated CSV file
    merged_df = pd.read_csv('wynik_combined.csv')

    # Create a scatter plot
    fig = px.scatter(merged_df, 
                    x='YearOfBirth', 
                    y='Number', 
                    color='ClusterNumber',
                    hover_data=['Name', 'Sex', 'Number'],
                    title='Number of Births by Year and Cluster')
    

    # Save the figure as a PNG file
    # fig.write_image("plot.png")

    # Show the plot
    fig.show()


# visual()
elbow()