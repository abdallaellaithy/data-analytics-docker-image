import pandas as pd
import numpy as np

# Read the CSV
data = pd.read_csv('/home/doc-bd-a1/updated_data.csv')

# Check for missing values
missing_values = data.isnull().sum()
print(missing_values)

# Data structure
print(data.info())

# Summary statistics
print(data.describe())

# Drop rows with missing values
data.dropna(subset=["Age", "Embarked"], inplace=True)

# Missing values for numerical columns
data["Age"].fillna(data["Age"].mean(), inplace=True)
data["Fare"].fillna(data["Fare"].median(), inplace=True)

# Extract titles from the "Name" column
data['Title'] = data['Name'].str.extract(' ([A-Za-z]+)\.')

# One-Hot Encoding
data = pd.get_dummies(data, columns=["Sex", "Embarked"])

# Drop unnecessary columns
data.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"], inplace=True)

# Save the result
data.to_csv('/home/doc-bd-a1/res_dpre.csv', index=False)

import subprocess
subprocess.run(["python3", "eda.py"])
subprocess.run(["python3", "model.py"])
subprocess.run(["python3", "vis.py"])
