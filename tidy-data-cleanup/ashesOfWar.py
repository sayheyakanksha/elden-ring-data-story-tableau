import pandas as pd

# Load the CSV file
df = pd.read_csv('datasets-dirty/ashesOfWar.csv')

# Convert 'id' values to strings and prepend 'ashofwar_'
df['id'] = 'ashofwar_' + df['id'].astype(str)

# Save the updated CSV file
df.to_csv('ashesOfWar_details.csv', index=False)

print("Column renamed successfully! Saved as 'datasets-clean/ashesOfWar_clean.csv'.")