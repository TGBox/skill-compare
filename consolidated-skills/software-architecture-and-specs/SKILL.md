---
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
