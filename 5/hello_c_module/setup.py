"""
setup.py - Build-Skript für das hellomodule C-Erweiterungsmodul

Kompilieren mit:
    python setup.py build_ext --inplace

Das erzeugt eine .pyd (Windows) oder .so (Linux/Mac) Datei.
"""
from setuptools import setup, Extension

# Definition der C-Erweiterung
hellomodule = Extension(
    'hellomodule',           # Name des Moduls (muss mit PyInit_xxx übereinstimmen)
    sources=['hellomodule.c']  # Liste der C-Quelldateien
)

setup(
    name='hellomodule',
    version='1.0',
    description='Ein einfaches C-Erweiterungsmodul fuer Python',
    ext_modules=[hellomodule]
)

