import pandas as pd

# Load the CSV file
df = pd.read_csv('datasets-dirty/consumables.csv')

# Convert 'id' values to strings and prepend 'consumable_'
df['id'] = 'consumable_' + df['id'].astype(str)

# Save the updated CSV file
df.to_csv('consumables_details.csv', index=False)

print("Column renamed successfully!")