import pandas as pd
import json
import os

# Load the CSV
df = pd.read_csv('datasets-dirty/ammos.csv')
df.columns = df.columns.str.strip()  # Clean column names

# Initialize two lists
ammo_metadata = []
ammo_attributes = []

# Process each row
for index, row in df.iterrows():
    ammo_id = f"ammo_{row['id']}"  # Add ammo_ prefix

    # Save general metadata
    ammo_metadata.append({
        'id': ammo_id,
        'name': row['name'],
        'description': row['description'],
        'image': row['image'],  # assuming the column is named 'image'
        'type': row['type'],
        'damage_type': row['damage type'],
        'passive_effect': row['passive effect'],
        'dlc': row['dlc']
    })

    # Expand attack power JSON
    attack_power = row['attack power']
    if isinstance(attack_power, str) and attack_power.startswith("{") and attack_power.endswith("}"):
        try:
            attack_dict = json.loads(attack_power.replace("'", '"'))  # Safe JSON load

            for attr, value in attack_dict.items():
                ammo_attributes.append({
                    'id': ammo_id,
                    'attribute_type': 'attack_power',
                    'attribute_name': attr,
                    'attribute_value': int(value)  # Cast value from str to int
                })

        except json.JSONDecodeError as e:
            print(f"Error decoding attack power JSON in row {index}: {e}")

# Save outputs
pd.DataFrame(ammo_metadata).to_csv('ammos_details.csv', index=False)
pd.DataFrame(ammo_attributes).to_csv('ammos_stats.csv', index=False)

print("✅ Data cleaned successfully!")
print("Metadata saved as 'ammos_details.csv'.")
print("Attributes saved as 'ammos_stats.csv'.")