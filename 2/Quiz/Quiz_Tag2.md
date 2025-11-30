# Quiz Tag 2: Fehlerbehandlung und robuste Software

## 1. Syntax- vs Semantikfehler

### Frage 1.1 (Multiple Choice)
Wann werden Syntaxfehler erkannt?

- [ ] A) Zur Laufzeit, wenn das Programm ausgeführt wird
- [x] B) Beim Einlesen des Codes, noch bevor das Programm ausgeführt wird
- [ ] C) Erst wenn der Code kompiliert wird
- [ ] D) Nur wenn ein Debugger verwendet wird

### Frage 1.2 (Multiple Choice)
Welcher Code enthält einen Syntaxfehler?

- [ ] A) `print("Hallo")`
- [ ] B) `if x == 5: print("Richtig")`
- [x] C) `print("Hallo" `
- [ ] D) `def divide(a, b): return a / b`

### Frage 1.3 (Multiple Choice)
Was ist ein Semantikfehler?

- [ ] A) Ein Fehler in der Syntax des Codes
- [x] B) Ein logischer Fehler, bei dem der Code syntaktisch korrekt ist, aber nicht das Gewünschte macht
- [ ] C) Ein Fehler, der nur in bestimmten Programmiersprachen auftritt
- [ ] D) Ein Fehler, der immer zu einem Programmabsturz führt


---

## 2. Ausnahmen behandeln

### Frage 2.1 (Multiple Choice)
Was ist der Hauptzweck von `try/except` Blöcken?

- [ ] A) Code schneller zu machen
- [x] B) Fehler abzufangen und kontrolliert zu behandeln, statt das Programm abstürzen zu lassen
- [ ] C) Variablen zu deklarieren
- [ ] D) Funktionen zu definieren

### Frage 2.2 (Multiple Choice)
Welche Exception wird bei Division durch Null geworfen?

- [ ] A) `ValueError`
- [x] B) `ZeroDivisionError`
- [ ] C) `TypeError`
- [ ] D) `ArithmeticError`

### Frage 2.3 (Multiple Choice)
Was passiert, wenn eine Exception in einem `try`-Block auftritt, aber kein passender `except`-Block vorhanden ist?

- [ ] A) Das Programm stürzt sofort ab
- [x] B) Die Exception wird nach oben weitergeworfen (propagiert)
- [ ] C) Die Exception wird automatisch ignoriert
- [ ] D) Das Programm läuft weiter, als wäre nichts passiert

### Frage 2.4 (Multiple Choice)
Was ist eine Best Practice beim Exception Handling?

- [ ] A) Immer `except:` ohne Typ verwenden, um alle Fehler zu fangen
- [x] B) Spezifische Exception-Typen fangen (z.B. `ValueError`, `FileNotFoundError`)
- [ ] C) Nie Exception Handling verwenden
- [ ] D) Alle Exceptions stillschweigend ignorieren


---

## 3. Eigene Ausnahmen

### Frage 3.1 (Multiple Choice)
Von welcher Klasse müssen eigene Exceptions erben?

- [ ] A) `Error`
- [x] B) `Exception`
- [ ] C) `BaseException`
- [ ] D) `CustomError`

### Frage 3.2 (Multiple Choice)
Wie wirft man eine eigene Exception?

- [ ] A) `throw CustomError("Fehler")`
- [x] B) `raise CustomError("Fehler")`
- [ ] C) `error CustomError("Fehler")`
- [ ] D) `except CustomError("Fehler")`

### Frage 3.3 (Multiple Choice)
Was ist der Vorteil von Exception-Hierarchien?

- [ ] A) Code wird schneller
- [x] B) Man kann sowohl spezifische als auch allgemeine Fehlerbehandlung haben
- [ ] C) Exceptions werden automatisch geloggt
- [ ] D) Es gibt keinen Vorteil


---

## 4. finally und Aufräumen

### Frage 4.1 (Multiple Choice)
Wann wird der `finally`-Block ausgeführt?

- [ ] A) Nur wenn eine Exception auftritt
- [ ] B) Nur wenn keine Exception auftritt
- [x] C) Immer, unabhängig von Exceptions
- [ ] D) Nie

### Frage 4.2 (Multiple Choice)
Was ist der Hauptvorteil des `with`-Statements?

- [ ] A) Code wird schneller ausgeführt
- [x] B) Automatisches Ressourcen-Management (Ressourcen werden automatisch geschlossen)
- [ ] C) Variablen werden automatisch deklariert
- [ ] D) Funktionen werden automatisch aufgerufen

### Frage 4.3 (Multiple Choice)
Welche Methode(n) muss ein Context Manager implementieren?

- [ ] A) Nur `__enter__()`
- [ ] B) Nur `__exit__()`
- [x] C) `__enter__()` und `__exit__()`
- [ ] D) `__init__()` und `__del__()`

### Frage 4.4 (Multiple Choice)
Was bedeutet es, wenn `__exit__()` `False` zurückgibt?

- [ ] A) Die Exception wird unterdrückt
- [x] B) Die Exception wird weitergeworfen (propagiert)
- [ ] C) Das Programm wird beendet
- [ ] D) Der Context Manager wird nicht geschlossen


---

## 5. Seiteneffekte, *args, **kwargs

### Frage 5.1 (Multiple Choice)
Was sind Seiteneffekte in Funktionen?

- [x] A) Änderungen außerhalb des Funktionsbereichs (z.B. globale Variablen, Dateien)
- [ ] B) Rückgabewerte von Funktionen
- [ ] C) Parameter von Funktionen
- [ ] D) Lokale Variablen in Funktionen

### Frage 5.2 (Multiple Choice)
Was sammelt `*args` in einer Funktion?

- [ ] A) Keyword-Argumente in einem Dictionary
- [x] B) Positionsargumente in einem Tupel
- [ ] C) Lokale Variablen
- [ ] D) Globale Variablen

### Frage 5.3 (Multiple Choice)
Was sammelt `**kwargs` in einer Funktion?

- [ ] A) Positionsargumente in einem Tupel
- [x] B) Keyword-Argumente in einem Dictionary
- [ ] C) Lokale Variablen
- [ ] D) Globale Variablen

### Frage 5.4 (Multiple Choice)
Kann man `*args` und `**kwargs` in derselben Funktion verwenden?

- [ ] A) Nein, das ist nicht möglich
- [x] B) Ja, aber `*args` muss vor `**kwargs` stehen
- [ ] C) Ja, aber `**kwargs` muss vor `*args` stehen
- [ ] D) Ja, die Reihenfolge ist egal


---

## 6. Logging

### Frage 6.1 (Multiple Choice)
Welches Log-Level hat die niedrigste Priorität?

- [ ] A) INFO
- [ ] B) WARNING
- [x] C) DEBUG
- [ ] D) ERROR

### Frage 6.2 (Multiple Choice)
Welches Log-Level hat die höchste Priorität?

- [ ] A) INFO
- [ ] B) WARNING
- [ ] C) ERROR
- [x] D) CRITICAL

### Frage 6.3 (Multiple Choice)
Wie konfiguriert man das Logging-Modul grundlegend?

- [ ] A) `logging.setup()`
- [x] B) `logging.basicConfig()`
- [ ] C) `logging.init()`
- [ ] D) `logging.start()`

### Frage 6.4 (Multiple Choice)
Wie erstellt man einen Logger für ein spezifisches Modul?

- [ ] A) `logging.createLogger('module_name')`
- [x] B) `logging.getLogger('module_name')`
- [ ] C) `logging.newLogger('module_name')`
- [ ] D) `logging.Logger('module_name')`

### Frage 6.5 (Multiple Choice)
Was ist ein Vorteil von Logging gegenüber `print()`?

- [ ] A) Logging ist immer schneller
- [x] B) Logging bietet verschiedene Log-Level und kann in Dateien geschrieben werden
- [ ] C) Logging kann keine Fehler machen
- [ ] D) Logging ist einfacher zu verwenden


---

### Bonus 1 (Offene Frage)
Erkläre den Unterschied zwischen `try/except` und `try/except/finally`. Wann sollte man welches verwenden?

