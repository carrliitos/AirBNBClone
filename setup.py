from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name="AIRBNB-pkg-Carrliitos",
	version="0.0.1",
	author="Benzon Carlitos Salazar",
	description="An Air BNB clone package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/carrliitos/AirBNBClone",
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
	packages=find_packages('models'),
	package_dir={'': 'models'},
)