"""Setup file
Usage: >> python setup.py install
"""
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-hello-garciart",
    version="2020.1",
    author="Rob Garcia",
    author_email="rgarcia@rgprogramming.com",
    description="Smart Sensor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/garciart/SmartSensor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)