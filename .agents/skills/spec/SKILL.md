---
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
