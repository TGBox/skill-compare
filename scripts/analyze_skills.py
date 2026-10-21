import json
import collections
from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

with open('data/all_skills_full.json', 'r', encoding='utf-8') as f:
    skills = json.load(f)

print(f"Total skills scanned: {len(skills)}")

# 1. Group by SHA256 (Exact file duplicates)
hash_groups = collections.defaultdict(list)
for s in skills:
    hash_groups[s['sha256']].append(s)

exact_dupes = {h: slist for h, slist in hash_groups.items() if len(slist) > 1}
total_exact_dupe_files = sum(len(slist) for slist in exact_dupes.values())
unique_exact_dupe_concepts = len(exact_dupes)

print(f"\n--- 1. EXACT DUPLICATES (Identical content) ---")
print(f"Number of groups with identical files: {unique_exact_dupe_concepts}")
print(f"Total redundant file instances: {total_exact_dupe_files - unique_exact_dupe_concepts}")

# 2. Normalized Name Collisions
name_groups = collections.defaultdict(list)
for s in skills:
    norm_name = s['name'].lower().replace('_', '-').strip()
    name_groups[norm_name].append(s)

name_collisions = {name: slist for name, slist in name_groups.items() if len(slist) > 1}
print(f"\n--- 2. NAME COLLISIONS (Same name, potentially differing paths/contents) ---")
print(f"Skills sharing the same normalized name: {len(name_collisions)}")

# 3. Source Distribution
source_counts = collections.Counter(s['source_group'] for s in skills)
print(f"\n--- 3. SOURCE DISTRIBUTION ---")
for src, count in source_counts.most_common():
    print(f"  - {src}: {count}")

# 4. Domain Distribution
domain_counts = collections.Counter(s['domain'] for s in skills)
print(f"\n--- 4. DOMAIN DISTRIBUTION ---")
for dom, count in domain_counts.most_common():
    print(f"  - {dom}: {count}")

# 5. Overlapping & High Similarity Pairs (Content / Description)
print(f"\n--- 5. HIGH SEMANTIC / FUNCTIONAL OVERLAP ---")
# Check description similarity among distinct names
similar_pairs = []
for i in range(len(skills)):
    for j in range(i + 1, len(skills)):
        s1 = skills[i]
        s2 = skills[j]
        if s1['sha256'] == s2['sha256']:
            continue
        # Check description similarity
        if s1['description'] and s2['description']:
            sim = similarity(s1['description'], s2['description'])
            if sim > 0.65:
                similar_pairs.append({
                    "skill1": s1['name'],
                    "path1": s1['path'],
                    "skill2": s2['name'],
                    "path2": s2['path'],
                    "similarity": round(sim, 3)
                })

print(f"Found {len(similar_pairs)} pairs with description similarity > 65% (distinct files)")

# Save analytical breakdown to JSON
analytics = {
    "total_count": len(skills),
    "exact_duplicate_groups": [
        {
            "hash": h,
            "count": len(slist),
            "name": slist[0]['name'],
            "instances": [{"id": s['id'], "path": s['path'], "source": s['source_group']} for s in slist]
        }
        for h, slist in exact_dupes.items()
    ],
    "name_collision_groups": [
        {
            "name": name,
            "count": len(slist),
            "instances": [{"id": s['id'], "path": s['path'], "source": s['source_group'], "sha256": s['sha256']} for s in slist]
        }
        for name, slist in name_collisions.items()
    ],
    "source_distribution": dict(source_counts),
    "domain_distribution": dict(domain_counts),
    "similar_pairs": similar_pairs[:50]
}

with open('data/analytics.json', 'w', encoding='utf-8') as f:
    json.dump(analytics, f, indent=2, ensure_ascii=False)

print("\nAnalytics saved to data/analytics.json")
