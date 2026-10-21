---
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
