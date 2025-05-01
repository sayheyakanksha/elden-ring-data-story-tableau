import pandas as pd

# Load the CSV file
df = pd.read_csv('datasets-dirty/cookbooks.csv')

# Convert 'id' values to strings and prepend 'cookbook_'
df['id'] = 'cookbook_' + df['id'].astype(str)

# Save the updated CSV file
df.to_csv('cookbooks_details.csv', index=False)

print("Column renamed successfully!")