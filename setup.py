from setuptools import setup

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name="yuca_datalake_utils",
    version="1.0.0",
    description="The datalake_utils module makes it simple for you to manipulate data on Amazon S3 using Hadoop's filesystem compability",
    py_modules=["datalake_utils"],
    package_dir={"": "src"},
    # extras_require={
    #     "dev": [
    #         "pytest >= 3.7",
    #         "check-manifest",
    #         "twine"
    #     ]
    # },
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "Programming Language :: Python :: 3.7",
    #     "Programming Language :: Python :: 3.8",
    #     "Topic :: Software Development :: Libraries :: Python Modules",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent"
    # ],
    python_requires=">=3",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    author="Luis Roberto de Oliveira Moro",
    # author_email="vaidhyanathan.sm@gmail.com",
    # url="https://github.com/smv1999/number-utility"
)
