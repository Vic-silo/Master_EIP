"""Instalador para el paquete "pyoperaciones"."""

from setuptools import setup

long_description = (
    open('README.txt').read()
    + '\n' +
    open('LICENSE').read()
    + '\n')

setup(
    name="RFunc",
    version="1.0",
    description="EIP Activity. Prime numers showed.",
    long_description=long_description,
    classifiers=[
        # Indica la estabilidad del proyecto. Los valores comunes son
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indique a quien va dirigido su proyecto
        "Intended Audience :: EIP",
        "Topic :: Math",
        # Indique licencia usada (debe coincidir con el "license")
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        # Indique versiones soportas, Python 2, Python 3 o ambos.
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="pyoperaciones mathematical operations prime",
    author="Victor Simo",
    author_email="vicsilo.simo@gmail.com",
    license="GNU GPLv3",
    packages=["RFunc"]
)
