import pandas as pd

# Load the CSV file
df = pd.read_csv('datasets-dirty/greatRunes.csv')

# Convert 'id' values to strings and prepend 'greatRune_'
df['id'] = 'greatRune_' + df['id'].astype(str)

# Save the updated CSV file
df.to_csv('greatRunes_details.csv', index=False)

print("Column renamed successfully!")