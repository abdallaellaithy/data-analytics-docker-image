import sys
import pandas as pd

# Accept the dataset file path
dataset_path = sys.argv[1]

# Read the dataset
data = pd.read_csv(dataset_path)

# Save the updated data
data.to_csv('/home/doc-bd-a1/updated_data.csv', index=False)

import subprocess
subprocess.run(["python3", "dpre.py"])