from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='datalake_utils',
    version='1.0.4',
    description="Manipulate data on Amazon S3 using Apache Hadoop filesystem compability",
    packages=["datalake_utils"],
    install_requires=['boto3'],
    # package_dir={'': 'datalake_utils'},
    # extras_require={
    #     "dev": [
    #         "pytest >= 3.7",
    #         "check-manifest",
    #         "twine"
    #     ]
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Luis Roberto de Oliveira Moro",
    author_email="luis.moro@yuca.live",
    url="https://github.com/yuca-live/yuca-datalake-utils"
)