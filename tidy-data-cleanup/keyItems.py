import pandas as pd

# Load the CSV file
df = pd.read_csv('datasets-dirty/keyItems.csv')

# Convert 'id' values to strings and prepend 'keyItem_'
df['id'] = 'keyItem_' + df['id'].astype(str)

# Save the updated CSV file
df.to_csv('keyItems_details.csv', index=False)

print("Column renamed successfully!")