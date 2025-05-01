import pandas as pd

# Load the CSV file
df = pd.read_csv('datasets-dirty/tools.csv')

# Convert 'id' values to strings and prepend 'bell_'
df['id'] = 'tool_' + df['id'].astype(str)

# Save the updated CSV file
df.to_csv('tools_details.csv', index=False)

print("Column renamed successfully!")