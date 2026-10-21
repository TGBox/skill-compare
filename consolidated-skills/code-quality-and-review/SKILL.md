---
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
