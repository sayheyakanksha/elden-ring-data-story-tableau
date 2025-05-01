import pandas as pd

# Load the CSV file
df = pd.read_csv('datasets-dirty/creatures.csv')

# Convert 'id' values to strings and prepend 'creature_'
df['id'] = 'creature_' + df['id'].astype(str)

# Save the updated CSV file
df.to_csv('creatures_details.csv', index=False)

print("Column renamed successfully!")