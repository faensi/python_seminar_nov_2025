# Python Fortgeschritten Workspace

Dieses Repository enthält Materialien, Notebooks und Ressourcen für einen Python Fortgeschritten-Kurs. Die Inhalte sind in verschiedene Kapitel und Themenbereiche gegliedert.

## Setup environment

Um die Notebooks und Skripte auszuführen, solltest du eine eigene Python-Umgebung mit Miniconda/Conda einrichten. Das sorgt für saubere Abhängigkeiten und vermeidet Versionskonflikte. Am einfachsten geht das mit der bereitgestellten `environment.yml`:

```bash
# Neue Umgebung aus environment.yml erstellen (empfohlen)
conda env create -f environment.yml

# Umgebung aktivieren
conda activate python_fortgeschritten
```

**Bestehende Umgebung aktualisieren:**
Falls du bereits eine Umgebung hast und die Pakete aus der `environment.yml` nachinstallieren möchtest:

```bash
conda env update -n python_fortgeschritten -f environment.yml --prune
```

## Verzeichnisstruktur

```
python_fortgeschritten/
├── 1/                          # Tag 1: Funktionale und iterative Vertiefung
│   ├── 00_iteratoren_generatoren.ipynb
│   ├── 01_comprehensions.ipynb
│   ├── 02_lambda_map_filter_reduce.ipynb
│   ├── 03_itertools.ipynb
│   ├── 04_sortierung_key_funktionen.ipynb
│   ├── 05_rekursive_funktionen.ipynb
│   ├── 06_rekursion_komplexitaet_memoisation.ipynb
│   ├── 07_memoisation_dekorateure.ipynb
│   └── Tag1_Zusammenfassung.md
├── 2/                          # Tag 2: Fehlerbehandlung und robuste Software
│   ├── 08_syntax_semantikfehler.ipynb
│   ├── 09_ausnahmen_behandeln.ipynb
│   ├── 10_eigene_ausnahmen.ipynb
│   ├── 11_finally_aufraeumen.ipynb
│   ├── 12_seiteneffekte_args_kwargs.ipynb
│   ├── 13_logging.ipynb
│   └── Tag2_Zusammenfassung.md
├── 3/                          # Tag 3: Objektorientierung vertieft
│   ├── 14_klassen_instanzen_objekte.ipynb
│   ├── 15_instanz_klassenattribute_properties.ipynb
│   ├── 16_zugriffsmodifikatoren.ipynb
│   ├── 17_magische_methoden_operator_ueberladung.ipynb
│   ├── 18_vererbung_mehrfachvererbung.ipynb
│   └── Tag3_Zusammenfassung.md
├── 4/                          # Tag 4: Fortgeschrittenes OOP
│   ├── 19_slots.ipynb
│   ├── 20_metaklassen.ipynb
│   ├── 21_design_patterns.ipynb
│   ├── 22_threads_multiprocessing.ipynb
│   ├── 23_xml_verarbeitung.ipynb
│   └── Tag4_Zusammenfassung.md
├── 5/                          # Tag 5: Anwendungen und Erweiterungen
│   ├── 24_packaging_libraries.ipynb
│   ├── 25_numpy.ipynb
│   ├── 26_scipy_pandas.ipynb
│   ├── 27_matplotlib.ipynb
│   ├── 28_os_schnittstellen.ipynb
│   ├── 29_c_cpp_extending_embedding.ipynb
│   ├── 30_tkinter.ipynb
│   ├── 31_textverarbeitung_regex.ipynb
│   └── Tag5_Zusammenfassung.md
├── data/                       # Datensätze für Übungen
├── imgs/                       # Bilder und Grafiken
├── EinführungsNotebooks/       # Einführungsmaterialien
│   └── jupyter_intro.ipynb
├── extras/                     # Zusätzliche Materialien
│   ├── cheat_sheets/
│   └── debugging_tipps/
├── environment.yml             # Conda-Umgebungskonfiguration
└── README.md                   # Diese Datei
```

### Erklärung der Verzeichnisse

- **1/, 2/, 3/, 4/, 5/**: Tages-Verzeichnisse mit den entsprechenden Notebooks. Die Notebooks sind fortlaufend nummeriert (00-32).
- **data/**: Enthält Datensätze, die in den Notebooks verwendet werden. Diese werden typischerweise durch Code in den Notebooks erzeugt.
- **imgs/**: Enthält Bilder und Grafiken, die in den Notebooks verwendet werden.
- **EinführungsNotebooks/**: Enthält Einführungsmaterialien, insbesondere eine Einführung in Jupyter Notebooks.
- **extras/**: Zusätzliche Materialien wie Cheat Sheets und Debugging-Tipps.

### Nummerierung der Notebooks

Die Notebooks sind fortlaufend über alle Tage hinweg nummeriert:
- Tag 1: 00-07
- Tag 2: 08-13
- Tag 3: 14-18
- Tag 4: 19-23
- Tag 5: 24-31

## Wichtige Dateien

- **environment.yml**: Conda-Umgebungskonfiguration mit allen benötigten Paketen
- **TagN_Zusammenfassung.md**: Zusammenfassungen für jeden Tag mit behandelten Themen und wichtigen Konzepten

## Hinweise zur Nutzung

### Empfohlene Reihenfolge

1. Beginne mit dem Einführungsnotebook: `EinführungsNotebooks/jupyter_intro.ipynb`
2. Arbeite die Notebooks in der nummerierten Reihenfolge durch (00, 01, 02, ...)
3. Jeder Tag baut auf den vorherigen auf, daher ist die Reihenfolge wichtig

### Selbststudium

- Führe alle Code-Beispiele aus
- Versuche die Aufgaben selbst zu lösen, bevor du die Musterlösungen anschaust
- Die Musterlösungen sind standardmäßig eingeklappt (klicke auf "Lösung:" um sie zu sehen)

### Unterricht und Workshops

- Die Notebooks können als Präsentationsmaterial verwendet werden
- Aufgaben können als Übungen während des Unterrichts bearbeitet werden
- Musterlösungen können gemeinsam besprochen werden

### Aufgaben und Lösungen

Jedes Notebook enthält:
- Theoretische Erklärungen
- Code-Beispiele
- Aufgaben zum Üben
- Musterlösungen (standardmäßig eingeklappt)

Die Musterlösungen sind in Markdown-Abschnitten mit der Überschrift "#### Lösung:" oder "##### Lösung:" versteckt. Klicke auf die Überschrift, um die Lösung zu sehen.

## Technische Details

- **Python Version**: 3.12
- **Notebook Format**: Jupyter Notebook (.ipynb)
- **Hauptpakete**: NumPy, SciPy, Pandas, Matplotlib, Jupyter

## Support

Bei Fragen oder Problemen:
1. Überprüfe die Zusammenfassungsdateien (TagN_Zusammenfassung.md)
2. Schaue dir die Musterlösungen in den Notebooks an
3. Konsultiere die offizielle Python-Dokumentation

Viel Erfolg beim Lernen!

