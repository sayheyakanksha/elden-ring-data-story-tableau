import pandas as pd

# Load the CSV file
df = pd.read_csv('datasets-dirty/multi.csv')

# Convert 'id' values to strings and prepend 'multiplayer_item_'
df['id'] = 'multiplayer_item_' + df['id'].astype(str)

# Save the updated CSV file
df.to_csv('multi_details.csv', index=False)

print("Column renamed successfully!")