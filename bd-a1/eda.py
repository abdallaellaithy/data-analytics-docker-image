import pandas as pd

# Read the CSV
data = pd.read_csv('/home/doc-bd-a1/res_dpre.csv')

# Insight 1: Age 
age_mean = data['Age'].mean()
age_median = data['Age'].median()
age_std = data['Age'].std()
insight_1 = f"Insight 1: Age Distribution\nMean Age: {age_mean}\nMedian Age: {age_median}\nStandard Deviation of Age: {age_std}"

# Insight 2: Survival Rate
survival_rate = data['Survived'].mean() * 100
insight_2 = f"Insight 2: Survival Rate\nSurvival Rate: {survival_rate:.2f}%"

# Insight 3: Family Size 
data['FamilySize'] = data['SibSp'] + data['Parch']
family_size_counts = data['FamilySize'].value_counts()
insight_3 = f"Insight 3: Family Size Distribution\n{family_size_counts}"

# Save insights to text files
with open('eda-in-1.txt', 'w') as file:
    file.write(insight_1)

with open('eda-in-2.txt', 'w') as file:
    file.write(insight_2)

with open('eda-in-3.txt', 'w') as file:
    file.write(insight_3)
