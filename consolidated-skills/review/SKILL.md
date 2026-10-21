---
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
