import pandas as pd

# Load both CSV files
ps5_df = pd.read_csv('metacritic_games_ps5.csv')
xbox_df = pd.read_csv('metacritic_games_xbox.csv')

# Add a platform column if you want to distinguish them
ps5_df['Platform'] = 'PS5'
xbox_df['Platform'] = 'Xbox'

# Merge them
merged_df = pd.concat([ps5_df, xbox_df], ignore_index=True)

# Optional: Rearrange columns if you want 'Platform' earlier
cols = ['Platform'] + [col for col in merged_df.columns if col != 'Platform']
merged_df = merged_df[cols]

# Save the merged file
merged_df.to_csv('metacritic_games_combined.csv', index=False)

print("✅ Merged CSV saved as 'metacritic_games_combined.csv'")