import pandas as pd
import json

# Load the CSV
df = pd.read_csv('datasets-dirty/weapons.csv')
df.columns = df.columns.str.strip()  # Clean column names

# Lists to store tidy data
weapon_metadata = []
weapon_attributes = []

# Process each row
for index, row in df.iterrows():
    weapon_id = f"weapon_{row['id']}"  # Standardize ID

    # Save general metadata
    weapon_metadata.append({
        'id': weapon_id,
        'weapon_id': row['weapon_id'],
        'name': row['name'],
        'image': row['image'],
        'weight': row['weight'],
        'description': row['description'],
        'dlc': row['dlc'],
        'damage_type': row['damage type'],
        'category': row['category'],
        'passive_effect': row['passive effect'],
        'skill': row['skill'],
        'FP cost': row['FP cost']
    })

    # Expand 'requirements' JSON-like string
    requirements = row['requirements']
    if isinstance(requirements, str) and requirements.startswith("{") and requirements.endswith("}"):
        try:
            req_dict = json.loads(requirements.replace("'", '"'))  # Convert single to double quotes
            for attr_name, attr_value in req_dict.items():
                weapon_attributes.append({
                    'id': weapon_id,
                    'attribute_type': 'weapon_requirements',
                    'attribute_name': attr_name,
                    'attribute_value': int(attr_value)
                })
        except json.JSONDecodeError as e:
            print(f"❌ Error decoding requirements in row {index}: {e}")

# Save outputs
pd.DataFrame(weapon_metadata).to_csv('weapons_details.csv', index=False)
pd.DataFrame(weapon_attributes).to_csv('weapons_stats.csv', index=False)

print("✅ Weapons data cleaned successfully!")
print("Metadata saved as 'weapons_metadata.csv'.")
print("Attributes saved as 'weapons_attributes.csv'.")