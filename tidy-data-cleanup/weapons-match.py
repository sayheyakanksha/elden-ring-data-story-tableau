import pandas as pd

# Load both files
details_df = pd.read_csv('weapons_details.csv')
cleaned_df = pd.read_csv('weapons_cleaned.csv')

# Strip extra whitespace
details_df['name'] = details_df['name'].str.strip()
cleaned_df['weapon_name'] = cleaned_df['weapon_name'].str.strip()

# Merge on name
merged_df = cleaned_df.merge(details_df[['id', 'name']], left_on='weapon_name', right_on='name', how='left')

# Drop duplicate 'name' column from right table
merged_df = merged_df.drop(columns=['name'])

# Optional: move id to first column
cols = ['id'] + [col for col in merged_df.columns if col != 'id']
merged_df = merged_df[cols]

# Save the final output
merged_df.to_csv('weapons_cleaned_with_id.csv', index=False)

print("✅ Merged weapon ID into weapons_cleaned.csv.")