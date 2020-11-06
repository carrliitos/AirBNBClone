from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name="AirBNBClone-pkg-Carrliitos",
	version="0.0.1",
	author="Benzon Carlitos Salazar",
	description="AirBNB Clone package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/carrliitos/AirBNBClone",
	python_requires='>=3.6',
	packages=find_packages('src'),
	package_dir={'': 'src'},
)