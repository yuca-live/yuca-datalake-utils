import pathlib
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name="datalake_utils",
  version="0.0.1",
  description="Manipulate data on Amazon S3 using Apache Hadoop's filesystem compability",
  long_description=long_description,
  long_description_content_type="text/markdown",
  author="Luis Roberto de Oliveira Moro",
  author_email="",
  license="MIT",
  packages=["yuca-datalake-utils"],
  zip_safe=False
)