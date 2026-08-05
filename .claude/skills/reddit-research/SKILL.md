---
name: reddit-research
description: Reddit-Recherche und Engagement. Scannt Subreddits, formuliert Antworten vor, extrahiert Insights. Vorlage — Konfiguration unter "Konfiguration" und "Persona" vor Nutzung ausfüllen.
license: Adaptiert von Svenja-dev/claude-code-skills (MIT), Konfiguration/Persona für Balero Creativo generalisiert.
---

# Reddit Research Skill

## Konfiguration

**Ziel-Subreddits:** (Beispiel — an eigene Nische anpassen)
- r/graphic_design (Grafikdesign allgemein)
- r/branding (Markenstrategie)
- r/web_design (Webdesign)
- r/marketing (Marketing allgemein)
- r/Entrepreneur (Gründer:innen, KMU)
- r/ClaudeAI (Claude-Community, AI-Diskussionen)

**Reddit-Account:** [DEIN-REDDIT-ACCOUNT, z.B. u/dein-handle]

**Fokus-Keywords:** [DEINE THEMEN, z.B. Branding, Logo, Markenidentität, Design-Prozess, Kreativagentur]

---

## Slash-Commands

### /reddit-scan
**Zweck:** Scannt alle konfigurierten Subreddits nach relevanten Posts

**Workflow:**
1. Rufe für jeden Subreddit die letzten 25 Posts ab (via WebFetch oder MCP)
2. Filtere nach Keywords: [deine Fokus-Keywords, siehe Konfiguration]
3. Sortiere nach Relevanz (Keyword-Matches + Upvotes)
4. Zeige Top 10 mit: Titel, Subreddit, Upvotes, Kommentaranzahl, URL

**Ausgabeformat:**
```
## Reddit-Scan: [Datum]

### Relevante Posts (Top 10)

1. **[Titel]** - r/[subreddit] (↑ [upvotes] | 💬 [comments])
   Keywords: [matched keywords]
   → [url]

2. ...
```

**API-Endpunkte:**
```
https://www.reddit.com/r/graphic_design/new.json?limit=25
https://www.reddit.com/r/branding/new.json?limit=25
...
```

---

### /reddit-draft
**Zweck:** Erstellt Value-First Antwort-Entwurf für einen Reddit-Post

**Input:** Reddit-Post-URL oder Beschreibung des Themas

**Workflow:**
1. Lade Post-Inhalt und Top-Kommentare
2. Analysiere: Was ist die Frage/das Problem?
3. Generiere hilfreiche Antwort nach diesen Regeln:

**Antwort-Regeln (Value-First):**
- NIEMALS direkte Produktwerbung
- IMMER erst Mehrwert liefern (Erfahrung, Tipps, Ressourcen)
- Persönliche Erfahrung einbauen (eigene Projekte, konkrete Ergebnisse)
- Fachliche Kompetenz zeigen ohne arrogant zu wirken
- Am Ende OPTIONAL: "Falls interessiert, arbeite ich an [Thema]" (nur wenn 100% relevant)

**Ausgabeformat:**
```
## Antwort-Entwurf für: [Post-Titel]

**Subreddit:** r/[subreddit]
**Karma-Impact:** [niedrig/mittel/hoch] (basierend auf Themenrelevanz)

---

### Vorgeschlagene Antwort:

[Antworttext hier - 100-300 Wörter]

---

### Hinweise:
- [Ton-Empfehlung für diesen Subreddit]
- [Risiken wenn vorhanden]
```

---

### /reddit-insights
**Zweck:** Extrahiert Pain Points und Feature-Ideen aus Reddit-Diskussionen

**Workflow:**
1. Sammle Posts zu einem Thema (z.B. "Branding-Probleme bei KMU")
2. Analysiere Kommentare nach wiederkehrenden Beschwerden
3. Kategorisiere in: Pain Points, Feature-Wünsche, Competitor-Mentions

**Ausgabeformat:**
```
## Reddit Insights: [Thema]

**Analysierte Posts:** [Anzahl]
**Zeitraum:** [letzte X Tage/Wochen]

### Pain Points (wiederkehrende Probleme)

| Problem | Häufigkeit | Beispiel-Zitate | Relevanz für dein Angebot |
|---------|------------|-----------------|-------------------|
| [Problem 1] | [x Mal] | "[Zitat]" | [hoch/mittel/niedrig] |
| ... | ... | ... | ... |

### Feature-Wünsche

| Feature | Nachfrage | Status in deinem Angebot |
|---------|-----------|-------------------|
| [Feature] | [hoch/mittel] | [vorhanden/geplant/neu] |

### Competitor-Mentions

| Tool/Produkt | Sentiment | Stärken | Schwächen |
|--------------|-----------|---------|-----------|
| [Name] | [positiv/neutral/negativ] | [...] | [...] |

### Empfehlungen für deine Content-/Produkt-Roadmap

1. **[Priorität 1]:** [Empfehlung basierend auf Pain Points]
2. **[Priorität 2]:** ...
```

---

### /reddit-monitor
**Zweck:** Zeigt neue relevante Posts der letzten 24 Stunden

**Workflow:**
1. Prüfe alle konfigurierten Subreddits
2. Filtere Posts < 24h alt
3. Sortiere nach Engagement (Upvotes + Kommentare)
4. Markiere Posts die Antwort verdienen

**Ausgabeformat:**
```
## Reddit Monitor: [Datum/Uhrzeit]

### Neue Posts (letzte 24h)

**Antwort empfohlen:**
- [ ] [Post 1] - r/[sub] - [Grund warum antworten]
- [ ] [Post 2] - ...

**Beobachten:**
- [Post 3] - r/[sub] - [Warum interessant]

**Statistiken:**
- Neue Posts gesamt: [X]
- Davon relevant: [Y]
- Mit Antwort-Potenzial: [Z]
```

---

## Subreddit-spezifische Regeln

### r/graphic_design
- **Ton:** Professionell, erfahrungsbasiert
- **Tabu:** Direkte Verkaufspitches
- **Gut funktioniert:** Case Studies, Vorher/Nachher, Praxistipps

### r/web_design
- **Ton:** Technisch, präzise
- **Tabu:** Marketing-Sprache, Buzzwords
- **Gut funktioniert:** Konkrete Beispiele, Tool-Tipps, Troubleshooting

### r/branding
- **Ton:** Strategisch, erfahrungsbasiert
- **Tabu:** Übertreibungen
- **Gut funktioniert:** Methodenvergleiche, Case Studies

### r/marketing
- **Ton:** Sachlich, datengetrieben
- **Tabu:** Reiner Selbstpromo ohne Substanz
- **Gut funktioniert:** Daten/Ergebnisse, ehrliche Learnings

### r/Entrepreneur
- **Ton:** Zukunftsorientiert, pragmatisch
- **Gut funktioniert:** Konkrete Zahlen, Gründer-Erfahrungen

### r/ClaudeAI
- **Ton:** Community-Member, nicht Experte
- **Tabu:** Angeberei über eigene Projekte
- **Gut funktioniert:** Hilfreiche Tipps, Use-Case-Sharing, Fragen stellen

---

## Karma-Aufbau-Strategie

**Phase 1: Zuhören (Woche 1-2)**
- Nur lesen, keine Posts
- Notiere wiederkehrende Fragen
- Identifiziere aktive Power-User

**Phase 2: Helfen (Woche 3-6)**
- Beantworte Fragen ohne Eigeninteresse
- Teile Ressourcen (Links, Guides, Tools)
- Upvote gute Antworten anderer

**Phase 3: Beitragen (ab Woche 7)**
- Eigene Erfahrungsberichte teilen
- AMAs oder Diskussionen starten
- Subtil auf eigene Projekte verweisen (nur wenn 100% relevant)

---

## Technische Implementierung (Praxis-erprobt)

### Methoden-Übersicht

| Methode | Lesen | Posten | Auth nötig |
|---------|-------|--------|------------|
| **Claude-in-Chrome** | ✅ | ✅ (manuell) | Via Browser-Login |
| **curl + User-Agent** | ✅ | ❌ | Nein |
| **WebFetch** | ❌ | ❌ | - |

### 1. Claude-in-Chrome MCP (BESTE für Interaktion)

**Wann nutzen:** Kommentare posten, Replies checken, Karma tracken

##### /reddit-scan Workflow (Browser)
```
1. tabs_context_mcp (createIfEmpty: true)
   → Tab-Gruppe prüfen/erstellen

2. tabs_create_mcp
   → Neuen Tab erstellen

3. navigate (url: "https://www.reddit.com/r/graphic_design/new/")
   → Subreddit öffnen

4. browser_wait_for (time: 2)
   → Warten bis geladen

5. read_page (tabId: X)
   → Posts extrahieren

6. Für jeden relevanten Post:
   - get_page_text → Volltext lesen
   - Relevanz bewerten
```

##### /reddit-draft Workflow (Browser + Posten)
```
1. navigate (url: "[POST-URL]")
   → Post öffnen

2. get_page_text (tabId: X)
   → Post + Kommentare lesen

3. Antwort generieren (Anti-KI Regeln!)

4. find (query: "comment box", tabId: X)
   → Kommentarfeld finden

5. USER muss manuell posten (ToS!)
   → Vorschlag in Zwischenablage oder anzeigen
```

##### /reddit-track Workflow (Browser)
```
1. navigate (url: "https://www.reddit.com/user/[DEIN-REDDIT-ACCOUNT]/comments/")
   → Eigene Kommentare öffnen

2. read_page → Karma-Scores extrahieren

3. Für jeden getrackten Kommentar:
   - navigate → Original-Post öffnen
   - read_page → Replies zählen
   - Performance-Report aktualisieren
```

---

### 2. curl mit Browser User-Agent (BESTE für Bulk-Scan)

**Wann nutzen:** Schneller Scan vieler Subreddits, keine Interaktion nötig

### Erfahrung: WebFetch vs curl

**Problem:** WebFetch wird von Reddit blockiert (403 Forbidden)
**Lösung:** Bash + curl mit Browser User-Agent

### Funktionierende curl-Befehle

**Subreddit-Posts abrufen (FUNKTIONIERT):**
```bash
# Neue Posts
curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  "https://www.reddit.com/r/graphic_design/new.json?limit=25"

# Hot Posts
curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  "https://www.reddit.com/r/web_design/hot.json?limit=25"

# Top Posts (letzte Woche)
curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  "https://www.reddit.com/r/marketing/top.json?t=week&limit=25"
```

**Suche in Subreddit:**
```bash
curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  "https://www.reddit.com/r/graphic_design/search.json?q=branding%20logo&restrict_sr=1&limit=25"
```

**Post mit Kommentaren:**
```bash
curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  "https://www.reddit.com/r/graphic_design/comments/[POST-ID].json"
```

### Parsing mit jq (optional)

```bash
# Titel und URLs extrahieren
curl -s -A "Mozilla/5.0..." "https://www.reddit.com/r/graphic_design/new.json?limit=10" | \
  jq -r '.data.children[].data | "\(.title) → \(.url)"'

# Posts mit Keyword filtern
curl -s -A "Mozilla/5.0..." "https://www.reddit.com/r/branding/new.json?limit=50" | \
  jq -r '.data.children[].data | select(.title | test("branding|logo"; "i")) | "\(.title)"'
```

### Warum WebFetch nicht funktioniert

| Tool | User-Agent | Ergebnis |
|------|-----------|----------|
| WebFetch | Claude-Code/1.0 | ❌ 403 Forbidden |
| curl (ohne -A) | curl/8.x | ❌ 403 Forbidden |
| curl (mit -A) | Mozilla/5.0... | ✅ 200 OK |

**Grund:** Reddit blockiert automatisierte User-Agents, erlaubt aber Browser-User-Agents.

### Rate Limits

- 60 Requests/Minute ohne Auth
- Bei Überschreitung: 429 Too Many Requests
- Empfehlung: 2-3 Sekunden zwischen Requests

---

## API-Referenz (Endpunkte)

**Basis-URL:** `https://www.reddit.com`

| Endpunkt | Beschreibung |
|----------|--------------|
| `/r/{sub}/new.json?limit=25` | Neueste Posts |
| `/r/{sub}/hot.json?limit=25` | Trending Posts |
| `/r/{sub}/top.json?t=day&limit=25` | Top Posts (day/week/month/year/all) |
| `/r/{sub}/search.json?q={query}&restrict_sr=1` | Suche in Subreddit |
| `/r/{sub}/comments/{id}.json` | Post mit Kommentaren |

**Wichtige Parameter:**
- `limit`: Max 100 Posts pro Request
- `after`: Pagination Token (für mehr als 100)
- `t`: Zeitraum für /top (hour/day/week/month/year/all)
- `restrict_sr`: 1 = nur in diesem Subreddit suchen

---

## Persona: [DEIN NAME]

> Fülle diesen Abschnitt mit deiner echten Persona aus, bevor du die Commands nutzt. Beispielstruktur:

**Hintergrund:**
- [Persönlicher Kontext, sparsam erwähnen]
- [Deine fachliche Expertise, z.B. Branding/Design]
- [Deine Erfahrung: Rolle, Jahre, Projektgröße]
- Pragmatisch, direkt, manchmal frustriert über Bürokratie/schlechte Tools
- Reddit-Account: [DEIN-REDDIT-ACCOUNT]

**Schreibstil:**
- [Denksprache vs. Schreibsprache, falls unterschiedlich]
- Spricht aus Erfahrung, nicht aus Lehrbüchern
- Gibt konkrete Zahlen und Beispiele aus echten Projekten

---

## Anti-KI-Detection Regeln (KRITISCH)

### REDDIT-SPEZIFISCHE FORMATIERUNG (WICHTIG!)

**KEINE Markdown-Formatierung in Kommentaren:**
- KEINE **Sterne** für Bold (schreibe einfach: wichtig, nicht **wichtig**)
- KEINE Listen mit - oder * (schreibe: "first thing is X, also Y, and then Z")
- KEINE Überschriften (## oder ###)
- KEINE Code-Blöcke für normalen Text
- KEINE horizontalen Trenner (---)
- Überschriften als Plaintext: "Quick tip -" nicht "**Quick tip** -"

**Kleinschreibung bei kurzen Kommentaren:**
- Kurze Antworten komplett klein: "yeah that makes sense, we had the same issue"
- Längere Posts können normal sein, aber nicht übertrieben formal
- Satzanfänge klein OK: "honestly? i think you're overcomplicating this"

**Typische menschliche Fehler (gezielt einbauen, 1-2 pro Post):**
- "wasnt" statt "wasn't" (fehlender Apostroph)
- "theres" statt "there's"
- "dont" statt "don't"
- "its" vs "it's" Verwechslung
- "teh" statt "the" (Tippfehler)
- "adn" statt "and"
- "wierd" statt "weird"
- Doppeltes Leerzeichen zwischen Wörtern
- Fehlendes Leerzeichen nach Komma: "yeah,but still"

**Reddit-typische Sprache:**
- "tbh", "imo", "ngl", "afaik", "iirc"
- "lol", "lmao" (sparsam)
- "idk" statt "I don't know"
- "gonna", "wanna", "kinda", "sorta"
- Sätze die mit "And" oder "But" beginnen
- Abrupte Enden ohne Fazit

### NIEMALS verwenden (KI-Erkennungsmerkmale):

**Verbotene Wörter/Phrasen:**
- "Delve", "delve into", "dive into", "deep dive"
- "Tapestry", "Vibrant", "Bustling", "Realm", "Embark"
- "It's important to note", "It's worth mentioning"
- "Furthermore", "Moreover", "Additionally" (zu formal)
- "In conclusion", "In summary", "To summarize"
- "Navigate", "landscape", "ever-evolving"
- "Testament to", "Symphony of", "Embrace"
- "Whether you're X or Y", "When it comes to"
- "Leverage", "Robust", "Streamline", "Optimize" (Buzzwords)
- "The best part?", "The result?", "And honestly?" (rhetorische Fragen-Pattern)
- "It's not X. It's Y." (Kontrast-Framing)

**Verbotene Strukturen:**
- Em-Dash (—) übermäßig verwenden → max 1 pro Post
- Perfekte Listen mit genau 3 Punkten → variiere: 2, 4, 5
- Gleichmäßige Satzlängen → mix kurz und lang
- Jeder Absatz gleich lang → variiere drastisch
- Zu viele Übergangswörter ("firstly", "secondly")
- Perfekte Grammatik IMMER → gelegentliche Fehler OK
- Formeller Stil durchgehend → wechsle Register

### IMMER einbauen (Menschliche Merkmale):

**Authentizitäts-Signale:**
1. **Ungleichmäßige Satzlängen** - Ein Satz kurz. Der nächste vielleicht etwas länger, weil du einen Gedanken zu Ende bringen willst.
2. **Gelegentliche Tippfehler** - "teh" statt "the", "adn" statt "and" (max 1-2 pro Post)
3. **Persönliche Erfahrungen** - "Bei uns war das so...", "Wir hatten mal einen Fall wo..."
4. **Emotionen zeigen** - Frustration ("Ich hasse es wenn..."), Begeisterung ("Das war ein Game-Changer")
5. **Unvollständige Gedanken** - "Aber naja..." oder einfach abbrechen
6. **Umgangssprache** - "tbh", "imo", "ngl", Kontraktionen
7. **Abrupte Themenwechsel** - "Oh, und noch was:"
8. **Rhetorische Fragen** - aber NICHT im KI-Stil ("You know what helped us?")
9. **Sätze mit "And" oder "But" beginnen**
10. **Spezifische Details** - Nicht "many companies" sondern "3 of my 5 clients"

**Frustrations-Phrasen (authentisch):**
- "ugh, don't get me started on..."
- "this drove me crazy for months"
- "I wish someone had told me earlier"
- "classic mistake, been there"
- "not gonna lie, this sucked"
- "we learned this the hard way"

**Mama-von-Zwillingen Einschübe (optional, sparsam):**
- "wrote this while the kids are napping lol"
- "sorry for typos, multitasking here"
- "quick reply between meetings"

---

## Antwort-Templates (Anti-KI optimiert)

### Template 1: Erfahrungsbericht
```
[Hook mit persönlicher Erfahrung]
We dealt with exactly this at [vague company description]. Took us about [specific timeframe] to figure out.

[Kern-Insight, direkt]
What worked: [konkrete Maßnahme]. What didn't: [Fehler den wir gemacht haben].

[Spezifisches Detail]
Our conversion rate went from [X]% to [Y]% after we [konkrete Änderung]. Not saying it'll work for everyone but worth a shot.

[Optional: Frustration oder Warnung]
Fair warning tho - [Vendor/Approach] sounds great on paper but [Problem]. Ask me how I know lol

[Hilfsangebot ohne Pitch]
Happy to share more details if useful. We made every mistake in the book.
```

### Template 2: Technische Hilfe
```
[Direkte Antwort, kein Intro]
Yeah so [technische Lösung].

[Kontext warum]
The reason this works is [kurze Erklärung]. We tried [Alternative] first and it [Ergebnis].

[Gotcha/Warnung]
One thing that bit us: [spezifisches Problem]. Make sure you [Prävention].

[Code/Config falls relevant - nicht perfekt formatiert]
something like:
[code snippet, casual formatting]

might need to adjust for your setup obvs
```

### Template 3: Meinungs-Post
```
[Meinung direkt raus]
Honestly? [Meinung]. I know [Gegenargument] but in my experience [Begründung].

[Anekdote]
Had a client who [kurze Story]. Ended up [Ergebnis].

[Nuance]
That said, depends on [Faktor]. If you're [Situation A], maybe [Alternative] makes more sense.

[Offene Frage]
Curious what others think. Am I the only one who [Erfahrung]?
```

---

## Qualitäts-Checkliste vor dem Posten

- [ ] Keine verbotenen KI-Phrasen?
- [ ] Satzlängen variieren?
- [ ] Mindestens 1 persönliche Erfahrung?
- [ ] Keine perfekte 3er-Liste?
- [ ] Emotion/Frustration erkennbar?
- [ ] Spezifische Zahlen statt vage Aussagen?
- [ ] Kein "In conclusion" oder ähnliches Ende?
- [ ] Max 1 Em-Dash?
- [ ] Gelegentlicher Typo oder informelle Sprache?

---

## /reddit-track
**Zweck:** Trackt Performance von geposteten Kommentaren

**Workflow:**
1. Lade Tracking-Log (siehe unten)
2. Für jeden getrackten Kommentar:
   - Navigiere zur URL (Browser oder Exa Search)
   - Extrahiere: Upvotes, Replies, Awards
   - Berechne Engagement-Rate
3. Aktualisiere Tracking-Log
4. Zeige Performance-Report

**Ausgabeformat:**
```
## Reddit Performance Report: [Datum]

### Kommentar-Performance

| Post | Subreddit | Gepostet | ↑ Votes | 💬 Replies | Trend |
|------|-----------|----------|---------|------------|-------|
| [Titel] | r/[sub] | [Datum] | [X] | [Y] | 📈/📉/➡️ |

### Top Performer
🏆 **[Post-Titel]** - [X] Upvotes, [Y] Replies
   Warum erfolgreich: [Analyse]

### Learnings
- [Was hat funktioniert]
- [Was kann verbessert werden]

### Nächste Aktionen
- [ ] [Auf Reply antworten in Post X]
- [ ] [Ähnlichen Kommentar in r/Y posten]
```

**Tracking-Intervalle:**
- Nach 24h: Erste Performance-Messung
- Nach 7 Tagen: Mid-term Check
- Nach 30 Tagen: Final Performance

---

## Tracking-Log (Gepostete Kommentare)

> Trage hier deine eigenen geposteten Kommentare ein, sobald du startest.

### Aktive Kommentare

| Datum | Post-Titel | Subreddit | URL | Status |
|-------|------------|-----------|-----|--------|
| [Datum] | [Post-Titel] | r/[subreddit] | [URL] | ⏳/✅ Gepostet |

### Performance-Historie

| Datum | Post | Upvotes | Replies | Notes |
|-------|------|---------|---------|-------|
| [Datum] | [Post] | [X] | [Y] | [Notiz] |

---

## /reddit-reply
**Zweck:** Antwortet auf Replies zu unseren Kommentaren

**Workflow:**
1. Prüfe Tracking-Log auf neue Replies
2. Lade Reply-Kontext
3. Generiere authentische Antwort (Anti-KI Regeln!)
4. Poste und aktualisiere Log

**Wichtig:**
- Replies sollten KÜRZER sein als Original-Kommentare
- Noch informeller (mehr "yeah", "totally", "haha")
- Direkt auf die Frage eingehen
- Keine neuen Verkaufspitches

---

## Karma-Tracking

**Account:** [DEIN-REDDIT-ACCOUNT]

| Datum | Post Karma | Comment Karma | Notizen |
|-------|------------|---------------|---------|
| [Datum] | [X] | [Y] | [Notiz] |

**Ziel:** 100+ Comment Karma für Glaubwürdigkeit in deinen Ziel-Subs
