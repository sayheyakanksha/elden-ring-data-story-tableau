import pandas as pd

# Load the CSV file
df = pd.read_csv('datasets-dirty/materials.csv')

# Convert 'id' values to strings and prepend 'material_'
df['id'] = 'material_' + df['id'].astype(str)

# Save the updated CSV file
df.to_csv('materials_details.csv', index=False)

print("Column renamed successfully!")