import pandas as pd

# Load the CSV file
df = pd.read_csv('datasets-dirty/remembrances.csv')

# Convert 'id' values to strings and prepend 'remembrance_'
df['id'] = 'remembrance_' + df['id'].astype(str)

# Save the updated CSV file
df.to_csv('remembrances_details.csv', index=False)

print("Column renamed successfully!")