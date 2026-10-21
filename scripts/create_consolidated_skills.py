import os

os.makedirs('consolidated-skills', exist_ok=True)

SKILLS = {
    "code-quality-and-review": {
        "name": "code-quality-and-review",
        "title": "Code Quality, Review & Debugging Master",
        "description": "All-in-one skill for professional code quality: multi-axis code reviews, systematic root-cause debugging, minimalist 'ponytail' refactoring, security hardening (OWASP), and accidental data loss prevention.",
        "content": """---
name: code-quality-and-review
description: Comprehensive standard for software quality, multi-axis code review, systematic root-cause debugging, minimalist refactoring (ponytail principle), and security hardening.
---

# Code Quality, Review & Debugging Master

A unified, production-grade skill designed for software engineering teams. It combines rigorous multi-axis review, systematic debugging, defensive security, and ruthless minimalism.

## 1. Multi-Axis Code Review (The 5 Dimensions)
Before any code is accepted or merged, evaluate across five distinct axes:

1. **Correctness & Edge Cases**:
   - Does the logic behave correctly under boundary conditions (null, empty, negative, concurrent access)?
   - Are error states handled explicitly without swallowing exceptions?
2. **Readability & Simplicity (The Ponytail Rule)**:
   - Question every abstraction. Prefer standard library solutions over external dependencies.
   - 10 lines of clear code beat 50 lines of speculative boilerplate.
   - Delete dead flexibility, unneeded helper wrappers, and premature generalizations.
3. **Architecture & Consistency**:
   - Does this fit into existing repository patterns?
   - Are interfaces decoupled and single-responsibility?
4. **Security & Data Safety**:
   - Input validation and parameterized queries (SQL injection prevention).
   - Strict XSS / SSRF defense and secrets isolation.
   - **Accidental Data Loss Gate**: Never run broad DELETE without WHERE, DROP TABLE, or irreversible file wipes without explicit confirmation.
5. **Performance & Resource Hygiene**:
   - Avoid N+1 queries, memory leaks, unclosed streams/file handles.
   - Minimize computational complexity in hot paths.

## 2. Systematic Root-Cause Debugging Workflow
Never guess or apply blind trial-and-error fixes. Follow the 4-phase debugging protocol:

1. **Reproduce & Isolate**:
   - Identify the exact minimal trigger and input data that reproduces the failure.
   - Formulate a reproducible test case or script.
2. **Trace & Hypothesize**:
   - Inspect call stacks and sanitize logs. Trace variable states from entry to error.
   - State an explicit hypothesis: "The bug occurs because component X receives Y instead of Z."
3. **Verify Hypothesis**:
   - Prove the hypothesis with targeted assertion or breakpoint before modifying implementation code.
4. **Fix at Root & Add Regression Test**:
   - Fix the underlying defect, not just the symptom.
   - Add an automated test that fails before the fix and passes after.

## 3. Minimalist Refactoring Guide
- **YAGNI (You Aren't Gonna Need It)**: Do not add hooks, generic type parameters, or configuration flags for future use-cases that do not currently exist.
- Standard Library first: Native language features (e.g., standard collections, native fetch, built-in string methods) before adding npm/pip packages.
- Leave a clean trail: Document non-obvious design decisions with concise comments in English.
"""
    },
    "software-architecture-and-specs": {
        "name": "software-architecture-and-specs",
        "title": "Software Architecture, Spec & System Design",
        "description": "Guides system architecture from requirement specification to API design contracts, Architecture Decision Records (ADRs), adversarial stress-testing, and database schema migrations.",
        "content": """---
name: software-architecture-and-specs
description: End-to-end framework for system architecture, specification-driven development, stable API contracts, Architecture Decision Records (ADRs), and safe schema migrations.
---

# Software Architecture, Spec & System Design

This skill provides an engineering standard for defining, designing, and maintaining robust software systems before code is written.

## 1. Specification-Driven Development (Spec-First)
Do not jump straight into code when requirements are complex or ambiguous:
1. **Clarify Objective & User Persona**: Who is this for and what concrete problem does it solve?
2. **Capability Decomposition**: Break requirements into a capability matrix of independent, testable modules.
3. **Define In-Scope vs. Not-Doing**:
   - Clearly delineate what will *not* be supported in this iteration. The "Not-Doing" list prevents feature creep.
4. **Acceptance Criteria**: Define measurable criteria for done.

## 2. API & Interface Contract Design
1. **Contract Before Implementation**:
   - Define type schemas, endpoints, request/response models before backend or frontend logic is written.
   - Ensure backward compatibility. Never break existing clients without deprecation phases.
2. **Naming & Conventions**:
   - Use predictable resource-oriented URLs (REST) or strongly typed GraphQL/RPC schemas.
   - Use ISO-8601 for dates and standard status codes.

## 3. Architecture Decision Records (ADRs)
When making architectural choices with trade-offs, record them in `docs/adr/YYYY-MM-DD-decision-title.md`:
- **Context**: What problem forced the decision?
- **Options Considered**: Alternative approaches evaluated.
- **Decision & Rationale**: Why the chosen approach won.
- **Consequences**: Positive outcomes and acknowledged downsides/trade-offs.

## 4. Adversarial Stress-Testing (Doubt-Driven)
Cross-examine architectural proposals:
- Where is the single point of failure?
- What happens when network latency spikes or a dependency is unavailable?
- How does the system scale under a 10x traffic increase?
- What migration path is needed if a database column or table is renamed (Expand/Contract pattern)?
"""
    },
    "modern-web-and-ui": {
        "name": "modern-web-and-ui",
        "title": "Modern Web, UI/UX & Frontend Engineering",
        "description": "Standard for creating visually stunning, accessible, high-performance web applications with vanilla CSS/JS, dark mode, Chrome DevTools profiling, and responsive layouts.",
        "content": """---
name: modern-web-and-ui
description: Professional web development and UI/UX design: semantic HTML5, modern vanilla CSS tokens, WCAG 2.1 AA accessibility, Chrome DevTools performance audits, and sleek aesthetics.
---

# Modern Web, UI/UX & Frontend Engineering

A design and engineering standard for creating web applications that wow users with visual excellence, fluid interactivity, and flawless performance.

## 1. Visual Aesthetics & Design System
- **Curated Color Palettes**: Sleek dark modes with deep slate/indigo backgrounds, tailored HSL accents, and glassmorphic panels (`backdrop-filter: blur(12px)`).
- **Modern Typography**: Clear font hierarchy using Google Fonts (Inter, Outfit, Roboto) with proportional line-heights and letter-spacing.
- **Subtle Micro-Animations**: Smooth transitions on hover, modal open/close animations, and dynamic state feedback.
- **Windowed & Fullscreen Modes**: Always provide a fullscreen toggle button alongside windowed mode for dashboard and data apps.

## 2. Accessible Semantic Markup (WCAG 2.1 AA)
- Single `<h1>` per page with hierarchical `<h2>`-`<h6>` structure.
- All interactive elements must have clear focus rings, unique IDs, and keyboard navigation support.
- Proper contrast ratios (minimum 4.5:1 for regular text, 3:1 for large text).
- Correct ARIA attributes (`aria-label`, `aria-expanded`, `aria-hidden`) where semantic HTML alone is insufficient.

## 3. Web Performance & Core Web Vitals
- **LCP (Largest Contentful Paint)**: Minimize critical render-blocking CSS/JS, optimize image assets, and use inline critical styles.
- **INP (Interaction to Next Paint)**: Avoid long tasks on the main thread; debounce search inputs; use CSS transforms for animations.
- **Zero Layout Shift (CLS)**: Always reserve dimensions for images, banners, and dynamic containers.
- **Tufte Data Visualization**: High data-ink ratio, legible axis markers, and direct labeling without cluttered legends.
"""
    },
    "context-and-token-efficiency": {
        "name": "context-and-token-efficiency",
        "title": "Context & Token Optimization (JackOfAllTrAIdes Suite)",
        "description": "Meta-skill for drastic reduction of LLM token consumption: AST skeletonization, repository architecture mapping, import tracing, log compression, and schema reduction.",
        "content": """---
name: context-and-token-efficiency
description: Slash LLM token usage and prevent context overflow using AST code skeletonization, log compression, diff packaging, document-to-markdown conversion, and schema reduction.
---

# Context & Token Optimization Suite

This skill provides token compression techniques to maximize coding productivity while minimizing token consumption, context exhaustion, and API costs.

## 1. Token Reduction Tools & Techniques
1. **Python / JS AST Skeletonizer**:
   - Extract structural interfaces (class definitions, function signatures, docstrings, type annotations) while stripping method bodies.
   - Gives the LLM 100% of the API contract at 10% of the token cost.
2. **Codebase Architecture Reporter**:
   - Scans directories and produces a compact module dependency tree and summary instead of feeding entire source files.
3. **Log & Stacktrace Compressor**:
   - Strips repeating log entries, removes ANSI terminal color codes, collapses internal framework stack frames, and isolates the root cause line.
4. **Data Schema Reducer**:
   - Converts large JSON payloads, SQL table dumps, or CSV files into a compact schema with 2 sample rows instead of thousands of records.
5. **Document to Markdown Converter**:
   - Extracts plain text and tables from PDFs, DOCX, and Jupyter Notebooks, stripping styling bloat and base64 image strings.

## 2. Context Engineering Rules
- Never paste an entire 2,000-line file when only a 30-line function is being modified.
- Use slice viewing (`StartLine` / `EndLine`) when inspecting files.
- Package git diffs with structural skeletons before requesting reviews.
"""
    },
    "devops-testing-and-git": {
        "name": "devops-testing-and-git",
        "title": "DevOps, CI/CD, Git & Test Automation",
        "description": "Best practices for Test-Driven Development (TDD), atomic Git commits, release branching, CI/CD pipelines, and observability.",
        "content": """---
name: devops-testing-and-git
description: Complete standard for Test-Driven Development (TDD), atomic Git version control, CI/CD deployment pipelines, and structured observability.
---

# DevOps, CI/CD, Git & Test Automation

A disciplined software delivery framework ensuring that code is continuously tested, cleanly versioned, and reliably deployed.

## 1. Test-Driven Development (TDD)
Follow the Red-Green-Refactor cycle:
1. **Red**: Write a failing unit or integration test that precisely defines the expected behavior.
2. **Green**: Write the minimal amount of code necessary to make the test pass.
3. **Refactor**: Clean up the implementation, eliminate duplication, and verify tests remain green.

## 2. Git Workflow & Versioning
- **Atomic Commits**: Each commit must represent a single logical change with a descriptive message following Conventional Commits (`feat:`, `fix:`, `refactor:`, `test:`, `docs:`).
- **Clean Branching**: Use feature branches with short lifespans. Rebase onto main to maintain linear, readable history.
- **Changelog & Semantic Versioning**: Increment SemVer numbers (`MAJOR.MINOR.PATCH`) intentionally based on backward compatibility.

## 3. CI/CD & Launch Readiness
- Automated quality gates: Linters, type checkers, and test suites must pass before merge.
- Pre-flight launch checklist:
  - Database migration tested on staging.
  - Environment variables and secrets configured.
  - Rollback plan verified.
- **Observability**: Structured JSON logging, health-check endpoints, and key performance metrics (error rate, response latency).
"""
    },
    "enterprise-data-and-sql": {
        "name": "enterprise-data-and-sql",
        "title": "Enterprise Data, SQL & Cloud Analytics",
        "description": "Standard for high-performance SQL query optimization, data cleaning pipelines (dbt/Dataform), schema mapping manifestos, and cloud data governance.",
        "content": """---
name: enterprise-data-and-sql
description: Enterprise data engineering standard: SQL performance tuning, automated data cleaning, dbt/Dataform transformation pipelines, and schema mapping.
---

# Enterprise Data, SQL & Cloud Analytics

A comprehensive data engineering standard consolidating best practices for SQL performance, cloud data warehouses (BigQuery, PostgreSQL), and ETL/ELT pipelines.

## 1. High-Performance SQL Optimization
- **Prune Early**: Filter rows with `WHERE` and select only necessary columns before performing joins. Avoid `SELECT *`.
- **Partitioning & Clustering**: Always leverage partition and cluster keys to prevent expensive full-table scans.
- **Join Hygiene**: Join smaller dimension tables against larger fact tables; avoid cartesian cross-joins.
- **Window Functions**: Prefer window functions (`ROW_NUMBER()`, `DENSE_RANK()`) over self-joins.

## 2. Data Pipelines & ELT (dbt / Dataform)
- **Modular Data Modeling**:
  - `stg_` (Staging): Clean raw ingested data with uniform naming and types.
  - `int_` (Intermediate): Business logic aggregations and joins.
  - `fct_` / `dim_` (Marts): Curated fact and dimension tables for analytics.
- **Data Quality & Testing**: Enforce `not_null`, `unique`, and referential integrity tests on all primary keys.

## 3. Schema Mapping & Migration Manifesto
Before migrating data across schemas:
1. Document source-to-target field mappings with explicit type casting.
2. Define transformation logic for null, missing, or malformed records.
3. Validate row counts and checksums post-migration.
"""
    },
    "agent-workflow-and-ideation": {
        "name": "agent-workflow-and-ideation",
        "title": "Agent Customization & Ideation Partner",
        "description": "Strategic thinking framework for divergent/convergent ideation, requirement interviewing, agent customization, and rule orchestration.",
        "content": """---
name: agent-workflow-and-ideation
description: Master framework for ideation, requirement clarification, anti-yes-man stress-testing, and AI assistant customization.
---

# Agent Customization & Ideation Partner

This skill turns the AI into a sharp strategic thinking partner, preventing premature coding and aligning on clear user intent.

## 1. Divergent & Convergent Ideation (The 3 Phases)
### Phase 1: Understand & Expand (Divergent)
- Reframe the challenge into a sharp **"How Might We"** problem statement.
- Ask 3-5 sharpening questions to identify target users, real constraints, and success criteria.
- Explore 5-8 variations across distinct innovation lenses (Inversion, Constraint Removal, Extreme Simplification, Scale).

### Phase 2: Evaluate & Converge
- Cluster ideas into 2-3 distinct strategic directions.
- Stress-test against:
  - **User Value**: Painkiller vs. vitamin?
  - **Feasibility**: Real cost, technical friction, and maintenance burden.
  - **Differentiation**: What makes this genuinely superior?
- **Surface Hidden Assumptions**: Name what you are betting on and what could kill the project.

### Phase 3: Sharpen & Ship (The One-Pager)
Produce a clear one-pager containing:
- Problem Statement
- Recommended Direction
- Key Assumptions to Validate
- MVP Scope
- **The "Not Doing" List** (the most valuable part: deliberate trade-offs)
- Open Questions

## 2. Agent Customization Best Practices
- Keep rule files (`GEMINI.md`, `AGENTS.md`) focused and enforceable.
- Prefer explicit behavior contracts over vague guidance.
- Regularly audit installed skills to prune duplicates and domain ballast.
"""
    }
}

for skill_id, skill_data in SKILLS.items():
    skill_dir = os.path.join('consolidated-skills', skill_id)
    os.makedirs(skill_dir, exist_ok=True)
    file_path = os.path.join(skill_dir, 'SKILL.md')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(skill_data['content'].strip() + '\n')
    print(f"Created consolidated skill: {file_path}")

print("All 7 consolidated skills successfully created.")
