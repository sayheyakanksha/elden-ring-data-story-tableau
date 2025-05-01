import pandas as pd

# Load the CSV file
df = pd.read_csv('datasets-dirty/talismans.csv')

# Convert 'id' values to strings and prepend 'talisman_'
df['id'] = 'talisman_' + df['id'].astype(str)

# Save the updated CSV file
df.to_csv('talismans_details.csv', index=False)

print("Column renamed successfully!")