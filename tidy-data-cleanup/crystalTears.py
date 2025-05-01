import pandas as pd

# Load the CSV file
df = pd.read_csv('datasets-dirty/crystalTears.csv')

# Convert 'id' values to strings and prepend 'crystalTear_'
df['id'] = 'crystalTear_' + df['id'].astype(str)

# Save the updated CSV file
df.to_csv('crystalTears_details.csv', index=False)

print("Column renamed successfully!")