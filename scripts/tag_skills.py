import json

with open('data/all_skills_full.json', 'r', encoding='utf-8') as f:
    skills = json.load(f)

# Define the target 7 Consolidated Core Work Skills for an enterprise / dev team:
# 1. code-quality-and-review (combines code-review-and-quality, code-simplification, ponytail, security-and-hardening, security-best-practices, systematic-debugging, debugging-and-error-recovery)
# 2. architecture-and-design (combines spec-driven-development, api-and-interface-design, documentation-and-adrs, deprecation-and-migration, planning-and-task-breakdown, doubt-driven-development)
# 3. modern-web-and-frontend (combines frontend-ui-engineering, frontend-design, ui-ux-pro-max, modern-web-guidance, chrome-devtools, a11y-debugging, debug-optimize-lcp, tufte-data-viz)
# 4. context-and-token-efficiency (combines codebase-architecture-reporter, python-code-skeletonizer, dependency-context-collector, git-diff-packager, log-stacktrace-compressor, data-schema-reducer, document-to-markdown, token-usage-router)
# 5. testing-and-devops (combines test-driven-development, ci-cd-and-automation, shipping-and-launch, observability-and-instrumentation, git-workflow-and-versioning, incremental-implementation)
# 6. data-and-analytics-suite (combines bigquery-sql, ml-best-practices, data-autocleaning, schema-mapping, discovering-gcp-data-assets, notebook-guidance)
# 7. agent-workflow-and-ideation (combines idea-refine, interview-me, find-skills, agy-customizations, using-agent-skills)

# Everything else:
# - GameDev (114 skills): Mark as "Archiv / Privat (Nicht für Standard-Arbeitsplatz)"
# - Qt/C++ (22 skills): Mark as "Optionales Spezial-Paket (Desktop Qt)"
# - Pylance internal extensions (24 skills): Mark as "VS Code Intern / Redundant"
# - Exact clones (72 files): Mark as "Zu löschende Duplikate"

consolidation_mapping = {
    "code-quality-and-review": {
        "title": "Code Quality, Review & Debugging Master",
        "description": "Umfassende Code-Reviews, Sicherheitsaudits, Fehlersuche, Code-Vereinfachung und Best Practices in einem konsolidierten Skill.",
        "target_skills": ["code-review-and-quality", "code-simplification", "ponytail", "ponytail-review", "ponytail-audit", 
                          "security-and-hardening", "security-best-practices", "systematic-debugging", "debugging-and-error-recovery", 
                          "pylance-refactoring", "accidental-data-loss-prevention"]
    },
    "architecture-and-design": {
        "title": "Software Architecture, Spec & System Design",
        "description": "Von der Anforderung über Schnittstellen-Design bis hin zu ADRs und Migrationsstrategien.",
        "target_skills": ["spec-driven-development", "api-and-interface-design", "documentation-and-adrs", 
                          "deprecation-and-migration", "planning-and-task-breakdown", "doubt-driven-development", 
                          "source-driven-development", "constraint-driven-development"]
    },
    "modern-web-and-frontend": {
        "title": "Modern Web, UI/UX & Frontend Engineering",
        "description": "High-End Benutzeroberflächen, responsive Layouts, moderne Web-Standards, Accessibility und Chrome DevTools Performance.",
        "target_skills": ["frontend-ui-engineering", "frontend-design", "ui-ux-pro-max", "modern-web-guidance", 
                          "chrome-devtools", "a11y-debugging", "debug-optimize-lcp", "memory-leak-debugging", 
                          "browser-testing-with-devtools", "chrome-extensions", "tufte-data-viz", "design-system"]
    },
    "context-and-token-efficiency": {
        "title": "Context & Token Optimization (JackOfAllTrAIdes Suite)",
        "description": "Drastische Reduktion von LLM-Tokenverbrauch durch AST-Skelettierung, Log-Kompression, Diff-Packaging und Dokumentkonvertierung.",
        "target_skills": ["codebase-architecture-reporter", "python-code-skeletonizer", "dependency-context-collector", 
                          "git-diff-packager", "log-stacktrace-compressor", "data-schema-reducer", "document-to-markdown", 
                          "token-usage-router", "context-engineering", "pdf"]
    },
    "testing-and-devops": {
        "title": "DevOps, CI/CD, Git & Test Automation",
        "description": "Test-Driven Development (TDD), automatisierte Pipelines, Release-Management, Git-Workflows und Observability.",
        "target_skills": ["test-driven-development", "ci-cd-and-automation", "shipping-and-launch", 
                          "observability-and-instrumentation", "git-workflow-and-versioning", "incremental-implementation"]
    },
    "data-and-analytics-suite": {
        "title": "Enterprise Data, SQL & Cloud Analytics",
        "description": "Best Practices für SQL-Optimierung, Datenbereinigung, Schemamapping, Machine Learning und Cloud-Datenbanken.",
        "target_skills": ["bigquery-sql", "bigquery_sql", "bigquery-ai-ml", "bigquery_ai_ml", "bigquery-bigframes", 
                          "bigquery_bigframes", "bigquery-graph", "bigquery_graph", "bigquery-graph-query", 
                          "bigquery-graph-author", "bigtable-basics", "dbt-bigquery", "dataform-bigquery", 
                          "data-autocleaning", "schema-mapping", "discovering-gcp-data-assets", "ml-best-practices", 
                          "notebook-guidance", "federate-lakehouse-catalog", "enforcing-resource-attribution", 
                          "managing-python-dependencies", "dak-setup", "building-data-apps", "resolving-mcp-region-configs"]
    },
    "agent-workflow-and-ideation": {
        "title": "Agent Customization & Ideation Partner",
        "description": "Strukturierte Ideenfindung, Nutzer-Interviews, Custom Agent Configuration und Metaskills.",
        "target_skills": ["idea-refine", "interview-me", "find-skills", "agy-customizations", "antigravity-guide", 
                          "using-agent-skills", "google-antigravity-sdk"]
    }
}

# Tag each skill with relevance and target bundle
enhanced_skills = []
for s in skills:
    s_clean = s['name'].lower().replace('_', '-').strip()
    target_bundle = None
    for bundle_id, bundle_info in consolidation_mapping.items():
        if s_clean in [t.lower().replace('_', '-') for t in bundle_info['target_skills']]:
            target_bundle = bundle_id
            break
            
    # Determine workplace suitability
    if s['domain'] == 'Game Development & Graphics':
        suitability = 'unsuitable_ballast' # Not useful for typical company/enterprise work
        suitability_reason = 'Gaming/Game-Engine spezifisch (Phaser, PyGame, Pixi, Audio/Shader, Platformer etc.). Für Büro-/Entwicklungsarbeit in der Regel Ballast.'
    elif 'vscode-pylance' in s['path'].lower():
        suitability = 'internal_redundant'
        suitability_reason = 'Interne VS Code Extension Kopie - wird direkt von VS Code verwaltet, nicht als manueller Skill benötigt.'
    elif s['domain'] == 'Qt & C++ Development':
        suitability = 'specialized'
        suitability_reason = 'Nur relevant, falls im Team Qt/QML/C++ Desktop-Applikationen entwickelt werden. Sonst als separates Modul auslagern.'
    elif target_bundle:
        suitability = 'high_value'
        suitability_reason = f'Hohe Relevanz für den Arbeitsalltag. Empfohlen für Bündel: {consolidation_mapping[target_bundle]["title"]}'
    else:
        suitability = 'review_needed'
        suitability_reason = 'Einzel-Skill, prüfen ob benötigt oder archivierbar.'
        
    s_copy = dict(s)
    s_copy['target_bundle'] = target_bundle
    s_copy['suitability'] = suitability
    s_copy['suitability_reason'] = suitability_reason
    enhanced_skills.append(s_copy)

with open('data/enhanced_skills.json', 'w', encoding='utf-8') as f:
    json.dump(enhanced_skills, f, indent=2, ensure_ascii=False)

print(f"Enhanced {len(enhanced_skills)} skills with consolidation mapping and suitability tags.")

# Summary statistics
suitability_counts = {}
for s in enhanced_skills:
    suitability_counts[s['suitability']] = suitability_counts.get(s['suitability'], 0) + 1
print("Suitability breakdown:")
for k, v in suitability_counts.items():
    print(f"  - {k}: {v}")
