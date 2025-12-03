"""Setup configuration for hello_package."""

from setuptools import setup, find_packages

setup(
    name='hello_package',
    version='0.1.0',
    description='A simple hello package example',
    author='Python Seminar',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[],
)

