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
        "id": "review",
        "title": "review",
        "icon": "shield-check",
        "color": "#10b981", # emerald
        "tagline": "Code-Reviews, Bug-Diagnose, Ponytail-Minimalismus & OWASP-Sicherheit",
        "triggers": "review, code review, audit, debug, check, prüfe, untersuche, fehler finden",
        "summary": "Prüft Code nach dem 5-Achsen-Standard (Korrektheit, Anti-Bloat, Architektur, Sicherheit, Performance) und führt systematische Fehlersuche durch.",
        "skills_included": [
            "code-review-and-quality", "code-simplification", "ponytail", "ponytail-review", 
            "ponytail-audit", "security-and-hardening", "security-best-practices", 
            "systematic-debugging", "debugging-and-error-recovery", "accidental-data-loss-prevention"
        ],
        "benefits": [
            "Kurzer, einprägsamer Befehl: 'review' oder 'prüfe'",
            "Einheitlicher 5-Stufen-Review-Standard für das gesamte Team",
            "Beinhaltet 'Ponytail'-Prinzipien für minimale Lösungen ohne Bloat",
            "Integrierte Root-Cause-Debugging-Methode statt blindem Raten"
        ]
    },
    {
        "id": "spec",
        "title": "spec",
        "icon": "layers",
        "color": "#6366f1", # indigo
        "tagline": "Anforderungen, Schnittstellenverträge (APIs), ADRs & Systemarchitektur",
        "triggers": "spec, architect, design, adr, api contract, entwerfe, spezifikation, architektur, schnittstelle, plane",
        "summary": "Spezifiziert Anforderungen vor dem Coden (Spec-First), fixiert API-Schnittstellen und dokumentiert Architekturentscheidungen (ADRs).",
        "skills_included": [
            "spec-driven-development", "api-and-interface-design", "documentation-and-adrs", 
            "deprecation-and-migration", "planning-and-task-breakdown", "doubt-driven-development", 
            "source-driven-development", "constraint-driven-development"
        ],
        "benefits": [
            "Kurzer Befehl: 'spec' oder 'entwerfe'",
            "Verhindert kostspieliges Refactoring durch vorherige Spezifikation",
            "Strukturierte ADR-Vorlagen für firmeninterne Nachvollziehbarkeit",
            "Schnittstellenverträge (APIs, Interfaces) vor der Code-Erstellung"
        ]
    },
    {
        "id": "ui",
        "title": "ui",
        "icon": "layout",
        "color": "#06b6d4", # cyan
        "tagline": "Modernes Webdesign, responsive Oberflächen, Barrierefreiheit (WCAG) & LCP",
        "triggers": "ui, frontend, web, layout, css, accessibility, devtools, oberfläche, gui, frontend-bau, barrierefrei",
        "summary": "Bündelt moderne Frontend-Entwicklung, responsive Layouts, WCAG 2.1 AA Barrierefreiheit, Chrome DevTools MCP und Core Web Vitals (LCP).",
        "skills_included": [
            "frontend-ui-engineering", "frontend-design", "ui-ux-pro-max", "modern-web-guidance", 
            "chrome-devtools", "a11y-debugging", "debug-optimize-lcp", "memory-leak-debugging", 
            "browser-testing-with-devtools", "chrome-extensions", "tufte-data-viz", "design-system"
        ],
        "benefits": [
            "Ultra-kurz: 'ui' oder 'oberfläche'",
            "Feste Richtlinien für erstklassige Ästhetik (Dark Mode, Typografie, Glassmorphism)",
            "Automatisierte Browser-Audits für Barrierefreiheit und Core Web Vitals",
            "Unterstützt Vollbild- und Fenstermodus (User Rule 4)"
        ]
    },
    {
        "id": "ship",
        "title": "ship",
        "icon": "git-merge",
        "color": "#ec4899", # pink
        "tagline": "Test-Driven Development (TDD), atomare Git-Commits, CI/CD & Deployments",
        "triggers": "ship, test, deploy, git, release, ci-cd, tdd, veröffentliche, teste, liefere, release-plan, pipeline",
        "summary": "Gewährleistet den Red-Green-Refactor Zyklus (TDD), saubere Git-Branching-Strategien, CI/CD-Pipelines und sichere Release-Checklisten.",
        "skills_included": [
            "test-driven-development", "ci-cd-and-automation", "shipping-and-launch", 
            "observability-and-instrumentation", "git-workflow-and-versioning", "incremental-implementation"
        ],
        "benefits": [
            "Handlungsorientiert: 'ship' oder 'veröffentliche'",
            "Schluss mit ungetestetem Code: TDD als fester Standard",
            "Saubere, atomare Git-Commits und Changelogs für das Team",
            "Strukturierte Pre-Flight-Checklisten vor jedem Produktions-Release"
        ]
    },
    {
        "id": "data",
        "title": "data",
        "icon": "database",
        "color": "#3b82f6", # blue
        "tagline": "SQL-Performance-Tuning, dbt/Dataform Pipelines, Schemamapping & Cloud-Daten",
        "triggers": "data, sql, bigquery, dbt, dataform, pipeline, schema, daten, datenbank, abfrage, datenbereinigung",
        "summary": "Die komplette Daten-Suite: High-Performance SQL-Optimierung, Datenbereinigung, dbt/Dataform ELT-Pipelines und sichere Schema-Migrationen.",
        "skills_included": [
            "bigquery-sql", "bigquery-ai-ml", "bigquery-bigframes", "bigquery-graph", 
            "bigquery-graph-query", "bigquery-graph-author", "bigtable-basics", "dbt-bigquery", 
            "dataform-bigquery", "data-autocleaning", "schema-mapping", "discovering-gcp-data-assets", 
            "ml-best-practices", "notebook-guidance", "federate-lakehouse-catalog", 
            "enforcing-resource-attribution", "managing-python-dependencies", "dak-setup", "building-data-apps"
        ],
        "benefits": [
            "Prägnant: 'data' oder 'daten'",
            "Konsolidiert 26 zersplitterte Google Data Agent Kit (DAK) Skills",
            "Vermeidet doppelte Schreibweisen (_ vs -)",
            "Standardisierte Mapping-Manifestos für komplexe Datenmigrationen"
        ]
    },
    {
        "id": "ideate",
        "title": "ideate",
        "icon": "sparkles",
        "color": "#8b5cf6", # purple
        "tagline": "Strukturierte Ideenfindung, Nutzer-Interviews & PRD-One-Pager",
        "triggers": "ideate, refine, interview, brainstorm, scope, stress-test, idee, konzept, anforderung, hinterfrage",
        "summary": "Macht den Agenten zum strategischen Sparringspartner: Hinterfragt unklare Anforderungen (Anti-Yes-Man), leitet Interviews und erstellt One-Pager.",
        "skills_included": [
            "idea-refine", "interview-me", "find-skills", "agy-customizations", 
            "antigravity-guide", "using-agent-skills", "google-antigravity-sdk"
        ],
        "benefits": [
            "Präzise: 'ideate' oder 'idee' (kollisionsfrei mit /plan)",
            "Schärft unpräzise Aufgabenstellungen vor der Code-Implementierung",
            "Verhindert 'Yes-Man'-Verhalten von KI-Modellen durch konstruktives Hinterfragen",
            "Erstellt fertige PRD-One-Pager mit Not-Doing-Listen"
        ]
    },
    {
        "id": "context-and-token-efficiency",
        "title": "Automatische Systemregel (Token & Context)",
        "icon": "cpu",
        "color": "#f59e0b", # amber
        "is_automatic_layer": True,
        "tagline": "Dauerhaft aktiv im Hintergrund (Regel & SessionStart-Hook, kein manueller Aufruf nötig)",
        "triggers": "Automatisch bei jedem Start & Prompt aktiv",
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
