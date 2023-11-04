import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV
data = pd.read_csv('/home/doc-bd-a1/res_dpre.csv')

# Create a visualization
pclass_counts = data['Pclass'].value_counts().sort_index()

# Create a bar chart
plt.bar(pclass_counts.index, pclass_counts.values) 

# Set labels and title
plt.xlabel('Pclass')
plt.ylabel('Count')
plt.title('Passengers by Pclass')

plt.savefig('/home/doc-bd-a1/vis.png')