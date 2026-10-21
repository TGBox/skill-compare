---
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
