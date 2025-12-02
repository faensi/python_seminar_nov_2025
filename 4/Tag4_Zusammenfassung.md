# Tag 4: Fortgeschrittenes OOP - Zusammenfassung

## Behandelte Themen

1. **__slots__** (Notebook 19)
   - Speicher-Optimierung
   - Einschränkungen
   - Performance-Vergleich

2. **Metaklassen** (Notebook 20)
   - Metaklassen-Grundlagen
   - type()
   - __new__
   - Anwendungsfälle

3. **Design Patterns** (Notebook 21)
   - Singleton Pattern
   - Factory Pattern
   - Observer Pattern
   - Strategy Pattern

4. **Threads und Multiprocessing** (Notebook 22)
   - threading
   - multiprocessing
   - GIL (Global Interpreter Lock)
   - Parallelisierung

5. **XML-Verarbeitung** (Notebook 23)
   - xml.etree.ElementTree
   - DOM
   - SAX
   - XML-Parsing

## Wichtige Konzepte

- **__slots__**: Speicher-Optimierung durch Begrenzung von Instanzattributen
- **Metaklassen**: Klassen, die andere Klassen erstellen
- **Design Patterns**: Bewährte Lösungsmuster für wiederkehrende Probleme
- **Threading**: Parallele Ausführung von Code in einem Prozess
- **Multiprocessing**: Echte Parallelisierung durch separate Prozesse
- **GIL**: Global Interpreter Lock begrenzt Thread-Parallelität in Python
- **XML-Parsing**: Strukturierte Datenverarbeitung mit ElementTree, DOM und SAX

## Stichpunkte

- __slots__ spart Speicher, schränkt aber Flexibilität ein
- Metaklassen sind mächtig, aber sollten sparsam verwendet werden
- Design Patterns bieten wiederverwendbare Lösungen für häufige Probleme
- Singleton stellt sicher, dass nur eine Instanz existiert
- Factory Pattern erstellt Objekte ohne die genaue Klasse zu spezifizieren
- Threading ermöglicht parallele Ausführung, ist aber durch GIL begrenzt
- Multiprocessing nutzt separate Prozesse für echte CPU-Parallelisierung
- GIL verhindert gleichzeitige Ausführung von Python-Bytecode in mehreren Threads
- ElementTree bietet eine einfache und pythonische API für XML-Verarbeitung
- DOM-Parsing lädt das gesamte XML in den Speicher, SAX ist speichereffizienter

