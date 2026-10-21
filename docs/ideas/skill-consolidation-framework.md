# Skill Consolidation Framework: Von 268 zersplitterten Skills zu 7 produktiven Master-Skills

## Problem Statement

*Wie können wir die 268 verstreuten, redundanten Skills auf dem PC so untersuchen, vergleichen und bereinigen, dass redundanter Ballast (72 exakte Duplikate, 114 Gaming-Skills) eliminiert wird und wenige standardisierte, hocheffiziente Master-Skills entstehen, die das gesamte Team produktiv nutzen kann?*

---

## Empfohlene Richtung (Recommended Direction)

Die Untersuchung aller Skills auf dem System ergab eine extreme Zersplitterung über 13 Quellpfade:

- **268 Skills insgesamt**
- **72 exakte Dateikopien** (identischer SHA256-Inhalt durch redundante Plugin-Kopien, z.B. in `.openclaw` und Doppelkopien in `.gemini/config/skills/`)
- **114 Spieleentwicklungs-Skills** (Phaser, PyGame, Pixi, Platformer, Audio-Synthese etc.), die für Unternehmens- und Arbeitsplatzsoftware Ballast darstellen und das Kontextfenster von KI-Agenten überlasten
- **88 wertvolle Kernskills** für Softwarearchitektur, Frontend, Code-Qualität, TDD, Cloud-Daten und Token-Effizienz
- **22 spezialisierte Qt/C++ Skills**

### Die 3-Phasen-Transformationsstrategie

1. **Phase 1: Physische Entschlackung & Duplikat-Bereinigung**
   - Löschen redundanter Unterordner (z.B. `.openclaw/skills/` innerhalb des Ponytail-Plugins).
   - Harmonisierung der Namensgebung (Beseitigung der `_` vs. `-` Dopplungen wie `bigquery_ai_ml` und `bigquery-ai-ml`).
   - Einsparung von 72 redundanten Dateien ohne jeglichen Informationsverlust.

2. **Phase 2: Entkopplung von Hobby/Gaming-Skills**
   - Verschieben der 114 Spieleentwicklungs-Skills in ein optionales, separates Paket (`plugins/gaming-suite`), anstatt sie im globalen `.gemini/config/skills/` Verzeichnis zu belassen.
   - Verhindert, dass der KI-Agent bei normalen Software-Aufgaben irrtümlich Spielphysik (z.B. Coyote-Time oder Screen-Shake) vorschlägt.

3. **Phase 3: Etablierung des 6+1 Modells für das Team**
   Anstatt 88 Mikroskills einzeln zu verwalten, stellen wir dem Team **6 fokussierte Master-Skills** plus **1 automatische Systemschicht** bereit:

   **Die 6 aktiven Master-Skills (aufrufbar & steuernd):**
   - `code-quality-and-review`: Umfassender 5-Achsen-Review, Root-Cause-Debugging, Ponytail-Minimalismus, OWASP-Sicherheit & Accidental Data Loss Prevention.
   - `software-architecture-and-specs`: Spec-Driven Development, API-Verträge, ADRs, Migrationspfade.
   - `modern-web-and-ui`: Barrierefreies HTML5/CSS, Dark Mode, UI/UX-Intelligenz, Chrome DevTools MCP & LCP-Optimierung.
   - `devops-testing-and-git`: Test-Driven Development (TDD), CI/CD-Pipelines, atomare Git-Commits, Observability.
   - `enterprise-data-and-sql`: High-Performance SQL, dbt/Dataform Pipelines, Schemamapping, Cloud Data Governance.
   - `agent-workflow-and-ideation`: Strukturierte Ideenverfeinerung, Nutzer-Interviews, Prompt-Führung.

   **Die 1 automatische System-Schicht (Zero-Config, im Hintergrund):**
   - `rules/context-and-token-efficiency.md`: Permanente Verhaltensregeln für den Agenten (Slice-Viewing, AST vor Implementierungsdetails, Log-Sanitisierung).
   - `hooks/hooks.json`: Automatischer `SessionStart`-Hook, der beim Starten eines Projekts/einer Session einmalig die Codebase-Architektur erfasst.

---

## Zu validierende Kernannahmen (Key Assumptions)

- [ ] **Annahme 1 (Kontext-Gewinn):** Das Entfernen der 114 Gaming-Skills und Reduzieren auf 6 Master-Skills senkt die Latenz und Token-Kosten pro Anfrage messbar und verbessert die Präzision des Agenten. *(Test: Vergleich der System-Prompt-Größe und Tool-Auswahl-Genauigkeit)*
- [ ] **Annahme 2 (Team-Akzeptanz):** Mitarbeiter bevorzugen 6 verständliche, umfassende Workflows gegenüber der Suche in über 80 einzelnen Mikroskills. *(Test: Testphase der 6 Master-Skills im Team für 2 Wochen)*
- [ ] **Annahme 3 (Automatisierungseffekt):** Durch die Auslagerung von Token-Effizienz in feste Regeln und Hooks spart das Team automatisch bis zu 80% Token, ohne dass jemand manuell an den Aufruf denken muss. *(Test: Vergleich von Kontext-Größen mit und ohne Regel)*

---

## MVP Scope (Minimal Viable Product)

- **Interaktives Vergleichs-Dashboard (`SkillLens Pro`):**
  - Vollständiger Katalog aller 268 Skills mit Filterung nach Eignung, Domäne und Herkunft.
  - Side-by-Side Comparator mit synchronisierter Ansicht von 2-3 Skills.
  - Duplikat-Detektor mit 1-Klick-PowerShell-Bereinigungsskript.
  - Vollbild- und Fenstermodus (User Rule 4).
- **Die 6 einsatzbereiten Master-Skills:**
  - Fertig ausformulierte `SKILL.md`-Dateien im Verzeichnis `consolidated-skills/`.
- **Die automatische Regel- und Hook-Schicht:**
  - `rules/context-and-token-efficiency.md` & `hooks/hooks.json`.

---

## "Not Doing" Liste (Bewusste Abgrenzung)

1. **Keine 1:1 Beibehaltung veralteter Einzel-Mikroskills:**
   - Skills wie `pylance-refactoring` oder 3-Zeiler-Skills werden nicht isoliert weitergepflegt, sondern sind integraler Bestandteil von `code-quality-and-review`.
2. **Keine Vermischung von Spieledomänen mit Unternehmensentwicklung:**
   - Spieleengines wie Phaser, Pygame oder PixiJS werden nicht in die Arbeits-Skills übernommen. Sie bleiben isoliert in ihrem Original-Repository.
3. **Keine irreversiblen Löschungen ohne Backup:**
   - Das Bereinigungsskript verschiebt Duplikate zuerst in ein mit Zeitstempel versehenes Backup-Verzeichnis (`$HOME\.gemini\skills_backup_*`), bevor gelöscht wird.

---

## Offene Fragen & Nächste Schritte

1. **Installations-Präferenz:** Möchten Sie die 7 Master-Skills global unter `C:\Users\DaniBani\.gemini\config\skills\` aktivieren oder als Workspace-Regeln in `.agents/skills` der einzelnen Kundenprojekte teilen?
2. **Spezial-Skills:** Werden im Unternehmen aktuell Qt/C++ Desktop-Applikationen entwickelt? Falls ja, kann das Qt-Paket als optionales 8. Spezial-Bündel beibehalten werden.
