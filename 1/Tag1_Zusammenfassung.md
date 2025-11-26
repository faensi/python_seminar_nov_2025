# Tag 1: Funktionale und iterative Vertiefung - Zusammenfassung

## Behandelte Themen

1. **Iteratoren und Generatoren** (Notebook 00)
   - Iterator-Protokoll
   - Generator-Funktionen und Generator-Expressions
   - Speichereffizienz und unendliche Sequenzen

2. **Comprehensions** (Notebook 01)
   - List, Dict und Set Comprehensions
   - Verschachtelte Comprehensions
   - Bedingungen in Comprehensions

3. **Lambda, map, filter, reduce** (Notebook 02)
   - Lambda-Funktionen
   - Funktionale Programmierung mit map(), filter(), reduce()

4. **Itertools** (Notebook 03)
   - cycle, chain, combinations, permutations
   - product, groupby, islice

5. **Sortierung mit key-Funktionen** (Notebook 04)
   - sorted() vs sort()
   - key-Parameter für komplexe Sortierungen
   - Mehrfache Sortierkriterien

6. **Rekursive Funktionen** (Notebook 05)
   - Rekursion-Grundlagen
   - Base Cases
   - Rekursion vs Iteration

7. **Rekursion Komplexität und Memoisation** (Notebook 06)
   - Komplexitätsprobleme bei Rekursion
   - Einführung Memoisation
   - Performance-Vergleich

8. **Memoisation und Dekorateure** (Notebook 07)
   - Memoisation implementieren
   - Dekorateure-Grundlagen
   - @lru_cache

## Wichtige Konzepte

- **Lazy Evaluation**: Generatoren erzeugen Werte on-the-fly
- **Funktionale Programmierung**: map, filter, reduce für datengetriebene Operationen
- **Memoisation**: Speicherung bereits berechneter Werte zur Performance-Optimierung
- **Dekorateure**: Funktionen, die andere Funktionen modifizieren
- **Rekursion**: Funktionen, die sich selbst aufrufen (mit Base Cases)

## Stichpunkte

- Generatoren sind speichereffizienter als Listen für große Datenmengen
- Comprehensions sind oft lesbarer und schneller als for-Schleifen
- Lambda-Funktionen sind nützlich für kurze, einfache Operationen
- itertools bietet viele nützliche Funktionen für Iterator-Operationen
- Rekursive Funktionen können ineffizient sein ohne Memoisation
- Dekorateure ermöglichen wiederverwendbare Funktionsmodifikationen

