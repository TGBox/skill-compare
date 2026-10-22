# Plattform-Leitplanken für agentische Entwicklung

> Stand: 2026-10-22 · Ergebnis einer /idea-refine-Session
> Ausgearbeitete Fassung für die Leitung: <https://claude.ai/artifact/73wwSAsBedfgFnra9Z8X3v>

## Problem Statement

Wie sorgen wir dafür, dass viele parallele Coding-Agenten (Claude, Gemini …) dieselben
Plattform-Fakten kennen und Kollisionen vor dem Merge sichtbar werden, während der Chef
ein aktuelles Lagebild hat, ohne dass die Lösung davon abhängt, dass alle mitmachen?

Rahmen: Zielgruppe sind Chef und Entwickler gleichermaßen · Teilnahme zunächst freiwillig ·
gemischte Werkzeuge (Claude Code, Gemini/Antigravity u. a.).

## Recommended Direction

Ein Repo `development/plattform` als einzige Quelle für alles, was repoübergreifend gilt:

- `registry/services.toml`: Ports, Sub-Service-Namen, Apache-Pfade, db.ini-Sektionen, DB-Schemata
  (Startbestand aus data-al-overview; Abgleich mit `datahub-release/installer/templates/services.toml.template`)
- `PLATTFORM.md` (als `AGENTS.md` bzw. per `@`-Import in `CLAUDE.md`): ca. 20 harte Regeln
  (Apiserver seriell → kein großes `limit`, immer über Controller :8080, Design-System statt Hex,
  Geheimnisse in nssm statt `.env`, Release über Projekt 110 …)
- `adr/`: Architekturentscheidungen, beginnend mit den offenen (auth, Port 8089, Registry-Owner)
- `skills/`: wenige Firmen-Skills, die auf die Registry verweisen statt Fakten zu kopieren

Darauf zwei zentrale Läufe, die niemand installieren muss:

1. CI-Template-Job (nicht blockierend): vergleicht Ports/Namen im MR mit der Registry → MR-Kommentar
2. Wöchentlicher Drift-Lauf: data-al-overview-Analyse automatisiert → Lagebild für den Chef

Werkzeugneutral, weil nicht alle Claude nutzen. Zentrale Läufe, weil die Teilnahme freiwillig ist.

## Key Assumptions to Validate

- [ ] Die Registry bleibt aktuell → Owner festlegen; 4 Wochen lang jede Port-/Service-Änderung über Registry-MR
- [ ] Agenten halten sich an PLATTFORM.md → 2 Entwickler (Claude + Gemini) legen testweise einen Sub-Service an; freier Port?
- [ ] Ein nicht blockierender Hinweis reicht → zählen, wie viele Hinweise vor dem Merge behoben werden
- [ ] Firmen-Skills schlagen generische → gleiche Aufgabe mit/ohne `/neuer-subservice`
- [ ] Der Chef liest das Lagebild → Format vorab mit ihm abstimmen

## MVP Scope (4 Wochen)

- Woche 1 – Grundlage: Plattform-Repo, Registry aus data-al-overview, Port 8089 auflösen,
  PLATTFORM.md, ADR-Vorlagen für die offenen Entscheidungen → an die Leitung
- Woche 2 – Sichtbarkeit: MR-Hinweis als GitLab-CI-Template + Jenkins-Schritt
- Woche 3 – Firmen-Skills: `/neuer-subservice`, `/apiserver-zugriff`, `/release-komponente`;
  Format bereinigen (CLAUDE.md/AGENTS.md statt `rules/`, Antigravity-Hook mit scan_skills.py entfernen,
  `consolidated-skills/` und `.agents/skills/` zusammenlegen)
- Woche 4 – Lagebild und Pilot: Drift-Lauf wöchentlich, Pilot mit 2–3 Entwicklern auswerten,
  Entscheidung über Pflicht-Check

## Not Doing (and Why)

- Kein reines Claude-Plugin zuerst — erreicht die Gemini-Nutzer nicht; später als zusätzlicher Verteilweg
- Kein Claude-MR-Review-Bot — erst wenn die Registry steht, sonst prüft er gegen nichts
- Keine Pflicht-Checks — Mandat fehlt; Hinweise liefern erst die Belege dafür
- Keine Eigenpflege der 6 generischen Master-Skills — fertige Pakete können das besser
- Kein weiterer Repo-Atlas — Obsidian-Vault und `/gitlab-issue` einbinden statt ersetzen
- Gruppe `data` (Delphi/Forth/Data-Cur) vorerst nur in der Registry, ohne eigene Skills
- Keine unbelegten Zahlen (z. B. „85 % Token“) — erst messen

## Open Questions

- Wer ist Owner der Registry?
- Wer pflegt `devops/gitlab-issue` und den Obsidian-Vault, und lassen sie sich einbinden?
- Ist `services.toml.template` die Wahrheit, oder wird es aus einem eigenen Registry-Format erzeugt?
- Welches Format will der Chef für das Lagebild (Mail, Seite, power-py)?
- Auth: Rust-auth-backend oder Keycloak (auth-01)? (ADR)
