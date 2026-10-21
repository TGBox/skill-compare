---
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
