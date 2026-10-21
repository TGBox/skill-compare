import os
import shutil
import json

SHORT_SKILLS = {
    "review": {
        "title": "Review (Code Quality & Security)",
        "tagline": "Prüfe Code, finde Bugs, härte Sicherheit & streiche Bloat",
        "description": "Multi-axis code review, systematic root-cause debugging, minimalist 'ponytail' refactoring, and security hardening (OWASP). Trigger phrases: review, code review, audit, debug, check, prüfe, untersuche, fehler finden.",
        "skills_included": [
            "code-review-and-quality", "code-simplification", "ponytail", "ponytail-review", 
            "security-and-hardening", "systematic-debugging", "accidental-data-loss-prevention"
        ],
        "content": """---
name: review
description: Comprehensive standard for code review, root-cause debugging, minimalist refactoring (ponytail principle), and security hardening. Use on 'review', 'code review', 'check', 'debug', 'audit', or German: 'prüfe', 'untersuche', 'code-review', 'fehler finden'.
---

# Review: Code Quality, Debugging & Security

A fast, action-oriented engineering standard for reviewing code, diagnosing defects, eliminating complexity, and hardening security.

## Trigger-Keywords / Aufruf
- **English:** `review`, `code review`, `audit`, `debug`, `check`, `simplify`
- **Deutsch:** `prüfe`, `untersuche`, `code-review`, `sicherheitsaudit`, `fehler finden`, `vereinfache`

---

## 1. Multi-Axis Review Protocol (The 5 Dimensions)
Evaluate any change across five clear dimensions:

1. **Correctness & Edge Cases**:
   - Check boundary conditions (null, empty, negative, concurrent access).
   - Ensure explicit error handling without swallowing exceptions.
2. **Simplicity & Anti-Bloat (The Ponytail Rule)**:
   - Question every abstraction. Prefer standard library solutions over new external dependencies.
   - 10 lines of clean code beat 50 lines of speculative boilerplate. Delete dead flexibility.
3. **Architecture & Consistency**:
   - Adhere to established project patterns and decouple single-responsibility interfaces.
4. **Security & Data Safety**:
   - Parameterized queries (SQL injection defense), input sanitization (XSS/SSRF), secret isolation.
   - **Accidental Data Loss Gate:** Never run broad DELETE without WHERE, DROP TABLE, or destructive wipes without explicit user confirmation.
5. **Performance & Resource Hygiene**:
   - Prevent N+1 queries, memory leaks, and unclosed file/network streams.

---

## 2. Systematic Root-Cause Debugging (4 Steps)
Never guess or apply blind trial-and-error fixes:
1. **Reproduce:** Isolate the exact minimal trigger and input data that reproduces the defect.
2. **Trace & Hypothesize:** Sanitize stacktraces and formulate an explicit hypothesis (*"Component X receives Y instead of Z"*).
3. **Verify:** Prove the hypothesis with targeted assertions before changing business logic.
4. **Fix & Test:** Fix the underlying defect and add an automated regression test.
"""
    },
    "spec": {
        "title": "Spec (Architecture & System Design)",
        "tagline": "Spezifiziere Anforderungen, APIs, ADRs & Migrationen",
        "description": "Specification-driven development (Spec-First), stable API design contracts, Architecture Decision Records (ADRs), and schema migrations. Trigger phrases: spec, architect, design, adr, api contract, entwerfe, plane, architektur, spezifikation.",
        "skills_included": [
            "spec-driven-development", "api-and-interface-design", "documentation-and-adrs", 
            "deprecation-and-migration", "planning-and-task-breakdown", "doubt-driven-development"
        ],
        "content": """---
name: spec
description: End-to-end framework for system architecture, specification-driven development, API contracts, Architecture Decision Records (ADRs), and safe schema migrations. Use on 'spec', 'architect', 'design', 'adr', 'contract', or German: 'entwerfe', 'spezifikation', 'architektur', 'schnittstelle', 'plane'.
---

# Spec: Architecture, APIs & System Design

An action-driven framework to clarify requirements, lock in API contracts, and document architectural decisions before writing code.

## Trigger-Keywords / Aufruf
- **English:** `spec`, `architect`, `design`, `api contract`, `adr`, `decompose`
- **Deutsch:** `entwerfe`, `spezifikation`, `architektur`, `schnittstelle`, `api-vertrag`, `plane-system`

---

## 1. Specification-Driven Development (Spec-First)
Before coding complex or ambiguous features:
1. **Clarify Objective & Persona:** Define who this is for and the exact problem it solves.
2. **Capability Decomposition:** Break requirements into a matrix of independent, testable modules.
3. **Define In-Scope vs. Not-Doing:** Explicitly state what will *not* be built to prevent feature creep.
4. **Acceptance Criteria:** Write measurable criteria for definition of done.

---

## 2. API & Interface Contract Design
1. **Contract Before Logic:** Define schemas, request/response models, and status codes first.
2. **Predictable Conventions:** Use resource-oriented endpoints (REST) or strongly typed RPC schemas.
3. **Backward Compatibility:** Never break existing consumers without a formal deprecation phase.

---

## 3. Architecture Decision Records (ADRs)
Record non-trivial decisions in `docs/adr/YYYY-MM-DD-decision-title.md`:
- **Context:** What forced the decision?
- **Options Considered:** Alternatives evaluated.
- **Decision & Rationale:** Why the winning approach was selected.
- **Consequences:** Positive outcomes and acknowledged trade-offs.
"""
    },
    "ui": {
        "title": "UI (Frontend, UX & Web Performance)",
        "tagline": "Baue responsive Oberflächen, barrierefreies Web & schnelle Ladezeiten",
        "description": "Frontend UI engineering, accessible HTML5/CSS, WCAG 2.1 AA, sleek dark modes, DevTools MCP automation, and Core Web Vitals (LCP). Trigger phrases: ui, frontend, web, style, accessibility, oberfläche, frontend-bau, barrierefrei, webseite.",
        "skills_included": [
            "frontend-ui-engineering", "frontend-design", "ui-ux-pro-max", "modern-web-guidance", 
            "chrome-devtools", "a11y-debugging", "debug-optimize-lcp", "tufte-data-viz"
        ],
        "content": """---
name: ui
description: Professional frontend development and UI/UX design: semantic HTML5, modern vanilla CSS tokens, WCAG 2.1 AA accessibility, Chrome DevTools performance audits, and sleek aesthetics. Use on 'ui', 'frontend', 'web', 'css', 'design', or German: 'oberfläche', 'gui', 'frontend-bau', 'webseite', 'barrierefrei'.
---

# UI: Modern Web, UX & Frontend Engineering

A design and frontend engineering standard for building state-of-the-art web interfaces with fluid interactivity, rich dark aesthetics, and flawless performance.

## Trigger-Keywords / Aufruf
- **English:** `ui`, `frontend`, `web`, `layout`, `css`, `accessibility`, `devtools`
- **Deutsch:** `oberfläche`, `gui`, `frontend-bau`, `webseite`, `barrierefrei`, `gestalte`

---

## 1. Visual Aesthetics & Design System
- **Curated Palette:** Deep slate/navy dark themes (`#0a0e17`), tailored HSL accents, and subtle glassmorphic panels (`backdrop-filter: blur(12px)`).
- **Modern Typography:** Clear font hierarchy with Google Fonts (Inter, Outfit, Roboto) and proportional line-heights.
- **Subtle Micro-Animations:** Fluid transitions on hover, modal open/close transitions, and visual feedback.
- **Windowed & Fullscreen Modes (User Rule 4):** Always provide a fullscreen toggle alongside windowed mode for dashboards and complex tools.

---

## 2. Accessible Semantic Markup (WCAG 2.1 AA)
- Single `<h1>` per page with hierarchical heading structure.
- Keyboard navigation: clear focus rings, unique IDs, and keyboard event handlers.
- Minimum contrast ratio: 4.5:1 for regular text, 3:1 for large text.
- Meaningful ARIA attributes where semantic HTML alone is insufficient.

---

## 3. Web Performance & Core Web Vitals
- **LCP (Largest Contentful Paint):** Inline critical styles, defer non-essential scripts, optimize hero elements.
- **INP (Interaction to Next Paint):** Avoid blocking the main thread; debounce search/filter inputs.
- **Tufte Data Visualization:** High data-ink ratio, legible axis markers, and direct labeling without cluttered legends.
"""
    },
    "ship": {
        "title": "Ship (DevOps, Testing & Git)",
        "tagline": "Teste automatisiert, committe sauber & release zuverlässig",
        "description": "Test-Driven Development (TDD), atomic Git commits, release branching, CI/CD pipelines, and observability. Trigger phrases: ship, test, deploy, ci-cd, git, release, teste, veröffentliche, liefere, pipeline.",
        "skills_included": [
            "test-driven-development", "ci-cd-and-automation", "shipping-and-launch", 
            "observability-and-instrumentation", "git-workflow-and-versioning", "incremental-implementation"
        ],
        "content": """---
name: ship
description: Disciplined delivery standard: Test-Driven Development (TDD), atomic Git commits, CI/CD deployment pipelines, and structured observability. Use on 'ship', 'test', 'deploy', 'git', 'ci-cd', 'release', or German: 'veröffentliche', 'teste', 'liefere', 'release-plan', 'pipeline'.
---

# Ship: DevOps, Testing & Git Delivery

A disciplined delivery standard ensuring software is rigorously tested, cleanly versioned, and reliably shipped.

## Trigger-Keywords / Aufruf
- **English:** `ship`, `test`, `deploy`, `git`, `release`, `ci-cd`, `tdd`
- **Deutsch:** `veröffentliche`, `teste`, `liefere`, `git-workflow`, `release-plan`, `pipeline`

---

## 1. Test-Driven Development (TDD)
Execute the Red-Green-Refactor loop:
1. **Red:** Write a failing unit or integration test defining expected behavior.
2. **Green:** Write the minimal implementation required to make the test pass.
3. **Refactor:** Clean up code, eliminate duplication, and verify tests remain green.

---

## 2. Git Workflow & Versioning
- **Atomic Commits:** Each commit represents a single logical change following Conventional Commits (`feat:`, `fix:`, `refactor:`, `test:`, `docs:`).
- **Linear History:** Rebase feature branches to keep commit graphs readable.
- **Semantic Versioning (SemVer):** Increment `MAJOR.MINOR.PATCH` intentionally based on backward compatibility.

---

## 3. CI/CD & Launch Readiness
- Automated quality gates: linters, type checks, and tests must pass prior to merge.
- Pre-flight checklist: staging verification, environment secrets configured, rollback strategy verified.
- **Observability:** Structured JSON logging, health-check endpoints, and key telemetry metrics.
"""
    },
    "data": {
        "title": "Data (SQL, Pipelines & Analytics)",
        "tagline": "Optimiere SQL, baue Pipelines, mappe Schemas & bereinige Daten",
        "description": "High-performance SQL query tuning, data cleaning pipelines (dbt/Dataform), schema mapping manifestos, and cloud data governance. Trigger phrases: data, sql, bigquery, dbt, pipeline, daten, datenbank, abfrage, datenbereinigung.",
        "skills_included": [
            "bigquery-sql", "bigquery-ai-ml", "bigquery-bigframes", "dbt-bigquery", 
            "dataform-bigquery", "data-autocleaning", "schema-mapping", "discovering-gcp-data-assets"
        ],
        "content": """---
name: data
description: Enterprise data engineering: SQL performance tuning, automated data cleaning, dbt/Dataform pipelines, and schema mapping. Use on 'data', 'sql', 'bigquery', 'dbt', 'database', 'pipeline', or German: 'daten', 'datenbank', 'abfrage', 'datenbereinigung', 'schema-mapping'.
---

# Data: SQL, Pipelines & Cloud Analytics

An enterprise standard for high-performance SQL, data transformations (dbt/Dataform), and robust schema mapping.

## Trigger-Keywords / Aufruf
- **English:** `data`, `sql`, `bigquery`, `dbt`, `dataform`, `pipeline`, `schema`
- **Deutsch:** `daten`, `datenbank`, `abfrage`, `datenbereinigung`, `schema-mapping`, `analytik`

---

## 1. High-Performance SQL Optimization
- **Prune Early:** Filter rows with `WHERE` and select only necessary columns before joins. Never use `SELECT *`.
- **Partitioning & Clustering:** Always filter by partition/cluster keys to prevent expensive full-table scans.
- **Join Hygiene:** Join smaller dimension tables against larger fact tables; avoid cartesian cross-joins.
- **Window Functions:** Use window functions (`ROW_NUMBER()`, `DENSE_RANK()`) over costly self-joins.

---

## 2. Modular Data Pipelines (dbt / Dataform)
- `stg_` (Staging): Clean raw ingested data with uniform column types and names.
- `int_` (Intermediate): Business logic aggregations and joins.
- `fct_` / `dim_` (Marts): Curated fact and dimension tables ready for reporting.
- Enforce `not_null`, `unique`, and referential integrity tests on all primary keys.

---

## 3. Schema Mapping & Migration Manifesto
Before migrating datasets:
1. Document source-to-target field mappings with explicit type casting.
2. Define transformation logic for null, missing, or malformed records.
3. Validate row counts and checksums post-migration.
"""
    },
    "ideate": {
        "title": "Ideate (Clarify, Refine & Plan)",
        "tagline": "Schärfe Anforderungen, hinterfrage Annahmen & plane PRD-One-Pager",
        "description": "Strategic ideation framework: divergent exploration (7 lenses), convergent evaluation, user interview technique, and PRD one-pager creation. Trigger phrases: ideate, refine, interview, brainstorm, scope, idee, anforderung, konzept, hinterfrage.",
        "skills_included": [
            "idea-refine", "interview-me", "find-skills", "agy-customizations", "using-agent-skills"
        ],
        "content": """---
name: ideate
description: Strategic thinking partner: divergent/convergent ideation, requirement interviewing, anti-yes-man stress-testing, and PRD one-pagers. Use on 'ideate', 'refine', 'interview', 'scope', 'brainstorm', or German: 'idee', 'konzept', 'anforderung', 'hinterfrage', 'ideenfindung'.
---

# Ideate: Requirements, Strategic Refinement & Scope

A thinking-partner framework to challenge assumptions, extract true user intent, and produce sharp, buildable concepts before writing code.

## Trigger-Keywords / Aufruf
- **English:** `ideate`, `refine`, `interview`, `brainstorm`, `scope`, `stress-test`
- **Deutsch:** `idee`, `konzept`, `anforderung`, `hinterfrage`, `ideenfindung`, `schärfe-plan`

---

## 1. The 3 Ideation Phases
### Phase 1: Understand & Expand (Divergent)
- Reframe the challenge into a crisp **"How Might We"** problem statement.
- Ask 3-5 sharpening questions (target user, success criteria, real constraints).
- Explore 5-8 variations across lenses (Inversion, Constraint Removal, Radical Simplification, Scale).

### Phase 2: Evaluate & Converge
- Cluster ideas into 2-3 distinct strategic directions.
- Stress-test against User Value (painkiller vs vitamin), Feasibility, and Differentiation.
- **Surface Hidden Assumptions:** Name what you are betting on and what could kill the project.

### Phase 3: Sharpen & Ship (The One-Pager)
Produce a concrete one-pager containing:
- Problem Statement
- Recommended Direction
- Key Assumptions to Validate
- MVP Scope
- **The "Not Doing" List (deliberate trade-offs)**
- Open Questions

---

## 2. Anti-Yes-Man Culture
- Actively push back on speculative complexity.
- Challenge vague requests with friendly, direct inquiries until intent is ~95% clear.
"""
    }
}

def deploy_short_skills():
    print("Deploying the 6 short Master-Skills...")
    
    # 1. Project canonical: consolidated-skills/
    for skill_name, data in SHORT_SKILLS.items():
        skill_dir = os.path.join("consolidated-skills", skill_name)
        os.makedirs(skill_dir, exist_ok=True)
        file_path = os.path.join(skill_dir, "SKILL.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(data["content"].strip() + "\n")
        print(f"  [consolidated-skills] -> {file_path}")

    # Remove any old long-named folders in consolidated-skills
    old_names = [
        "code-quality-and-review", "software-architecture-and-specs", 
        "modern-web-and-ui", "devops-testing-and-git", 
        "enterprise-data-and-sql", "agent-workflow-and-ideation"
    ]
    for old in old_names:
        old_dir = os.path.join("consolidated-skills", old)
        if os.path.exists(old_dir):
            shutil.rmtree(old_dir)
            print(f"  Removed obsolete folder: {old_dir}")

    # 2. Team template: .agents/skills/
    team_agents_skills = os.path.join(".agents", "skills")
    os.makedirs(team_agents_skills, exist_ok=True)
    for skill_name, data in SHORT_SKILLS.items():
        target_dir = os.path.join(team_agents_skills, skill_name)
        os.makedirs(target_dir, exist_ok=True)
        with open(os.path.join(target_dir, "SKILL.md"), "w", encoding="utf-8") as f:
            f.write(data["content"].strip() + "\n")
        print(f"  [.agents/skills] -> {target_dir}/SKILL.md")

    # Copy rules and hooks to .agents/
    os.makedirs(".agents/rules", exist_ok=True)
    shutil.copy("rules/context-and-token-efficiency.md", ".agents/rules/context-and-token-efficiency.md")
    shutil.copy("hooks/hooks.json", ".agents/hooks.json")
    print("  [.agents/rules & hooks] -> copied context-and-token-efficiency.md & hooks.json")

    # 3. Global installation (Parallel-Betrieb): C:\Users\DaniBani\.gemini\config\skills
    global_skills_dir = r"C:\Users\DaniBani\.gemini\config\skills"
    if os.path.exists(global_skills_dir):
        for skill_name, data in SHORT_SKILLS.items():
            target_dir = os.path.join(global_skills_dir, skill_name)
            os.makedirs(target_dir, exist_ok=True)
            with open(os.path.join(target_dir, "SKILL.md"), "w", encoding="utf-8") as f:
                f.write(data["content"].strip() + "\n")
            print(f"  [Global config/skills] -> {target_dir}/SKILL.md")

    # Deploy global rule to C:\Users\DaniBani\.gemini\config\rules
    global_rules_dir = r"C:\Users\DaniBani\.gemini\config\rules"
    os.makedirs(global_rules_dir, exist_ok=True)
    shutil.copy("rules/context-and-token-efficiency.md", os.path.join(global_rules_dir, "context-and-token-efficiency.md"))
    print(f"  [Global config/rules] -> {global_rules_dir}/context-and-token-efficiency.md")

    print("\nAll 6 Master-Skills successfully deployed globally and locally!")

if __name__ == "__main__":
    deploy_short_skills()
