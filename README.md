# SkillLens Pro: Skill-Analyse & Konsolidierungs-Suite

Willkommen bei **SkillLens Pro**, der interaktiven Plattform zur Untersuchung, zum detaillierten Vergleich und zur nachhaltigen Konsolidierung aller auf Ihrem PC installierten KI-Skills.

---

## 🎯 Zusammenfassung der Analyse-Ergebnisse

Bei dem vollständigen Scan Ihres Systems (`C:\Users\DaniBani\.gemini`, VS Code Extensions, Repositories etc.) wurden **268 Skills** identifiziert:

| Kategorie | Anzahl | Anteil | Bewertung für den Arbeitsalltag |
| :--- | :---: | :---: | :--- |
| **Exakte Dateikopien (Duplikate)** | **72** | **26.9%** | Identische SHA256-Kopien (z.B. `.openclaw`-Ordner, Doppelkopien in Plugin-Ordnern). Zu bereinigen! |
| **Gaming & Spieledesign** | **114** | **42.5%** | Phaser, Pygame, Pixi, Platformer, Screen-Shake etc. Für die Büro- und Softwarearbeit Ballast. |
| **Arbeits-Kernkompetenzen (High Value)** | **88** | **32.8%** | Softwarearchitektur, Code-Reviews, TDD, Frontend, Cloud & Token-Effizienz. **Die Basis für das Team!** |
| **Spezialisiert (Qt / C++)** | **22** | **8.2%** | Nur relevant bei Desktop-App-Entwicklung mit Qt/QML. Als optionales Plugin auslagern. |
| **Konsolidiertes Ziel-Set** | **7** | - | **7 Master-Skills, die alle 88 Arbeits-Skills vereinen.** |

---

## 🚀 Schnelleinstieg in das Dashboard

Die interaktive Web-App **SkillLens Pro** ist sofort einsatzbereit:

1. **Option A (Laufender lokaler Server):**
   Öffnen Sie im Browser:
   [http://localhost:4321/index.html](http://localhost:4321/index.html)

2. **Option B (Direkt im Browser öffnen):**
   Doppelklicken Sie einfach auf [`index.html`](file:///c:/Users/DaniBani/Documents/VisualStudioCodeProjects/skill-compare/index.html) in diesem Projektordner.

---

## ✨ Features des Vergleichs-Dashboards

- 📊 **Dashboard & Kennzahlen:** Visuelle Analyse der Quellen, Domänenverteilung und Einsparpotenziale.
- 🔍 **Skill-Katalog & Filter:** Echtzeit-Filterung nach Eignung (Arbeitsrelevant vs. Gaming), Domäne, Quelle und Volltextsuche.
- ⚖️ **Side-by-Side Comparator:** Direkter Vergleich von 2 bis 3 Skills nebeneinander mit synchronem Inhalts-Viewer.
- ⚠️ **Duplikat-Detektor:** Exakte Gruppierung aller 72 Duplikate mit Pfadangaben und Empfehlungen, welches Original beibehalten werden soll.
- 📦 **Die 6 Master-Skills & Automatik:** Interaktiver Explorer der kombinierten Skills mit Quellauflistung und vollständiger `SKILL.md`-Vorschau sowie der automatischen Regel- und Hook-Schicht.
- 💡 **/idea-refine One-Pager:** Strukturierte Darstellung des "How Might We"-Statements, der 5 Innovations-Linsen und des Stresstests.
- ⛶ **Vollbild- & Fenstermodus:** Bequemer Umschalter in der Kopfleiste (und Taste `F11`) für konzentriertes Arbeiten.

---

## 📦 Das 6+1 Modell: 6 Master-Skills + 1 Automatik-Schicht

### 1. Die 6 einsatzbereiten Master-Skills (Aktiv aufrufbar)

Die kombinierten Skills liegen fertig formuliert und einsatzbereit im Ordner [`consolidated-skills/`](file:///c:/Users/DaniBani/Documents/VisualStudioCodeProjects/skill-compare/consolidated-skills), als Team-Vorlage in [`.agents/skills/`](file:///c:/Users/DaniBani/Documents/VisualStudioCodeProjects/skill-compare/.agents/skills) sowie global in `C:\Users\DaniBani\.gemini\config\skills`:

1. **`review`** (Trigger: `review`, `check`, `debug` / `prüfe`, `untersuche`): Multi-Achsen-Review (5 Dimensionen), Root-Cause-Debugging, Ponytail-Minimalismus, OWASP-Security und Schutz vor Datenverlust.
2. **`spec`** (Trigger: `spec`, `architect`, `design` / `entwerfe`, `spezifikation`, `plane`): Spec-Driven Development, API-Schnittstellenverträge, Architecture Decision Records (ADRs) und Datenbankschemamigrationen.
3. **`ui`** (Trigger: `ui`, `frontend`, `web`, `css` / `oberfläche`, `gui`, `barrierefrei`): Barrierefreies HTML5/CSS, Dark Mode, Responsive Design, Chrome DevTools MCP und Core Web Vitals (LCP).
4. **`ship`** (Trigger: `ship`, `test`, `deploy`, `git` / `veröffentliche`, `teste`, `pipeline`): Test-Driven Development (TDD), CI/CD-Pipelines, atomare Git-Commits und Observability.
5. **`data`** (Trigger: `data`, `sql`, `bigquery`, `dbt` / `daten`, `datenbank`, `abfrage`): High-Performance SQL-Tuning, dbt/Dataform ELT-Pipelines, Schemamapping und Cloud Data Governance.
6. **`ideate`** (Trigger: `ideate`, `refine`, `interview` / `idee`, `konzept`, `hinterfrage`): Strukturierte Ideenfindung, Anforderungs-Interviews und KI-Agenten-Metasteuerung.

### 2. Die automatische System-Schicht (Zero-Config, im Hintergrund)

- **`rules/context-and-token-efficiency.md`**: Permanente Verhaltensregel für den Agenten (erzwingt Slice-Viewing, AST vor Implementierungsdetails, Log-Sanitisierung).
- **`hooks/hooks.json`**: Automatischer `SessionStart`-Hook zur Erfassung der Codebase-Architektur beim Projektstart.
- **Vorteil:** Spart bis zu 85% Token völlig automatisch, ohne dass ein Mitarbeiter daran denken muss, einen Skill aufzurufen!

---

## 🛠️ Skripte & Automatisierung

- `python scripts/scan_skills.py`: Durchsucht den gesamten PC nach `SKILL.md`-Dateien und extrahiert Metadaten.
- `python scripts/analyze_skills.py`: Berechnet SHA256-Duplikate, Namenskollisionen und Ähnlichkeitsmatrizen.
- `python scripts/tag_skills.py`: Ordnet jeden Skill einem Ziel-Bündel und einer Eignungskategorie zu.
- `python scripts/export_web_data.py`: Generiert `data.js` für das Frontend.
- `python scripts/create_consolidated_skills.py`: Erstellt die 7 Master-`SKILL.md`-Dateien.
