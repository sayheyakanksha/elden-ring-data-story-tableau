import pandas as pd
import json
import os

# Load the dirty armor dataset
df = pd.read_csv('datasets-dirty/armors.csv')
df.columns = df.columns.str.strip()

# Initialize two lists
armor_metadata = []
armor_attributes = []

# Process each row
for index, row in df.iterrows():
    armor_id = f"armor_{row['id']}"  # Add armor_ prefix

    # Save general metadata
    armor_metadata.append({
        'id': armor_id,
        'name': row['name'],
        'description': row['description'],
        'image': row['image'],  # assuming the column is named 'image'
        'type': row['type'],
        'weight': row['weight'],
        'special_effect': row['special effect'],
        'how_to_acquire': row['how to acquire'],
        'in_game_section': row['in-game section'],
        'dlc': row['dlc']


    })

    # Expand damage negation
    damage_negation = row['damage negation']
    if isinstance(damage_negation, str) and damage_negation.startswith("[{") and damage_negation.endswith("}]"):
        try:
            dn_dict_list = json.loads(damage_negation.replace("'", '"'))
            if isinstance(dn_dict_list, list) and len(dn_dict_list) > 0:
                for attr, value in dn_dict_list[0].items():
                    armor_attributes.append({
                        'id': armor_id,
                        'attribute_type': 'damage_negation',
                        'attribute_name': attr,
                        'attribute_value': float(value)
                    })
        except json.JSONDecodeError as e:
            print(f"Error decoding damage negation JSON in row {index}: {e}")

    # Expand resistance
    resistance = row['resistance']
    if isinstance(resistance, str) and resistance.startswith("[") and resistance.endswith("]"):
        try:
            res_dict_list = json.loads(resistance.replace("'", '"'))
            if isinstance(res_dict_list, list) and len(res_dict_list) > 0:
                for attr, value in res_dict_list[0].items():
                    armor_attributes.append({
                        'id': armor_id,
                        'attribute_type': 'resistance',
                        'attribute_name': attr,
                        'attribute_value': int(value)
                    })
        except json.JSONDecodeError as e:
            print(f"Error decoding resistance JSON in row {index}: {e}")

# Ensure output folder exists
os.makedirs('datasets-clean', exist_ok=True)

# Save the two clean CSVs
pd.DataFrame(armor_metadata).to_csv('armors_details.csv', index=False)
pd.DataFrame(armor_attributes).to_csv('armors_stats.csv', index=False)

print("✅ Armors data cleaned successfully!")
print("Metadata saved as 'armors_details.csv'.")
print("Attributes saved as 'armors_attributes.csv'.")