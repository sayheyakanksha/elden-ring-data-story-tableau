import pandas as pd
import json

df = pd.read_csv('datasets-dirty/weapons_upgrades.csv')
df.columns = df.columns.str.strip()

# Mappings
label_map = {
    'Phy': 'Physical', 'Mag': 'Magic', 'Fir': 'Fire', 'Lit': 'Lightning', 'Hol': 'Holy', 'Sta': 'Stamina',
    'Str': 'Strength', 'Dex': 'Dexterity', 'Int': 'Intelligence', 'Fai': 'Faith', 'Arc': 'Arcane',
    'Bst': 'Boost', 'Rst': 'Robustness'
}

def parse_stat_dict(raw_str):
    try:
        cleaned = raw_str.replace("'", '"').replace('–', '0').replace('- ', '0').strip()
        data = json.loads(cleaned)
        return {label_map.get(k.strip(), k.strip()): v.strip().replace('-', '0') for k, v in data.items()}
    except:
        return {}

clean_rows = []

for _, row in df.iterrows():
    id_val = row['id']
    name = row['weapon name']
    upgrade = row['upgrade'].strip()
    passive = parse_stat_dict(row['passive effects']).get('Any', '-')

    attack_power = parse_stat_dict(row['attack power'])
    scaling = parse_stat_dict(row['stat scaling'])
    reduction = parse_stat_dict(row['damage reduction (%)'])

    # Collect all unique stat names across all three
    all_stats = set(attack_power) | set(scaling) | set(reduction)

    for stat in sorted(all_stats):
        clean_rows.append({
            'id': id_val,
            'weapon_name': name,
            'upgrade': upgrade,
            'stat_name': stat,
            'attack_power_value': int(attack_power.get(stat, '0')) if attack_power.get(stat, '0').isdigit() else 0,
            'stat_scaling': scaling.get(stat, '0'),
            'damage_reduction': int(reduction.get(stat, '0')) if reduction.get(stat, '0').isdigit() else 0,
            'passive': passive
        })

# Save to CSV
pd.DataFrame(clean_rows).to_csv('weapons_cleaned.csv', index=False)
print("✅ weapons_cleaned.csv generated.")