import pandas as pd
import json
import os

# Load the dirty classes dataset
df = pd.read_csv('datasets-dirty/classes.csv')
df.columns = df.columns.str.strip()

# Initialize two lists
class_metadata = []
class_attributes = []

# Process each row
for index, row in df.iterrows():
    class_id = f"class_{row['id']}"  # Add class_ prefix

    # Save general metadata
    class_metadata.append({

        'id': class_id,
        'name': row['name'],
        'description': row['description'],
        'image': row['image'],  # assuming the column is named 'image'
    })

    # Expand stats
    stats = row['stats']
    if isinstance(stats, str) and stats.startswith("{") and stats.endswith("}"):
        try:
            stats_dict = json.loads(stats.replace("'", '"'))
            for attr, value in stats_dict.items():
                class_attributes.append({
                    'id': class_id,
                    'attribute_type': 'character_stats',
                    'attribute_name': attr.title(),  # Title Case
                    'attribute_value': int(value)  # Ensure integer
                })
        except json.JSONDecodeError as e:
            print(f"Error decoding stats JSON in row {index}: {e}")

# Save the two clean CSVs
pd.DataFrame(class_metadata).to_csv('classes_details.csv', index=False)
pd.DataFrame(class_attributes).to_csv('classes_stats.csv', index=False)

print("✅ Classes data cleaned successfully!")