import pandas as pd
from sklearn.cluster import KMeans

# Read the CSV
data = pd.read_csv('/home/doc-bd-a1/res_dpre.csv')

data = data.drop(columns=['Title'])

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data)
data['Cluster'] = kmeans.labels_

with open('k.txt', 'w'):
    pass 
for i in range(3):
    value =data['Cluster'].value_counts().values[i] 
    cluster = data['Cluster'].value_counts().keys()[i]
    with open('k.txt', 'a') as file:
        file.write(f'Cluster({cluster}) has: {value}\n')