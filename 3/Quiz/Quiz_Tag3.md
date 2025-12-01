# Quiz Tag 3: Klassen, Objekte, magische Methoden, Vererbung

## 1. Klassen, Instanzen, Objekte

### Frage 1.1 (Multiple Choice)
Was beschreibt am besten eine *Instanz*?

- [ ] A) Eine Funktion innerhalb einer Klasse
- [ ] B) Der Bauplan für Objekte
- [x] C) Ein einzelnes, konkretes Objekt, das aus einer Klasse erzeugt wurde
- [ ] D) Ein Modul, das Klassen enthält

### Frage 1.2 (Multiple Choice)
Wie wird eine Instanz der Klasse `Person` korrekt erzeugt?

- [ ] A) `Person.__init__()`
- [ ] B) `p = new Person()`
- [ ] C) `p = Person`
- [x] D) `p = Person("Alice", 30)`

### Frage 1.3 (Multiple Choice, mehrere richtige Antworten möglich)
Welche Aussagen zu Klassen und Objekten in Python sind korrekt?

- [x] A) Eine Klasse beschreibt einen Bauplan für Objekte
- [x] B) Ein Objekt ist eine konkrete Ausprägung einer Klasse
- [ ] C) Es kann zu einer Klasse immer nur genau ein Objekt geben
- [ ] D) Klassen können nicht zur Laufzeit erzeugt werden

---

## 2. Instanzattribute, Klassenattribute, Properties

### Frage 2.1 (Multiple Choice)
Wo werden **Instanzattribute** typischerweise gesetzt?

- [ ] A) Innerhalb von `__str__`
- [ ] B) Im Rumpf der Klasse, direkt unter dem Klassennamen
- [x] C) In `__init__` mit `self.attribut = wert`
- [ ] D) Nur außerhalb der Klasse mit `obj.attribut = wert`

### Frage 2.2 (Multiple Choice)
Was ist ein **Klassenattribut**?

- [ ] A) Ein Attribut, das nur in `__init__` existiert
- [x] B) Ein Attribut, das auf der Klasse selbst definiert ist und von allen Instanzen geteilt wird
- [ ] C) Ein Attribut, das nur für eine bestimmte Instanz gilt
- [ ] D) Ein Attribut, das automatisch privat ist

### Frage 2.3 (Multiple Choice, mehrere richtige Antworten möglich)
Welche Aussagen zu `@property` sind korrekt?

- [x] A) `@property` macht aus einer Methode ein Attribut, das ohne Klammern aufgerufen wird
- [x] B) Mit `@<name>.setter` kann man eine Schreiblogik für das Property definieren
- [ ] C) `@property` kann nur in statischen Methoden verwendet werden
- [ ] D) `@property` verhindert grundsätzlich jede Änderung eines Attributs

---

## 3. „Zugriffsmodifikatoren“ (Konventionen)

### Frage 3.1 (Multiple Choice)
Was bedeutet ein führender Unterstrich, z.B. `_internes_attr`?

- [ ] A) Das Attribut ist wirklich privat und außerhalb der Klasse nicht zugreifbar
- [x] B) Es ist eine Konvention: „für internen Gebrauch, nicht Teil der öffentlichen API“
- [ ] C) Es wird vom Interpreter ignoriert
- [ ] D) Es macht das Attribut schneller

### Frage 3.2 (Multiple Choice)
Was passiert bei Attributen wie `__name` (zwei führende Unterstriche)?

- [ ] A) Python löscht dieses Attribut automatisch
- [ ] B) Python verbietet den Zugriff vollständig
- [x] C) Python wendet *Name Mangling* an und ändert den Attributnamen intern
- [ ] D) Es hat keinerlei Effekt

### Frage 3.3 (Multiple Choice, mehrere richtige Antworten möglich)
Welche Aussagen zu „privaten“ Attributen in Python sind korrekt?

- [x] A) Vollständig private Attribute existieren in Python nicht im Sinne anderer Sprachen
- [x] B) Name Mangling (`__name`) soll versehentliche Kollisionen in Unterklassen vermeiden
- [-] C) Auf Attribute mit führendem Unterstrich sollte von außen nur im Notfall zugegriffen werden
- [ ] D) Auf Attribute mit Unterstrich kann technisch nie von außen zugegriffen werden

---

## 4. Magische Methoden & Operatorüberladung

### Frage 4.1 (Multiple Choice)
Wofür werden magische Methoden wie `__str__` oder `__repr__` hauptsächlich verwendet?

- [ ] A) Um globale Variablen zu definieren
- [ ] B) Um das Verhalten bei `print(obj)` bzw. in der REPL zu steuern
- [ ] C) Um Imports zu beschleunigen
- [ ] D) Um Exceptions zu unterdrücken

### Frage 4.2 (Multiple Choice)
Welche magische Methode wird für den `+`-Operator verwendet?

- [ ] A) `__add__`
- [ ] B) `__plus__`
- [ ] C) `__sum__`
- [ ] D) `__op_add__`

### Frage 4.3 (Multiple Choice, mehrere richtige Antworten möglich)
Welche Aussagen zur Operatorüberladung sind korrekt?

- [ ] A) Mit `__add__` kann man definieren, wie sich eigene Objekte beim `+`-Operator verhalten
- [ ] B) Man sollte Operatorüberladung so verwenden, dass sie zur Bedeutung des Typs passt
- [ ] C) Operatorüberladung funktioniert nur für eingebaute Typen
- [ ] D) Schlecht gewählte Operatorüberladungen können Code schwerer lesbar machen

---

## 5. Vererbung und Mehrfachvererbung

### Frage 5.1 (Multiple Choice)
Was ist das Hauptziel von Vererbung?

- [ ] A) Code zu duplizieren
- [ ] B) Gemeinsames Verhalten in einer Basisklasse zu bündeln und in Unterklassen wiederzuverwenden
- [ ] C) Die Ausführung immer schneller zu machen
- [ ] D) Funktionen in Methoden umzuwandeln

### Frage 5.2 (Multiple Choice)
Welche Aussage zu `super()` in einer Unterklasse ist korrekt?

- [ ] A) `super()` ruft immer nur den Konstruktor von `object` auf
- [ ] B) `super()` funktioniert nur ohne Mehrfachvererbung
- [ ] C) `super()` hilft, die richtige nächste Klasse in der MRO (Method Resolution Order) aufzurufen
- [ ] D) `super()` darf nur in `__str__` verwendet werden

### Frage 5.3 (Multiple Choice, mehrere richtige Antworten möglich)
Welche Aussagen zu Mehrfachvererbung und MRO sind korrekt?

- [ ] A) Python bestimmt mit der MRO eine lineare Aufrufreihenfolge bei Mehrfachvererbung
- [ ] B) Bei Mehrfachvererbung sollte man `super()` konsistent in allen Klassen verwenden
- [ ] C) Mehrfachvererbung kann zu Diamantproblemen führen, wenn Klassen mehrfach in der Hierarchie vorkommen
- [ ] D) Python unterstützt grundsätzlich keine Mehrfachvererbung


