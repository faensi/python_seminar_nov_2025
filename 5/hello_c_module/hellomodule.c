/* hellomodule.c - Einfaches Python C-Erweiterungsmodul */
#define PY_SSIZE_T_CLEAN
#include <Python.h>

/* Globaler Counter (C int) */
static int counter = 0;

/* Funktion 1: Hallo Welt ausgeben */
static PyObject* hello_world(PyObject *self, PyObject *args) {
    printf("Hallo Welt!\n");
    Py_RETURN_NONE;
}

/* Funktion 2: Counter um 1 erhöhen und zurückgeben */
static PyObject* increment_counter(PyObject *self, PyObject *args) {
    counter++;
    return PyLong_FromLong(counter);
}

/* Optionale Funktion: Counter zurücksetzen */
static PyObject* reset_counter(PyObject *self, PyObject *args) {
    counter = 0;
    Py_RETURN_NONE;
}

/* Optionale Funktion: Aktuellen Counter-Wert abfragen */
static PyObject* get_counter(PyObject *self, PyObject *args) {
    return PyLong_FromLong(counter);
}

/* Methodentabelle: Definiert die Funktionen, die Python sieht */
static PyMethodDef HelloMethods[] = {
    {"hello_world", hello_world, METH_NOARGS, "Gibt 'Hallo Welt!' aus"},
    {"increment_counter", increment_counter, METH_NOARGS, "Erhoeht den Counter um 1"},
    {"reset_counter", reset_counter, METH_NOARGS, "Setzt den Counter auf 0 zurueck"},
    {"get_counter", get_counter, METH_NOARGS, "Gibt den aktuellen Counter-Wert zurueck"},
    {NULL, NULL, 0, NULL}  /* Sentinel */
};

/* Moduldefinition */
static struct PyModuleDef hellomodule = {
    PyModuleDef_HEAD_INIT,
    "hellomodule",                      /* Name des Moduls */
    "Ein einfaches C-Erweiterungsmodul mit Hallo Welt und Counter",  /* Docstring */
    -1,                                 /* Globaler Zustand (kein Support für Subinterpreter) */
    HelloMethods                        /* Methodentabelle */
};

/* Modul-Initialisierungsfunktion */
PyMODINIT_FUNC PyInit_hellomodule(void) {
    return PyModule_Create(&hellomodule);
}

