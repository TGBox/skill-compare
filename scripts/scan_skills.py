import os
import re
import json
import hashlib
from pathlib import Path

# Paths to search for skills
SEARCH_PATHS = [
    r"C:\Users\DaniBani\.gemini\config",
    r"C:\Users\DaniBani\.gemini\antigravity\builtin\skills",
    r"C:\Users\DaniBani\.gemini\antigravity-ide\builtin\skills",
    r"C:\Users\DaniBani\.ollama\skills",
    r"C:\Users\DaniBani\.vscode\extensions",
    r"C:\Users\DaniBani\Documents\VisualStudioCodeProjects\awesome-gamedev-agent-skills",
    r"C:\Users\DaniBani\Documents\VisualStudioCodeProjects\JackOfAllTrAIdes"
]

def parse_frontmatter(content):
    """Extract YAML frontmatter if present."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return {}, content
    
    fm_text = match.group(1)
    body = content[match.end():]
    data = {}
    for line in fm_text.splitlines():
        if ':' in line:
            key, val = line.split(':', 1)
            data[key.strip()] = val.strip().strip('"').strip("'")
    return data, body

def determine_source_group(filepath):
    """Categorize the origin of the skill."""
    fp = filepath.replace('\\', '/').lower()
    if 'plugins/agent-skills' in fp:
        return 'agent-skills (Plugin)'
    if 'plugins/data-agent-kit-plugin' in fp:
        return 'data-agent-kit (Plugin)'
    if 'plugins/chrome-devtools-plugin' in fp:
        return 'chrome-devtools (Plugin)'
    if 'plugins/modern-web-guidance' in fp:
        return 'modern-web-guidance (Plugin)'
    if 'plugins/ponytail' in fp:
        return 'ponytail (Plugin)'
    if 'plugins/qt-development-skills' in fp:
        return 'qt-development-skills (Plugin)'
    if 'plugins/google-antigravity-sdk' in fp:
        return 'google-antigravity-sdk (Plugin)'
    if 'builtin' in fp:
        return 'Gemini / Antigravity Built-in'
    if '.vscode/extensions' in fp:
        return 'VS Code Extensions (Pylance)'
    if '.ollama' in fp:
        return 'Ollama Skills'
    if 'awesome-gamedev-agent-skills' in fp:
        return 'Awesome GameDev Repo'
    if 'jackofalltraides' in fp:
        return 'JackOfAllTrAIdes Repo'
    if '.gemini/config/skills' in fp:
        return 'Global Customizations (.gemini/config/skills)'
    return 'Other'

def classify_skill_domain(name, desc, body):
    """Determine the functional domain of the skill."""
    text = (name + " " + desc + " " + body[:1000]).lower()
    
    # Game dev
    game_keywords = ['game', 'phaser', 'pixijs', 'pygame', 'godot', 'unity', 'unreal', 'fps', 
                     'roguelike', 'rpg', 'shader', 'level design', 'camera', 'coyote time', 
                     'audio bus', 'itch.io', 'steam', 'dialogue', 'tower defense', 'puzzle']
    if any(k in text for k in game_keywords) and 'data' not in name:
        return 'Game Development & Graphics'
        
    # BigQuery / Data / Cloud
    data_keywords = ['bigquery', 'dbt', 'dataform', 'spanner', 'bigtable', 'lakehouse', 
                     'gcp', 'data cleaning', 'machine learning', 'ml-best-practices', 'sql']
    if any(k in text for k in data_keywords) or 'bigquery' in name or 'data' in name:
        return 'Data Engineering & Cloud (GCP/SQL)'
        
    # Qt / C++
    qt_keywords = ['qt', 'qml', 'cmake', 'c++']
    if any(k in text for k in qt_keywords) or 'qt-' in name:
        return 'Qt & C++ Development'
        
    # Web / Frontend / UI
    web_keywords = ['web', 'html', 'css', 'frontend', 'chrome', 'browser', 'devtools', 
                    'lcp', 'a11y', 'accessibility', 'ui-ux', 'tufte']
    if any(k in text for k in web_keywords) or 'chrome-' in name:
        return 'Frontend, Web & UI/UX'
        
    # Token & Context Optimization
    token_keywords = ['token', 'context', 'compress', 'skeletonizer', 'packager', 
                      'reducer', 'architecture-reporter']
    if any(k in text for k in token_keywords) or 'token' in name:
        return 'Context & Token Optimization'
        
    # Core Engineering & Quality / Architecture
    meta_keywords = ['spec', 'test-driven', 'review', 'debugging', 'ci-cd', 'security', 
                     'hardening', 'git-workflow', 'api-and-interface', 'doubt', 'ponytail']
    if any(k in text for k in meta_keywords):
        return 'Software Architecture, Quality & Review'
        
    return 'General & Workflow'

def scan_all_skills():
    found_files = []
    seen_paths = set()
    
    for search_root in SEARCH_PATHS:
        if not os.path.exists(search_root):
            continue
        for root, dirs, files in os.walk(search_root):
            # Skip git and cache
            if '.git' in root or '__pycache__' in root or 'node_modules' in root:
                continue
            for f in files:
                if f.lower() == 'skill.md':
                    full_p = os.path.normpath(os.path.join(root, f))
                    if full_p not in seen_paths:
                        seen_paths.add(full_p)
                        found_files.append(full_p)
                        
    skills = []
    content_hashes = {}
    name_to_skills = {}
    
    for fp in found_files:
        try:
            with open(fp, 'r', encoding='utf-8', errors='replace') as file:
                content = file.read()
        except Exception as e:
            continue
            
        sha256 = hashlib.sha256(content.encode('utf-8')).hexdigest()
        fm, body = parse_frontmatter(content)
        
        # Name inference
        name = fm.get('name')
        if not name:
            # Try to grab first H1
            h1 = re.search(r'^#\s+(.+)$', body, re.MULTILINE)
            if h1:
                name = h1.group(1).strip()
            else:
                # Use parent directory name
                name = os.path.basename(os.path.dirname(fp))
                
        # Description inference
        desc = fm.get('description', '')
        if not desc:
            # Grab first paragraph
            paras = [p.strip() for p in body.split('\n\n') if p.strip() and not p.strip().startswith('#')]
            if paras:
                desc = paras[0][:300]
                
        # Extract headings
        headings = re.findall(r'^(#{1,3})\s+(.+)$', body, re.MULTILINE)
        heading_titles = [h[1].strip() for h in headings]
        
        source_group = determine_source_group(fp)
        domain = classify_skill_domain(name, desc, body)
        line_count = len(content.splitlines())
        char_count = len(content)
        
        skill_entry = {
            "id": hashlib.md5(fp.encode('utf-8')).hexdigest()[:10],
            "name": name,
            "path": fp,
            "filename": os.path.basename(fp),
            "parent_dir": os.path.basename(os.path.dirname(fp)),
            "source_group": source_group,
            "domain": domain,
            "description": desc,
            "line_count": line_count,
            "char_count": char_count,
            "sha256": sha256,
            "headings": heading_titles[:15],
            "content_preview": body[:800],
            "full_content": content
        }
        
        skills.append(skill_entry)
        
        # Register for duplicate detection
        if sha256 not in content_hashes:
            content_hashes[sha256] = []
        content_hashes[sha256].append(skill_entry["id"])
        
        clean_name = name.lower().replace('_', '-').strip()
        if clean_name not in name_to_skills:
            name_to_skills[clean_name] = []
        name_to_skills[clean_name].append(skill_entry["id"])

    # Mark exact duplicates
    for s in skills:
        s["exact_duplicates"] = [sid for sid in content_hashes[s["sha256"]] if sid != s["id"]]
        clean_name = s["name"].lower().replace('_', '-').strip()
        s["name_matches"] = [sid for sid in name_to_skills[clean_name] if sid != s["id"]]

    return skills

if __name__ == '__main__':
    print("Scanning skills...")
    skills = scan_all_skills()
    print(f"Total skills parsed: {len(skills)}")
    
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    # Save full data (without huge full_content in the summary json to keep it fast, but keep in data/all_skills.json)
    with open('data/all_skills_full.json', 'w', encoding='utf-8') as f:
        json.dump(skills, f, indent=2, ensure_ascii=False)
        
    # Lean version for UI
    lean_skills = []
    for s in skills:
        lean_s = dict(s)
        del lean_s['full_content'] # Keep payload lightweight for web app
        lean_skills.append(lean_s)
        
    with open('data/skills_summary.json', 'w', encoding='utf-8') as f:
        json.dump(lean_skills, f, indent=2, ensure_ascii=False)
        
    print("Saved data/all_skills_full.json and data/skills_summary.json successfully.")
