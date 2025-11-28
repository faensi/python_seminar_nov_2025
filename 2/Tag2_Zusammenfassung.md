# Tag 2: Fehlerbehandlung und robuste Software - Zusammenfassung

## Behandelte Themen

1. **Syntax- vs Semantikfehler** (Notebook 08)
   - Unterschiede zwischen Syntax- und Semantikfehlern
   - Debugging-Strategien

2. **Ausnahmen behandeln** (Notebook 09)
   - try/except Blöcke
   - Verschiedene Exception-Typen
   - Fehlerbehandlung Best Practices

3. **Eigene Ausnahmen** (Notebook 10)
   - Custom Exceptions erstellen
   - Exception-Hierarchien

4. **finally und Aufräumen** (Notebook 11)
   - finally-Block
   - with-Statement
   - Context Manager

5. **Seiteneffekte, *args, **kwargs** (Notebook 12)
   - Seiteneffekte in Funktionen
   - Variable Argumentanzahl mit *args und **kwargs

6. **Logging** (Notebook 13)
   - Logging-Modul verwenden
   - Log-Level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
   - Formatierung und Datei-Logging
   - Logging in Funktionen und Modulen

## Wichtige Konzepte

- **Exception Handling**: Robuste Fehlerbehandlung mit try/except
- **Context Manager**: Automatisches Ressourcen-Management mit with
- **Custom Exceptions**: Eigene Exception-Klassen für spezifische Fehler
- **Variable Argumente**: *args für Positionsargumente, **kwargs für Keyword-Argumente
- **Logging**: Strukturierte Protokollierung mit verschiedenen Log-Leveln

## Stichpunkte

- Syntaxfehler werden sofort erkannt, Semantikfehler erst zur Laufzeit
- try/except ermöglicht graceful error handling
- finally wird immer ausgeführt, unabhängig von Exceptions
- with-Statement stellt sicher, dass Ressourcen korrekt aufgeräumt werden
- *args und **kwargs ermöglichen flexible Funktionssignaturen
- Logging bietet strukturierte Protokollierung mit verschiedenen Wichtigkeitsstufen

