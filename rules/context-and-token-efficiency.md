# Context & Token Efficiency: Automatische Systemregel

Diese Regel ist dauerhaft im Hintergrund aktiv und erzwingt maximale Token-Disziplin bei jeder Unterhaltung und jedem Prompt, ohne dass ein Skill manuell aufgerufen werden muss.

---

## 1. Verhaltensregeln für den KI-Agenten (Permanente Pflicht)

1. **Dateizugriffe & Slices (`StartLine` / `EndLine`):**
   - Lade niemals ganze Quellcodedateien mit mehr als 250 Zeilen vollständig in den Kontext, wenn nur ein spezifischer Funktionsblock oder ein Fehler untersucht wird.
   - Nutze immer gezielte Bereichsabfragen (`view_file` mit `StartLine` und `EndLine`) oder `grep_search`.

2. **AST-Skelettierung vor Implementierungsdetails:**
   - Wenn Code-Schnittstellen, Typdefinitionen oder Modulbeziehungen analysiert werden, extrahiere nur die Klassensignaturen, Methodennamen und Typ-Annotationen (AST-Skelett). Funktionsrümpfe werden abgeschnitten.

3. **Log- und Stacktrace-Sanitisierung:**
   - Vor der Analyse von Terminal-Outputs oder CI/CD-Logs:
     - Entferne wiederholte identische Zeilen (Deduplizierung).
     - Entferne ANSI-Farb- und Escape-Sequenzen.
     - Blende interne Runtime- und Framework-Stackframes aus; isoliere die tatsächliche Fehlerursache (Root Cause).

4. **Daten-Payloads & Schemareduktion:**
   - Große JSON-, CSV- oder SQL-Dumps niemals roh in den Prompt laden.
   - Konvertiere Datensätze in ein kompaktes Schema mit maximal 2 repräsentativen Beispielzeilen.

5. **Dokumenten-Konvertierung (PDF / DOCX / Notebooks):**
   - Wandle Dokumente vor der Verarbeitung in reines, schlankes Markdown um. Entferne Formatierungs-Bloat, Inline-Styles und Base64-Grafiken.

---

## 2. Automatisches SessionStart-Verhalten

- Beim Start einer neuen Unterhaltung oder eines neuen Projekts erfasst der Agent einmalig die Modulstruktur des Repositories und legt sie in einer kompakten Übersicht im Scratchpad ab.
- Dies verhindert wiederholtes, blindes Suchen im Projektverzeichnis.
