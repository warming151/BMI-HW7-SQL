import pandas as pd 
import matplotlib.pyplot as plt
import os
import numpy as np

from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import NearestNeighbors


df = pd.read_csv('home/mhuan98/bmihw/bq-results-3.csv')
df = df.sample(frac=1).reset_index(drop=True)
columns = df.columns
#print(columns)
labels = df['aki_stage'].values
#print(labels)
onehot_labels = pd.get_dummies(labels).values
df.drop(['aki_stage','aki_stage_1'],axis=1,inplace=True)


X = df.values

kmeans = KMeans(n_clusters=4, random_state=5).fit(X)
kmeans.labels_
#kmeans.predict([[0, 0], [12, 3]])
kmeans.cluster_centers_
kmeans_result = km.fit_predict(X)
# plt.scatter(X[:, 0], X[:, 1], c=kmeans_result, s=50, cmap='viridis')
# plt.legend()
# plt.savefig('kmean2-1.png')

df_1 = pd.DataFrame([])
X_1  = TSNE(n_components=2, n_iter=250).fit_transform(X)

df_1['tsne1'] = X_embedded[:,0]
df_1['tsne2'] = X_embedded[:,1]
df_1['y'] = kmeans_result
# plt.scatter(X_embedded[:,0], X_embedded[:,1])
sns.scatterplot(
    x="tsne1", y="tsne2",hue="y",
    data=df_1,
    legend="full",
    alpha=0.5,
    save = 'home/mhuan98/bmihw/tsne.pdf'
)


X_train = df.iloc[:round(len(df)*0.6)]
y_train = onehot_labels[:round(len(df)*0.6)]
X_test = df.iloc[round(len(df)*0.6)+1:]
y_test = onehot_labels[round(len(df)*0.6)+1:]
neigh = NearestNeighbors(n_neighbors=2)
neigh.fit(X_train)
NearestNeighbors(n_neighbors=2)
knn1 = neigh.kneighbors_graph(X_train)
knn1.toarray((X_test))
final = knn1.predict




