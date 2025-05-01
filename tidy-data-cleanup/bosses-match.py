import pandas as pd

# Load the CSVs
bosses_df = pd.read_csv('datasets-dirty/bosses.csv')
locations_df = pd.read_csv('boss_locations_details.csv')

# Clean and align names
bosses_df['name'] = bosses_df['name'].str.strip()
locations_df['Boss Name'] = locations_df['Boss Name'].str.strip()

# Create a mapping from boss name to boss_id
name_to_id = dict(zip(locations_df['Boss Name'], locations_df['Boss_id']))

# Map boss_id into bosses_df using the name column
bosses_df['boss_id'] = bosses_df['name'].map(name_to_id)

# Save the updated DataFrame
bosses_df.to_csv('bosses_details_with_boss_id.csv', index=False)

print("✅ boss_id column added to bosses.csv")