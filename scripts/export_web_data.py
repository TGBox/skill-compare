import json
import os

with open('data/enhanced_skills.json', 'r', encoding='utf-8') as f:
    enhanced_skills = json.load(f)

with open('data/analytics.json', 'r', encoding='utf-8') as f:
    analytics = json.load(f)

# Keep the payload snappy for the web UI by trimming huge full_content into structural sections or storing on demand
web_skills = []
for s in enhanced_skills:
    item = {
        "id": s["id"],
        "name": s["name"],
        "path": s["path"].replace('\\', '/'),
        "parent_dir": s["parent_dir"],
        "source_group": s["source_group"],
        "domain": s["domain"],
        "description": s["description"],
        "line_count": s["line_count"],
        "char_count": s["char_count"],
        "sha256": s["sha256"],
        "headings": s["headings"],
        "content_preview": s["content_preview"],
        "target_bundle": s["target_bundle"],
        "suitability": s["suitability"],
        "suitability_reason": s["suitability_reason"],
        "exact_duplicates": s["exact_duplicates"],
        "name_matches": s["name_matches"]
    }
    web_skills.append(item)

# 7 Master Bundles Definition
bundles = [
    {
        "id": "code-quality-and-review",
        "title": "Code Quality, Review & Debugging Master",
        "icon": "shield-check",
        "color": "#10b981", # emerald
        "tagline": "Qualität, Sicherheit, saubere Architektur und systematische Fehlersuche",
        "summary": "Führt Code-Reviews, Code-Vereinfachung, OWASP/Sicherheitsprüfungen und systematische Root-Cause-Fehleranalyse in einem einzigen mächtigen Skill zusammen.",
        "skills_included": [
            "code-review-and-quality", "code-simplification", "ponytail", "ponytail-review", 
            "ponytail-audit", "security-and-hardening", "security-best-practices", 
            "systematic-debugging", "debugging-and-error-recovery", "accidental-data-loss-prevention"
        ],
        "benefits": [
            "Ersetzt 11 verstreute Review- und Debug-Skills",
            "Einheitlicher 5-Stufen-Review-Standard für das gesamte Team",
            "Beinhaltet 'Ponytail'-Prinzipien für minimale, wartbare Lösungen ohne Bloat",
            "Integrierte Root-Cause-Debugging-Methode statt blindem Raten"
        ]
    },
    {
        "id": "architecture-and-design",
        "title": "Software Architecture, Spec & System Design",
        "icon": "layers",
        "color": "#6366f1", # indigo
        "tagline": "Von der ersten Anforderung über ADRs bis zu zukunftssicheren APIs",
        "summary": "Verbindet Spec-Driven Development, API- und Schnittstellendesign, Architecture Decision Records (ADRs) und Migrationspfade in einem verlässlichen Leitfaden.",
        "skills_included": [
            "spec-driven-development", "api-and-interface-design", "documentation-and-adrs", 
            "deprecation-and-migration", "planning-and-task-breakdown", "doubt-driven-development", 
            "source-driven-development", "constraint-driven-development"
        ],
        "benefits": [
            "Kombiniert 8 getrennte Planungs- und Architektur-Skills",
            "Verhindert kostspieliges Refactoring durch vorherige Spezifikationsprüfung",
            "Strukturierte ADR-Vorlagen für firmeninterne Nachvollziehbarkeit",
            "Schnittstellenverträge (APIs, Interfaces) vor der Code-Erstellung"
        ]
    },
    {
        "id": "modern-web-and-frontend",
        "title": "Modern Web, UI/UX & Frontend Engineering",
        "icon": "layout",
        "color": "#06b6d4", # cyan
        "tagline": "High-End Benutzeroberflächen, State-of-the-Art Webstandards & UX",
        "summary": "Bündelt moderne Frontend-Architektur, responsive UI/UX-Designprinzipien, Accessibility (WCAG), Chrome DevTools MCP-Automatisierung und Web Vitals (LCP)-Optimierung.",
        "skills_included": [
            "frontend-ui-engineering", "frontend-design", "ui-ux-pro-max", "modern-web-guidance", 
            "chrome-devtools", "a11y-debugging", "debug-optimize-lcp", "memory-leak-debugging", 
            "browser-testing-with-devtools", "chrome-extensions", "tufte-data-viz", "design-system"
        ],
        "benefits": [
            "Ersetzt 12 Frontend- und DevTools-Einzeltools",
            "Feste Richtlinien für erstklassige Ästhetik (Dark Mode, Typografie, Glassmorphism)",
            "Automatisierte Browser-Audits für Barrierefreiheit und Core Web Vitals",
            "Datenvisualisierung nach Tufte-Standards für Berichte und Dashboards"
        ]
    },
    {
        "id": "context-and-token-efficiency",
        "title": "Automatische Kontext- & Token-Regel (System-Layer)",
        "icon": "cpu",
        "color": "#f59e0b", # amber
        "is_automatic_layer": True,
        "tagline": "Dauerhaft aktiv im Hintergrund (Regel & SessionStart-Hook, kein manueller Aufruf nötig)",
        "summary": "Aufgrund des Nutzer-Feedbacks aus der manuellen Skill-Liste herausgelöst: Greift als globale Regel (rules/context-and-token-efficiency.md) und automatischer SessionStart-Hook bei jedem Projektstart und jedem Prompt völlig selbstständig.",
        "skills_included": [
            "codebase-architecture-reporter", "python-code-skeletonizer", "dependency-context-collector", 
            "git-diff-packager", "log-stacktrace-compressor", "data-schema-reducer", "document-to-markdown", 
            "token-usage-router", "context-engineering", "pdf"
        ],
        "benefits": [
            "Vollautomatisch aktiv: Kein Mitarbeiter muss daran denken, einen Skill aufzurufen",
            "Verhindert Token-Verschwendung BEVOR große Dateien geladen werden",
            "Einmaliger SessionStart-Hook erfasst die Repo-Architektur beim Öffnen des Projekts",
            "Spart bis zu 85% Token im Kontextfenster ohne jegliche manuelle Interaktion"
        ]
    },
    {
        "id": "testing-and-devops",
        "title": "DevOps, CI/CD, Git & Test Automation",
        "icon": "git-merge",
        "color": "#ec4899", # pink
        "tagline": "Zuverlässige Deployments, Test-Driven Development & Git-Exzellenz",
        "summary": "Kombiniert den Red-Green-Refactor Zyklus (TDD), automatisierte CI/CD-Pipelines, strukturierte Git-Branching-Strategien, Observability (Logging/Metriken) und Deployment-Rollouts.",
        "skills_included": [
            "test-driven-development", "ci-cd-and-automation", "shipping-and-launch", 
            "observability-and-instrumentation", "git-workflow-and-versioning", "incremental-implementation"
        ],
        "benefits": [
            "Schluss mit ungetestetem Code: TDD als fester Standard",
            "Saubere, atomare Git-Commits und Changelogs für das Team",
            "Strukturierte Pre-Flight-Checklisten vor jedem Produktions-Release",
            "Inkrementelle Implementierung verhindert Monster-Pull-Requests"
        ]
    },
    {
        "id": "data-and-analytics-suite",
        "title": "Enterprise Data, SQL & Cloud Analytics",
        "icon": "database",
        "color": "#3b82f6", # blue
        "tagline": "SQL-Performance, Datenbereinigung, Schemamapping & Cloud-Pipelines",
        "summary": "Die komplette Enterprise-Suite für Daten-Profis: High-Performance SQL-Tuning, automatisierte Datenbereinigung, dbt/Dataform ELT-Pipelines, ML-Best-Practices und GCP-Datenbanken.",
        "skills_included": [
            "bigquery-sql", "bigquery-ai-ml", "bigquery-bigframes", "bigquery-graph", 
            "bigquery-graph-query", "bigquery-graph-author", "bigtable-basics", "dbt-bigquery", 
            "dataform-bigquery", "data-autocleaning", "schema-mapping", "discovering-gcp-data-assets", 
            "ml-best-practices", "notebook-guidance", "federate-lakehouse-catalog", 
            "enforcing-resource-attribution", "managing-python-dependencies", "dak-setup", "building-data-apps"
        ],
        "benefits": [
            "Konsolidiert 26 zersplitterte Google Data Agent Kit (DAK) Skills",
            "Vermeidet doppelte Schreibweisen (_ vs -)",
            "Standardisierte Mapping-Manifestos für komplexe Datenmigrationen",
            "Sichere Python- und SQL-Ausführung nach Unternehmensstandards"
        ]
    },
    {
        "id": "agent-workflow-and-ideation",
        "title": "Agent Customization & Ideation Partner",
        "icon": "sparkles",
        "color": "#8b5cf6", # purple
        "tagline": "Strukturierte Ideenfindung, Nutzerbedürfnisse & KI-Führung",
        "summary": "Verwandelt den KI-Assistenten in einen strategischen Denkpartner: Divergente/konvergente Ideenverfeinerung, Nutzer-Interviews, Customizations (Rules/Skills) und Metasteuerung.",
        "skills_included": [
            "idea-refine", "interview-me", "find-skills", "agy-customizations", 
            "antigravity-guide", "using-agent-skills", "google-antigravity-sdk"
        ],
        "benefits": [
            "Schärft unpräzise Aufgabenstellungen vor der Code-Implementierung",
            "Verhindert 'Yes-Man'-Verhalten von KI-Modellen durch konstruktives Hinterfragen",
            "Einfaches Onboarding neuer Kollegen in das Antigravity/Gemini-Ökosystem",
            "Zentraler Einstiegspunkt für die Steuerung aller anderen Skills"
        ]
    }
]

os.makedirs('web', exist_ok=True)

# Write js data bundle
js_content = f"""// Auto-generated skill intelligence data bundle
window.SKILL_DATA = {{
    skills: {json.dumps(web_skills, ensure_ascii=False)},
    analytics: {json.dumps(analytics, ensure_ascii=False)},
    bundles: {json.dumps(bundles, ensure_ascii=False)}
}};
"""

with open('web/data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Generated web/data.js with {len(web_skills)} skills, analytics and 7 consolidated bundles.")
