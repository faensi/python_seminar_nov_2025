# Tag 3: Objektorientierung vertieft - Zusammenfassung

## Behandelte Themen

1. **Klassen, Instanzen, Objekte** (Notebook 14)
   - Klassen-Grundlagen und Objektmodell
   - "Everything is an object" - Python's Objektmodell
   - Klassen definieren und instanziieren
   - __init__ Methode
   - self Parameter
   - Instanzattribute und Methoden

2. **Instanz- vs Klassenattribute, Properties** (Notebook 15)
   - Instanz- vs Klassenattribute (Unterschiede, Verwendung)
   - Mutable vs Immutable Klassenattribute (häufiger Fehler)
   - Zugriff auf Klassenattribute (über Klasse vs Instanz)
   - @property Decorator (Grundlagen, Setter, Deleter)
   - Berechnete vs gespeicherte Properties
   - Best Practices und häufige Fehler

3. **Zugriffsmodifikatoren** (Notebook 16)
   - Public, Protected (_), Private (__) Attribute
   - Name Mangling (Mechanismus und Funktionsweise)
   - Python's Philosophie: "We're all consenting adults"
   - Wann welchen Zugriffsmodifikator verwenden
   - Best Practices und Konventionen

4. **Magische Methoden und Operator-Überladung** (Notebook 17)
   - __str__ vs __repr__ (Unterschiede, Verwendung, Best Practices)
   - Vergleichsoperatoren (__eq__, __ne__, __lt__, etc.)
   - Arithmetische Operatoren (__add__, __sub__, __mul__, etc.)
   - In-Place Operatoren (__iadd__, __isub__, etc.)
   - Container-Methoden (__len__, __getitem__, __setitem__, __contains__)
   - Weitere magische Methoden (__call__, __enter__/__exit__)
   - Python's Data Model und magische Methoden
   - Best Practices für magische Methoden

5. **Vererbung und Mehrfachvererbung** (Notebook 18)
   - Einfache Vererbung (Grundlagen, Vorteile, Verwendung)
   - Method Overriding
   - isinstance() und issubclass()
   - Polymorphismus
   - super() (Funktionsweise, vs direkter Aufruf, mit Argumenten)
   - Mehrfachvererbung (Grundlagen, Diamond Problem)
   - Method Resolution Order (MRO) - Was ist das?
   - MRO Algorithmus (C3 Linearization)
   - MRO anzeigen (__mro__, mro())
   - Vererbung vs Komposition
   - Best Practices und häufige Fehler

## Wichtige Konzepte

- **Klassen und Objekte**: Objektorientierte Programmierung in Python
- **Vererbung**: Wiederverwendung von Code durch Klassenhierarchien
- **Polymorphismus**: Verschiedene Implementierungen derselben Schnittstelle
- **Encapsulation**: Kapselung von Daten und Methoden
- **MRO**: Bestimmt die Reihenfolge der Methodenauflösung bei Mehrfachvererbung

## Stichpunkte

- Klassen sind Vorlagen für Objekte
- In Python ist alles ein Objekt (Zahlen, Strings, Funktionen, Klassen)
- self verweist auf die aktuelle Instanz
- Instanzattribute sind individuell, Klassenattribute werden geteilt
- Mutable Klassenattribute (Listen/Dicts) führen zu unerwartetem Verhalten
- @property ermöglicht Methoden wie Attribute zu verwenden, mit Validierung
- @property.setter und @property.deleter für kontrollierten Zugriff
- Python hat keine echten privaten Attribute, nur Konventionen (_ und __)
- Name Mangling verhindert versehentliche Überschreibung in Vererbung
- Python's Philosophie: "We're all consenting adults" - Konventionen statt Verbote
- __str__ für Benutzer, __repr__ für Entwickler (sollte eindeutig sein)
- Operator-Überladung ermöglicht intuitive Syntax für eigene Klassen
- Magische Methoden ermöglichen spezielle Verhaltensweisen (Container, Callable, etc.)
- Vererbung für "ist-ein" Beziehungen, Komposition für "hat-ein" Beziehungen
- super() ist flexibel und MRO-konform (empfohlen statt direkter Aufruf)
- MRO (C3 Linearization) löst Konflikte bei Mehrfachvererbung eindeutig
- Diamond Problem wird durch MRO gelöst
- isinstance() und issubclass() prüfen Vererbungsbeziehungen
- Polymorphismus ermöglicht verschiedene Implementierungen derselben Schnittstelle

